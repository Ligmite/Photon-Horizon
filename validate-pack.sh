#!/bin/sh
# Runs Horizon's own shader-pack loader over the Photon port, with no GPU.
#
#   ./validate-pack.sh /path/to/horizon
#
# Points HORIZON_TEST_SHADER_PACKS at this folder (which holds shaders/) and runs
# horizon-shaders' `real_packs_read` ignored test: it preprocesses every stage
# file, translates every composite-style program, and loads each dimension's
# post-processing set (gbuffers, shadow, compute) as the game does.
set -eu

HORIZON="${1:?usage: $0 /path/to/horizon}"
PACK="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"

[ -f "$HORIZON/Cargo.toml" ] || { echo "no Cargo.toml in $HORIZON" >&2; exit 1; }
[ -d "$PACK/shaders" ] || { echo "no shaders folder in $PACK" >&2; exit 1; }

export HORIZON_TEST_SHADER_PACKS="$PACK"
export SHOW_ERRORS="${SHOW_ERRORS:-1}"
echo "Reading pack at $HORIZON_TEST_SHADER_PACKS with Horizon at $HORIZON"

cd "$HORIZON"
cargo test -p horizon-shaders --release -- --ignored --nocapture real_packs_read
