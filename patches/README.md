# Optional Horizon patch

The pack runs without anything in this folder. These files are for getting labPBR
normal/specular maps working in OptiFine-format packs, which Horizon currently binds to 1×1
stand-ins.

- [`HORIZON-PATCH.md`](HORIZON-PATCH.md) — what the patch does, why, how to apply and test.
- `photon-labpbr-pack-atlas.patch` — the unified diff, applied with `git apply` from a
  Horizon checkout.

Requires building Horizon from source (Rust toolchain). If the change lands upstream, this
folder becomes unnecessary.
