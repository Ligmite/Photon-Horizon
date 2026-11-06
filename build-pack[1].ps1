# Builds Photon-Horizon.zip from the pack sources (shaders/ at the zip root).
param([string]$Out = "Photon-Horizon.zip")
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$zip = Join-Path $root $Out
if (Test-Path $zip) { Remove-Item -Force $zip }
Compress-Archive -Path (Join-Path $root 'shaders'), (Join-Path $root 'README.md'), (Join-Path $root 'LICENSE') `
    -DestinationPath $zip -CompressionLevel Optimal
Write-Host "wrote $zip"
