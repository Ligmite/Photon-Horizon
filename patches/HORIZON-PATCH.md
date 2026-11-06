# Horizon renderer patch: labPBR maps for shader packs

`photon-labpbr-pack-atlas.patch` makes Horizon bind the resource packs' labPBR normal
(`_n.png`) and specular (`_s.png`) maps to the `normals` and `specular` samplers of
OptiFine-format shader packs, in the block atlas's own grid. Without it those samplers are
1×1 stand-ins (flat normal, black specular), so Photon's material system gets no per-block
material data.

## Why

Iris-format packs read per-block material data from `sampler2D normals` and
`sampler2D specular`. Horizon loads and binds these maps for its own WGSL packs
(`native_material.rs`, `native_post.rs`) but the OptiFine-format path binds stand-ins.
The data is already loaded; only the pack binding is missing.

## What it changes

- `crates/horizon-client-render/src/gfx/pack_atlas.rs` — `PackAtlas` keeps its layer count
  and rows; new `with_labpbr` copies the labPBR arrays into two more atlases over the same
  grid (same columns, rows, mip levels), and `labpbr()` returns their views. Maps whose size
  is not the atlas's sprite size are skipped (the stand-ins stay).
- `crates/horizon-client-render/src/gfx.rs` — builds the atlases when a pack starts if
  `pbr_maps` exist, and passes them to the pack renderer (`World.labpbr`).
- `crates/horizon-client-render/src/gfx/pack_post.rs` — `World`/`PackPost` carry the views;
  `Source::Normals`/`Source::Specular` bind them; both sample linearly now. Three tests pass
  `labpbr: None`.
- `crates/horizon-client/src/game/shader_packs.rs` and `game.rs` — `picks_native_pack`
  becomes `picks_pack`, true for any selected pack, so resource loads read the labPBR maps
  for `shaders/` packs too. Without this `pbr_maps` stays `None` and there is nothing to bind.

Packs that do not use the samplers are unaffected: no format, sampler or API change.

## Apply and build

From the root of a Horizon checkout:

```sh
git apply photon-labpbr-pack-atlas.patch
cargo build --profile fast -p horizon-client
cargo test -p horizon-client-render pack_atlas pack_post
```

The patch targets the 2026-11-03 `main` checkout and has not been compiled against other
revisions. If a hunk does not apply, the change is small and local (six renderer files plus
two one-line changes in the client).

## Verifying

1. Load Photon with a labPBR resource pack.
2. Enable Materials → Normal Mapping / Specular Mapping (both on by default).
3. Surface detail and roughness variation appear on blocks; POM starts to work.

Note: `mc_Entity` (per-block ids) is still only supplied on the flat-draw path, so packs'
*hardcoded* materials remain inactive on DX12/Vulkan. That is a separate issue (per-vertex
block ids) which this patch does not touch.
