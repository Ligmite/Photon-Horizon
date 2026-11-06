# Troubleshooting and first-run checklist

## First run

1. Put `Photon-Horizon.zip` in the game's `shaderpacks/` folder.
2. Options → Horizon Graphics → Shader Packs → **Photon-Horizon**.
3. Open **Shader Options...** and start from a profile (Medium is a good balance).
4. Look at the sky, a shadowed wall and water: GTAO darkens corners, shadows have
   soft penumbrae, water has waves and reflections, clouds are volumetric.
5. If the screen is black or the pack is not listed, see below.

## Read the loader's notes

The pack's notes are what Horizon prints when it loads a pack (and what
`validate-pack.ps1` prints). Phrases and what they mean:

| Note | Meaning | Action |
|---|---|---|
| `zero for now: name ...` | A declared uniform Horizon does not fill; reads 0 | Harmless for `currentRenderedItemId`/`clouds_offset`; anything else is a mapping gap |
| `<program>: skipped` with `file:line: message` | naga rejected a construct | The message names the file and line; fix or disable the option that enables it |
| `... is not provided yet` (sampler) | The sampler's type does not match any texture (e.g. 3D LUT expected, 2D supplied) | Check the `texture.*` line for that stage/name and its `TEXTURE_3D` size line |
| `this GPU can't write images from a fragment shader` | Storage images unsupported by the adapter | Only LPV/coloured-lights programs used those; they are removed |
| `shadow: no program; the shadow map stays clear` | No shadow program loaded | Should not happen (all three dimensions ship `shadow`); check the notes above it |
| `the pack requires 'X', which is not supported yet` | An `iris.features.required` feature Horizon lacks | The port does not require any |

`SHOW_ERRORS=1` (default in the scripts) prints the first error of every failed
program. `BACKENDS=1` additionally translates every module through wgpu's
backends (SPIR-V, HLSL, MSL, GLSL), which catches device-specific problems.

## Common problems

**The pack does not appear in Shader Packs.** The zip must hold `shaders/` at
its root (it does); an unzipped folder must be
`shaderpacks/Photon-Horizon/shaders/...`. Re-download or re-extract if the
folder layout was changed.

**Black or corrupt screen.** Check the notes for a skipped `final` program or a
`deferred` program; a skipped `final` leaves the frame black. Also check that
`colortex` formats were read (`buffers.glsl` is included by `final.fsh`).

**Night is pitch black.** `moon_phase_brightness` is built from a multi-line
`uniform.` expression in `shaders.properties`; Horizon joins backslash
continuations, so it parses — but if you edit that line, keep the trailing
backslashes.

**No normal/specular detail on blocks.** The renderer patch in `patches/` is not
applied: Horizon binds 1×1 stand-ins for `normals`/`specular` in OptiFine-format
packs. Apply it, rebuild, and use a LabPBR resource pack.

**Distant terrain (Horizon's LODs) is hidden behind fog.** Photon's border fog
ends at the chunk render distance. Set **Fog → LOD Distance** to the same value
as Horizon's *LOD Distance* setting (in chunks, e.g. 64); 0 leaves it off. The
fog then fades over the whole far view. (For a quick check, turning **Border
Fog** off also reveals the LODs.)

**LOD tiles pop or flicker at the full-detail boundary.** Horizon fades LOD
tiles in and out with a per-instance dither and biases their depth; OptiFine
packs do not receive that per-instance fade code, so the pack path draws tiles
whole. Old and new tiles then overlap at nearly the same depth around the
boundary, which z-fights and pops. This is a renderer gap (the fade would have
to be passed to pack terrain programs), not a setting. Interim: raise *LOD
Distance* so the switch is farther away, or disable TAA to see the geometry
without smearing. Fix path: `patches/HORIZON-PATCH.md` (the same place the LabPBR
binding belongs).

**Hardcoded block materials do nothing (Windows DX12/Vulkan).** `mc_Entity` is
only supplied on Horizon's flat-draw path; labPBR maps still work.

**TAAU / SH Skylight off.** Both are off by default: SH skylight's compute has
not been verified on Horizon's compute path, and TAAU is an upscaler that needs
your display setup. Both are in Shader Options.

**Water is flat grey / sky is black.** A `sampler3D` custom texture did not load
(`image/atmosphere/scattering.dat`, `image/worley_*.dat`): check the notes for
`texture.deferred...` and that `image/` files survived the zip.

## Reporting a translation failure

Paste the block starting at the program name, e.g.:

```
photon-horizon: ...
  deferred4: skipped
  include/lighting/diffuse_lighting.glsl:123: ...
```

with the `SHOW_ERRORS=1` line, and the file/line is usually enough to patch the
pack. The pack keeps upstream Photon's structure, so fixes stay small.
