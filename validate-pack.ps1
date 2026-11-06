# Runs Horizon's own shader-pack loader over the Photon port, with no GPU.
#
#   .\validate-pack.ps1 -Horizon C:\path\to\horizon
#
# What it does: points HORIZON_TEST_SHADER_PACKS at this folder (which holds
# shaders/) and runs horizon-shaders' `real_packs_read` ignored test. That test
# preprocesses every stage file, translates every composite-style program, and
# loads each dimension's post-processing set (gbuffers, shadow, compute) through
# the same code the game uses, printing errors, notes and timings.
#
# Exit code 0 means the loader accepted the pack (programs may still be listed
# as skipped: read the output). Set SHOW_ERRORS=1 for the first error of each
# failed program, BACKENDS=1 to also translate every module through wgpu's
# backends (SPIR-V, HLSL, MSL, GLSL).
param(
    [Parameter(Mandatory = $true)][string]$Horizon,
    [string]$Pack = $PSScriptRoot
)

$ErrorActionPreference = 'Stop'
if (-not (Test-Path (Join-Path $Horizon 'Cargo.toml'))) {
    throw "No Cargo.toml in $Horizon — pass the root of the Horizon checkout."
}
if (-not (Test-Path (Join-Path $Pack 'shaders'))) {
    throw "No shaders folder in $Pack — pass the pack root (photon-horizon)."
}

$env:HORIZON_TEST_SHADER_PACKS = (Resolve-Path $Pack).Path
$env:SHOW_ERRORS = '1'
Write-Host "Reading pack at $env:HORIZON_TEST_SHADER_PACKS with Horizon at $Horizon" -ForegroundColor Cyan

Push-Location $Horizon
try {
    cargo test -p horizon-shaders --release -- --ignored --nocapture real_packs_read
} finally {
    Pop-Location
}
