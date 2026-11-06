# Porting notes: changes from upstream Photon

Base: Photon v1.4 plus the HDR additions (the `hdr-clean` branch of `rrtt217/photon`, 618 files under `shaders/`).
This pack: 555 files. Everything not listed here is upstream, byte for byte.

## Removed: features with no Horizon counterpart (63 files)

Photonics (the mod that supplies ReSTIR light integration), Distant Horizons and Voxy (LoD mods
that supply their own geometry and depth), and Iris's LPV coloured-light volume:

```
photonics/*                         (8 files)
ph_lights.json
program/lpv/{setup,floodfill}.csh   (Iris coloured lights)
program/{shadow_voxels,voxy_opaque,voxy_translucent}.*, program/voxy.json
program/dh_terrain.*, program/dh_water.*
include/lighting/lpv/*              (4 files)
include/fog/lpv_fog.glsl
world*/dh_*                         (Voxy/DH terrain passes)
world*/voxy_*                       (Voxy geometry)
world*/gbuffers_voxels.*            (Voxy-only gbuffer)
world*/shadow_voxels.*              (Voxy shadows)
world*/setup.csh, world*/shadowcomp.csh   (LPV compute; stubs only)
```

`include/misc/lod_mod_support.glsl` stays: without `DISTANT_HORIZONS`/`VOXY` it defines
`combined_depth_tex = depthtex1` and the combined projection as the camera's, which is what
Horizon needs.

## `settings.glsl`

- Removed the option groups and defines that only the removed features read:
  `COLORED_LIGHTS`, `COLORED_LIGHTS_*`, `VOXEL_VOLUME_*`, `LPV_VL*`, `DH_OVERDRAW_*`,
  `NOISE_ON_DH_TERRAIN`, `PHOTONICS_*`, `HDR_ENABLED`/`HDR_MOD_INSTALLED` (dev switches).
- Added a **Horizon HDR** group (see `shaders.properties` below): `HDR_OUTPUT` (0/1, default 0),
  `HDR_PAPER_WHITE`, `HDR_PEAK_BRIGHTNESS`, `HDR_UI_BRIGHTNESS`, `hdr_tonemap`, `HDR_USE_FP16`.
- `SH_SKYLIGHT` is now off by default (`//#define`): the SH irradiance compute
  (`deferred4_a.csh`) needs Horizon's compute path to be verified first.
- Dropped the decoy `#ifdef` blocks of the removed switches; kept the rest.

## `shaders.properties`

- `screen = … [mods]` → `… [hdr]`; `screen.mods` became `screen.hdr` listing the HDR options,
  with `screen.hdr.columns = 1`.
- Removed the menus of features Horizon cannot run: `[distant_horizons]`, `[photonics]`,
  `[photonics_sharp]`, `[photonics_restir]`, `[colored_lights]`, `[lpv_vl]`, `[hdrmod]`.
- Removed `COLORED_LIGHTS` from `screen.lighting`, `[lpv_vl]` from `screen.fog`, and those
  tokens from the `profile.*` lines.
- Removed the program toggles of the LPV compute (`program.world*/setup.enabled`,
  `program.world*/shadowcomp.enabled`) and the `#ifdef COLORED_LIGHTS` shadow-culling block.
- `uniform.float.lightning_flash_iris` no longer reads Iris's `lightningBoltPosition`; it uses
  the pack's own `lightning_flash_of` (computed from the sky colour).
- Removed the Distant Horizons property block (`dhShadow.enabled`), the Photonics properties,
  the coloured-light `image.*` block (light data, voxel volume, light volumes), the Photonics GI
  image, and the Distant Horizons uniform block (`combined_projection_matrix*`,
  `dhRenderDistance`).
- Added `separateEntityDraws = true`: Photon's settings define
  `USE_SEPARATE_ENTITY_DRAWS` on modern versions, and Horizon draws translucent entities after
  deferred when the property is set, matching what the shader code expects.
- Trimmed the removed options from the `sliders` list.

## `include/global.glsl`

- Photonics shorthand (`PHOTONICS_IN_USE`) removed: the mod never defines it on Horizon.
- Added the Horizon HDR block: `HDR_OUTPUT == 1` defines `HDR_ENABLED` and the three HDR
  brightness constants from the pack's options, so the fork's HDR tonemap and encode paths
  compile without an HDR mod's uniforms.

## Horizon LOD support (distant terrain)

Horizon draws distant terrain with its own LOD tiles, but shares its terrain meshes and passes, so
Photon's `gbuffers_terrain` already shades them. The one thing that hid them was Photon's fog: its
`far` uniform is Horizon's *chunk render distance* (the detail distance), so `border_fog` faded
everything past it to the fog colour.

- `settings.glsl`: new `LOD_DISTANCE` value option (chunks, default 0 = off), under Fog.
- `include/misc/lod_mod_support.glsl`: defines `HORIZON_LOD_FOG` and `lod_fog_range()` when
  `LOD_DISTANCE > 0` (chunks × 16 blocks), and `lod_fog_range()` for a real LoD mod otherwise.
- `include/fog/simple_fog.glsl`: `border_fog` fades over `lod_fog_range()` with Photon's own
  LOD curve (`exp2(-2.4 · d²)`) when Horizon LOD or a LoD mod is active, and skips the
  near-distance vertical cutoff there.
- `include/fog/overworld/analytic.glsl` and `raymarched.glsl`: the sky rays' `fog_end` becomes
  `max(far, lod_fog_range())`, so the horizon haze matches the far view.
- `include/fog/end_fog_vl.glsl`: the volumetric fog's ray length is clamped to the same
  distance instead of `far`, so it stays coherent over distant terrain.
- `shaders.properties`: `LOD_DISTANCE` added to the Fog screen and to `sliders`.

This is the pack-side replacement for Photon's Distant Horizons integration: no LoD mod, no
renderer change. With `LOD_DISTANCE = 0` the pack behaves exactly as before.

Known gap: Horizon fades LOD tiles in/out with a per-instance dither and biases their depth
(`gfx/lod.rs`, `terrain.wgsl`'s `faded`/`instance_step`). Pack terrain programs get only the
instance origin, not that fade code, so tiles pop and z-fight at the detail boundary. Closing it
needs the renderer to pass the fade to packs and the pack to implement the dither; see
`patches/HORIZON-PATCH.md`.

## Not changed (deliberately)

`include/buffers.glsl`, the world-folder stubs, the `program/` pass bodies, `include/` feature
code, `lang/*` and the `image/` assets are upstream. The pack therefore runs Photon's own
algorithms: GTAO/SSAO, SSR, PCSS/VPS/SSRT shadows, crepuscular rays, volumetric fog and clouds,
Bruneton atmosphere, Gerstner water, COD:AW bloom, TAA/TAAU, DOF, motion blur, FXAA, CAS,
grading, POM and the weather system, with the same settings and profiles as upstream.
