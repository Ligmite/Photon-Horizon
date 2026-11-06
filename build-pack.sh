#!/bin/sh
# Builds Photon-Horizon.zip from the pack sources (shaders/ at the zip root).
set -eu
cd "$(dirname "$0")"
rm -f Photon-Horizon.zip
zip -qr Photon-Horizon.zip shaders README.md LICENSE
echo "wrote Photon-Horizon.zip"
