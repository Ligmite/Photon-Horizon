# Photon for Horizon

Photon for Horizon brings [SixthSurge's Photon](https://github.com/sixthsurge/photon) to
[Horizon](https://github.com/horizon-rust/horizon), the Minecraft: Java Edition rewrite in Rust. It
runs Photon's deferred rendering pipeline on Horizon's OptiFine/Iris-format shader-pack runtime
(the `shaders/` folder format), so the pack's own materials, lighting and post-processing run
unmodified in structure, with the full Photon settings tree available in Horizon's **Shader
Options** screen.

The base is the **HDR fork** of Photon v1.4 (`rrtt217/photon`, branch `hdr-clean`), which adds display-peak-aware
HDR tonemapping (Lottes extended, Reinhard piecewise extended, Hable/Uncharted-2 extended, ACES 2.0
SSTS) and an FP16 colour-buffer option. All of Photon v1.4 is present; the HDR path is an extra.

## Features

Photon's deferred pipeline, as-is: a 16-target G-buffer filled by the pack's `gbuffers_*` programs,
then `deferred*` and `composite*` passes that shade it.

| | |
|---|---|
| **Materials** | labPBR normal/specular maps, GGX specular with sun-disk area-light approximation, energy-conserving diffuse, SSS sheen, hardcoded block materials |
| **Lighting** | Directional sky/sun/moon/block light, coloured light maps, handheld light, cloud shadows |
| **Shadows** | Cascaded orthographic shadow map, PCSS with variable penumbra, coloured shadows, screen-space ray-traced contacts (SSRT) |
| **Ambient occlusion** | GTAO (bent normals, analytic arc integration) or SSAO, temporally accumulated, vanilla AO blend |
| **Reflections** | Screen-space reflections with GGX VNDF sampling for rough materials, sky-map fallback |
| **Atmosphere & fog** | Bruneton-style scattering LUT, volumetric fog with shadow-mapped shafts, crepuscular rays, biome fog |
| **Clouds** | Five volumetric layers (cumulus, congestus, altocumulus, cirrus, cirrocumulus, noctilucent), checkerboard temporal upscaling, cloud shadow map |
| **Sky** | Sun, moon, stars, galaxy, aurora, rainbow, custom sky |
| **Water** | Iterated Gerstner waves, parallax, absorption/scattering, refraction, caustics, Snell's window |
| **Post** | COD:AW bloom, TAA/TAAU, DOF, motion blur, FXAA, CAS, colour grading, auto exposure, purkinje shift |
| **Tonemapping** | Lottes (default), ACES fit/full, Hejl, Hable, Tech, Ozius, Reinhard — plus the HDR operators behind `HDR_OUTPUT` |
| **World** | Waving plants and leaves, POM with parallax shadow, edge highlight, rain puddles, weather system, lightning flashes |

Everything is configurable in game: **Options → Horizon Graphics → Shader Packs → Photon-Horizon →
Shader Options...** with Low/Medium/High/Ultra profiles, grouped pages, sliders and toggles.
[SETTINGS.md](SETTINGS.md) lists every option with its default and range.

## Install

1. Build or install Horizon.
2. Copy `Photon-Horizon.zip` into the game's `shaderpacks/` folder (next to `options.txt`).
   Alternatively unzip it so `shaderpacks/Photon-Horizon/shaders/` exists.
3. Options → Horizon Graphics → Shader Packs → **Photon-Horizon**.
4. Open **Shader Options...** and pick a profile to start.

To build the zip from source: `./build-pack.sh` (or `.\build-pack.ps1`).

## Horizon notes

The pack is Photon's code adapted where Horizon's pack runtime differs from Iris:

- **Horizon LOD (distant terrain)** works through the pack's terrain program. Set
  **Fog → LOD Distance** to Horizon's *LOD Distance* (in chunks) so fog fades over the far view
  instead of ending at the chunk render distance.
- **HDR**: Horizon presents HDR itself. `HDR_OUTPUT=0` (default) keeps Photon's SDR output for
  Horizon's present stage; `HDR_OUTPUT=1` enables the fork's HDR tonemapping with paper-white and
  peak values from the pack's options. That path is meant for rrtt217's HDR Mod: Horizon's present
  clamps the frame to 0..1 and decodes gamma 2.2 before mapping it to the display, so a
  display-referred HDR frame loses its highlights. Treat `HDR_OUTPUT=1` as a way to test the
  fork's operators, and set real HDR brightness in Horizon's **Graphics → HDR** settings.
- **SH skylight** is off by default; its compute program is present and can be enabled once it is
  verified on your driver.
- **labPBR maps** need the small renderer patch in [`patches/`](patches/): Horizon binds the
  `normals`/`specular` samplers of OptiFine-format packs to 1×1 stand-ins. Without the patch the
  pack still runs with its full material model, but resource-pack normal/specular maps are flat.
- **Hardcoded block materials** rely on `mc_Entity`, which Horizon supplies on its flat-draw path;
  on the default Windows path they are inactive (labPBR maps are unaffected).
- **Removed:** Photonics, Distant Horizons, Voxy and Iris's LPV coloured-light volume — mod
  features with no Horizon counterpart. See [PORTING.md](PORTING.md) for the exact file and
  settings changes.

## Checking a build

Horizon's loader can read the whole pack without a GPU:

```powershell
.\validate-pack.ps1 -Horizon C:\path\to\horizon
```

or `./validate-pack.sh /path/to/horizon`. It preprocesses every stage file, translates every
program with naga and loads each dimension's post set, printing any program it had to skip and why.

## Layout

```
shaders/                  the pack (settings.glsl, shaders.properties, world folders, include/, program/, image/)
patches/                  optional Horizon renderer patch for labPBR maps
tools/                    static checks and the settings reference generator
SETTINGS.md               every option, default and range
TROUBLESHOOTING.md        first run, common problems, reading loader notes
PORTING.md                changes from upstream Photon
validate-pack.ps1/.sh     run Horizon's loader over the pack
build-pack.ps1/.sh        build Photon-Horizon.zip
```

## Credits

**Photon** — © 2021–2025 **Benjamin Stott ("SixthSurge")**, author of Photon Shaders. 

- Menu translations: NakiriRuri and OrzMiku (Chinese Simplified), ChunghwaMC (Chinese Traditional),
  Jmayk (Italian), Timtaran (Russian), shihyeon (Korean), DVRKHz (Spanish), Patatagod69 (Dutch),
  sincerity (Estonian)
- Emin — shadow bias method from Complementary Reimagined
- DrDesten — depth tolerance for SSR
- Essentuan — Photonics mod support
- Jessie — f0/f82 values for labPBR hardcoded metals
- Sledgehammer Games — bloom downsampling (Call of Duty: Advanced Warfare)
- momentsingraphics.de — blue noise texture
- NASA Scientific Visualization Studio — galaxy image

**HDR fork** — **rrtt217**, branch [`hdr-clean` of `rrtt217/photon`](https://github.com/rrtt217/photon/tree/hdr-clean)
(the pack this port is based on), made for **rrtt217's HDR Mod**
([Minecraft-HDR-Mod](https://github.com/rrtt217/Minecraft-HDR-Mod)). The fork adds the
display-peak-aware tonemapping (Lottes extended, Reinhard piecewise extended, Hable/Uncharted-2
extended, ACES 2.0 SSTS) and the FP16 colour-buffer option that this port keeps.

**Tonemapping** — ACES components © 2015 Academy of Motion Picture Arts and Sciences (A.M.P.A.S.);
the RRT + ODT fit is by **Stephen Hill**; the Uncharted 2 curve is by **John Hable**.

**Horizon** — the runtime this port targets, © the Horizon contributors, MIT licensed.

This port's adaptation work is released under the same licence as Photon (see below), with the
HDR additions under the HDR fork's terms.

## Licence

Photon is distributed under the **Photon Shaders License Agreement** (© 2021–2025 Benjamin Stott).
It allows use, personal modification, study and redistribution, with two restrictions: it may not
be redistributed on platforms that pay creators directly or indirectly (Modrinth, CurseForge, …)
without the author's written permission, and it may not be sold.

The full text is in [LICENSE](LICENSE). ACES components carry their own licence in
[licenses/LICENSE-ACES.md](licenses/LICENSE-ACES.md).

