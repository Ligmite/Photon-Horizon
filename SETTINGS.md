# Settings reference

Every option in `shaders/settings.glsl`, as Horizon shows it in **Shader
Options...**. Switch options are on/off toggles; value options are sliders (or
cycle buttons) with the values listed. The Low/Medium/High/Ultra profiles set
groups of them at once (`shaders.properties`, `profile.*`).

## World

| Option | Default | Values |
|---|---|---|
| `WAVING_PLANTS` | On | on/off |
| `WAVING_LEAVES` | On | on/off |
| `EDGE_HIGHLIGHT` | Off | on/off |
| `EDGE_HIGHLIGHT_SCALE` | 16.0 | 4.0 8.0 16.0 32.0 64.0 128.0 |
| `SLANTED_RAIN` | On | on/off |
| `RAIN_OPACITY` | 0.25 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `SNOW_OPACITY` | 0.75 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `MOON_PHASE_AFFECTS_BRIGHTNESS` | On | on/off |
| `DESERT_SANDSTORM` | On | on/off |
| `SEA_LEVEL` | 63.0 | -60.0 4.0 63.0 |
| `END_GLOW` | On | on/off |
| `RANDOM_WEATHER_VARIATION` | On | on/off |
| `BIOME_WEATHER_VARIATION` | On | on/off |
| `WEATHER_TEMPERATURE_BIAS` | 0.00 | -1.00 -0.99 -0.98 -0.97 -0.96 -0.95 ... 1.00 (201 values) |
| `WEATHER_HUMIDITY_BIAS` | 0.00 | -1.00 -0.99 -0.98 -0.97 -0.96 -0.95 ... 1.00 (201 values) |
| `WEATHER_WIND_BIAS` | 0.00 | -1.00 -0.99 -0.98 -0.97 -0.96 -0.95 ... 1.00 (201 values) |
| `WEATHER_TEMPERATURE_VARIATION_SPEED` | 1.0 | 0.1 0.2 0.3 0.4 0.5 0.6 ... 5.0 (50 values) |
| `WEATHER_HUMIDITY_VARIATION_SPEED` | 1.0 | 0.1 0.2 0.3 0.4 0.5 0.6 ... 5.0 (50 values) |
| `WEATHER_WIND_VARIATION_SPEED` | 1.0 | 0.1 0.2 0.3 0.4 0.5 0.6 ... 5.0 (50 values) |

## Lighting

| Option | Default | Values |
|---|---|---|
| `HANDHELD_LIGHTING` | On | on/off |
| `HANDHELD_LIGHTING_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `CLOUD_SHADOWS` | On | on/off |
| `CLOUD_SHADOWS_INTENSITY` | 0.80 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `VANILLA_AO` | On | on/off |
| `VANILLA_AO_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.50 (151 values) |
| `AO_IN_SUNLIGHT` | On | on/off |
| `SH_SKYLIGHT` | Off | on/off |
| `SSS_SHEEN` | On | on/off |
| `SSS_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `SHADING_STRENGTH` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `LIGHTNING_FLASH` | On | on/off |
| `SUN_NR` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `SUN_NG` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `SUN_NB` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `SUN_MR` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `SUN_MG` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `SUN_MB` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `SUN_ER` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `SUN_EG` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `SUN_EB` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `SUN_I` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `MOON_R` | 0.75 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `MOON_G` | 0.83 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `MOON_B` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `MOON_I` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `BLOCKLIGHT_R` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `BLOCKLIGHT_G` | 0.75 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `BLOCKLIGHT_B` | 0.63 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `BLOCKLIGHT_I` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `SKYLIGHT_I` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `BOUNCED_LIGHT_I` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `CAVE_LIGHTING_I` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `NETHER_USE_BIOME_COLOR` | On | on/off |
| `NETHER_R` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `NETHER_G` | 0.25 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `NETHER_B` | 0.05 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `NETHER_I` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `NETHER_S` | 0.75 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `END_LIGHT_R` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `END_LIGHT_G` | 0.50 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `END_LIGHT_B` | 0.25 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `END_LIGHT_I` | 0.50 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `END_AMBIENT_R` | 0.75 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `END_AMBIENT_G` | 0.33 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `END_AMBIENT_B` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `END_AMBIENT_I` | 0.75 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `SHADOW` | On | on/off |
| `SHADOW_SSRT` | On | on/off |
| `SHADOW_SSRT_STEPS` | 10 | 4 5 6 7 8 9 ... 24 (21 values) |
| `SHADOW_PCF` | On | on/off |
| `SHADOW_COLOR` | On | on/off |
| `SHADOW_VPS` | On | on/off |
| `SHADOW_PENUMBRA_SCALE` | 1.0 | 0.0 0.1 0.2 0.3 0.4 0.5 ... 2.0 (21 values) |
| `ENTITY_SHADOWS` | On | on/off |
| `BLOCK_ENTITY_SHADOWS` | Off | on/off |
| `PIXELATED_SHADOWS` | Off | on/off |
| `PIXELATED_SHADOWS_RESOLUTION` | 16 | 4 8 16 32 64 128 |
| `SSS_STEPS` | 12 | 4 5 6 7 8 9 ... 24 (21 values) |
| `SHADOW_PCF_STEPS_MIN` | 6 | 4 6 8 12 16 18 ... 32 (13 values) |
| `SHADOW_PCF_STEPS_MAX` | 12 | 4 6 8 12 16 18 ... 32 (13 values) |
| `SHADOW_PCF_STEPS_SCALE` | 1.0 | 0.0 0.2 0.4 0.6 0.8 1.0 ... 2.0 (11 values) |
| `SHADOW_BLOCKER_SEARCH_RADIUS` | 0.5 | 0.1 0.2 0.3 0.4 0.5 0.6 ... 1.0 (10 values) |
| `SHADER_AO` | SHADER_AO_GTAO | SHADER_AO_NONE SHADER_AO_SSAO SHADER_AO_GTAO |
| `SSAO_STEPS` | 12 | 1 2 3 4 5 6 ... 64 (64 values) |
| `SSAO_RADIUS` | 2.0 | 0.1 0.2 0.3 0.4 0.5 0.6 ... 8.0 (81 values) |
| `GTAO_SLICES` | 2 | 1 2 3 4 5 6 ... 64 (64 values) |
| `GTAO_HORIZON_STEPS` | 3 | 1 2 3 4 5 6 ... 64 (64 values) |
| `GTAO_RADIUS` | 2.0 | 0.1 0.2 0.3 0.4 0.5 0.6 ... 8.0 (81 values) |
| `VANILLA_AO` | On | on/off |

## Sky

| Option | Default | Values |
|---|---|---|
| `SKY_GROUND` | Off | on/off |
| `ATMOSPHERE_SATURATION_BOOST` | On | on/off |
| `ATMOSPHERE_SATURATION_BOOST_INTENSITY` | 1.00 | -1.00 -0.99 -0.98 -0.97 -0.96 -0.95 ... 1.00 (201 values) |
| `CREPUSCULAR_RAYS` | On | on/off |
| `CREPUSCULAR_RAYS_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `CREPUSCULAR_RAYS_STEPS_HORIZON` | 20 | 1 2 3 4 5 6 ... 64 (64 values) |
| `CREPUSCULAR_RAYS_STEPS_ZENITH` | 4 | 1 2 3 4 5 6 ... 64 (64 values) |
| `RAINBOWS` | On | on/off |
| `END_SUN_EFFECT` | On | on/off |
| `ATMOSPHERE_RAIN_DESATURATION` | Off | on/off |
| `ATMOSPHERE_RAIN_DESATURATION_INTENSITY` | 1.00 | -1.00 -0.99 -0.98 -0.97 -0.96 -0.95 ... 1.00 (201 values) |
| `AURORA_NORMAL` | AURORA_NEVER | AURORA_NEVER AURORA_RARELY AURORA_ALWAYS |
| `AURORA_SNOW` | AURORA_RARELY | AURORA_NEVER AURORA_RARELY AURORA_ALWAYS |
| `AURORA_BRIGHTNESS` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `AURORA_FREQUENCY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `AURORA_CLOUD_LIGHTING` | 0.40 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AURORA_GROUND_LIGHTING` | 0.10 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `CLOUDS_TEMPORAL_UPSCALING` | 4 | 1 2 3 4 |
| `CLOUDS_AERIAL_PERSPECTIVE_BOOST` | 1 | 0 1 2 3 4 |
| `CLOUDS_SCALE` | 10.0 | 1.0 2.0 3.0 4.0 5.0 6.0 ... 15.0 (15 values) |
| `CLOUDS_CUMULUS` | On | on/off |
| `CLOUDS_CUMULUS_PRIMARY_STEPS_H` | 40 | 1 2 3 4 5 6 ... 80 (80 values) |
| `CLOUDS_CUMULUS_PRIMARY_STEPS_Z` | 20 | 1 2 3 4 5 6 ... 80 (80 values) |
| `CLOUDS_CUMULUS_LIGHTING_STEPS` | 6 | 1 2 3 4 5 6 ... 12 (12 values) |
| `CLOUDS_CUMULUS_AMBIENT_STEPS` | 2 | 1 2 3 4 |
| `CLOUDS_CUMULUS_ALTITUDE` | 1200.0 | 400.0 500.0 600.0 700.0 800.0 900.0 ... 10000.0 (97 values) |
| `CLOUDS_CUMULUS_THICKNESS` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CUMULUS_DENSITY` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CUMULUS_COVERAGE` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CUMULUS_SIZE` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CUMULUS_DETAIL_STRENGTH` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CUMULUS_WIND_SPEED` | 25.0 | 0.0 1.0 2.0 3.0 4.0 5.0 ... 100.0 (101 values) |
| `CLOUDS_CUMULUS_WIND_ANGLE` | 30.0 | 0.0 10.0 20.0 30.0 40.0 50.0 ... 350.0 (36 values) |
| `CLOUDS_CUMULUS_PRECOMPUTE_LOCAL_COVERAGE` | On | on/off |
| `CLOUDS_CUMULUS_CONGESTUS` | On | on/off |
| `CLOUDS_CUMULUS_CONGESTUS_PRIMARY_STEPS` | 20 | 1 2 3 4 5 6 ... 80 (80 values) |
| `CLOUDS_CUMULUS_CONGESTUS_LIGHTING_STEPS` | 6 | 1 2 3 4 5 6 ... 12 (12 values) |
| `CLOUDS_CUMULUS_CONGESTUS_AMBIENT_STEPS` | 2 | 1 2 3 4 |
| `CLOUDS_CUMULUS_CONGESTUS_ALTITUDE` | 400.0 | 400.0 500.0 600.0 700.0 800.0 900.0 ... 10000.0 (97 values) |
| `CLOUDS_CUMULUS_CONGESTUS_THICKNESS` | 32.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CUMULUS_CONGESTUS_DENSITY` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CUMULUS_CONGESTUS_COVERAGE` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CUMULUS_CONGESTUS_SIZE` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CUMULUS_CONGESTUS_DETAIL_STRENGTH` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CUMULUS_CONGESTUS_WIND_SPEED` | 20.0 | 0.0 1.0 2.0 3.0 4.0 5.0 ... 100.0 (101 values) |
| `CLOUDS_CUMULUS_CONGESTUS_WIND_ANGLE` | 30.0 | 0.0 10.0 20.0 30.0 40.0 50.0 ... 350.0 (36 values) |
| `CLOUDS_ALTOCUMULUS` | On | on/off |
| `CLOUDS_ALTOCUMULUS_PRIMARY_STEPS_H` | 12 | 1 2 3 4 5 6 ... 80 (80 values) |
| `CLOUDS_ALTOCUMULUS_PRIMARY_STEPS_Z` | 6 | 1 2 3 4 5 6 ... 80 (80 values) |
| `CLOUDS_ALTOCUMULUS_LIGHTING_STEPS` | 4 | 1 2 3 4 5 6 |
| `CLOUDS_ALTOCUMULUS_AMBIENT_STEPS` | 2 | 1 2 3 4 |
| `CLOUDS_ALTOCUMULUS_ALTITUDE` | 3200.0 | 400.0 500.0 600.0 700.0 800.0 900.0 ... 10000.0 (97 values) |
| `CLOUDS_ALTOCUMULUS_THICKNESS` | 0.15 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_ALTOCUMULUS_DENSITY` | 0.10 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_ALTOCUMULUS_COVERAGE` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_ALTOCUMULUS_SIZE` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_ALTOCUMULUS_DETAIL_STRENGTH` | 1.50 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_ALTOCUMULUS_WIND_SPEED` | 25.0 | 0.0 1.0 2.0 3.0 4.0 5.0 ... 100.0 (101 values) |
| `CLOUDS_ALTOCUMULUS_WIND_ANGLE` | 60.0 | 0.0 10.0 20.0 30.0 40.0 50.0 ... 350.0 (36 values) |
| `CLOUDS_CIRRUS` | On | on/off |
| `CLOUDS_CIRRUS_LIGHTING_STEPS` | 6 | 1 2 3 4 5 6 ... 12 (12 values) |
| `CLOUDS_CIRRUS_ALTITUDE` | 6000.0 | 400.0 500.0 600.0 700.0 800.0 900.0 ... 10000.0 (97 values) |
| `CLOUDS_CIRRUS_DENSITY` | 0.50 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CIRRUS_COVERAGE` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CIRRUS_SIZE` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CIRRUS_WIND_SPEED` | 40.0 | 0.0 1.0 2.0 3.0 4.0 5.0 ... 100.0 (101 values) |
| `CLOUDS_CIRRUS_WIND_ANGLE` | 90.0 | 0.0 10.0 20.0 30.0 40.0 50.0 ... 350.0 (36 values) |
| `CLOUDS_CIRRUS_DETAIL_STRENGTH` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CIRRUS_CURL_STRENGTH` | 0.80 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CIRROCUMULUS_DENSITY` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CIRROCUMULUS_COVERAGE` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CIRROCUMULUS_SIZE` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CIRROCUMULUS_DETAIL_STRENGTH` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_CIRROCUMULUS_CURL_STRENGTH` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_NOCTILUCENT` | On | on/off |
| `CLOUDS_NOCTILUCENT_INTENSITY` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 2.00 (200 values) |
| `CLOUDS_NOCTILUCENT_RARITY` | 0.70 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 1.00 (100 values) |
| `BLOCKY_CLOUDS` | Off | on/off |
| `BLOCKY_CLOUDS_LAYER_2` | Off | on/off |
| `BLOCKY_CLOUDS_THICKNESS` | 13.0 | 0.01 0.1 0.2 0.3 0.4 0.5 ... 32.0 (69 values) |
| `BLOCKY_CLOUDS_ALTITUDE` | 192.0 | 64.0 65.0 66.0 67.0 68.0 69.0 ... 320.0 (257 values) |
| `BLOCKY_CLOUDS_ALTITUDE_2` | 280.0 | 64.0 65.0 66.0 67.0 68.0 69.0 ... 320.0 (257 values) |
| `BLOCKY_CLOUDS_ROUNDNESS` | 0.28 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 1.00 (100 values) |
| `BLOCKY_CLOUDS_SHARPNESS` | 0.20 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `BLOCKY_CLOUDS_SIZE` | 1.00 | 0.10 0.11 0.12 0.13 0.14 0.15 ... 2.50 (241 values) |
| `BLOCKY_CLOUDS_BRIGHTNESS` | 1.00 | 0.00 0.02 0.04 0.06 0.08 0.10 ... 4.00 (201 values) |
| `BLOCKY_CLOUDS_BOTTOMLIGHT` | 0.00 | 0.00 0.0025 0.005 0.0075 0.01 0.0125 ... 0.5 (201 values) |
| `BLOCKY_CLOUDS_DENSITY` | 1.00 | 0.01 0.02 0.03 0.04 0.05 0.06 ... 5.00 (275 values) |
| `BLOCKY_CLOUDS_ATMOSPHERIC_SCATTERING` | On | on/off |
| `BLOCKY_CLOUDS_PRIMARY_STEPS` | 12 | 1 2 3 4 5 6 ... 64 (64 values) |
| `BLOCKY_CLOUDS_LIGHTING_STEPS` | 4 | 1 2 3 4 5 6 |
| `BLOCKY_CLOUDS_WIND_SPEED` | 0.33 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 10.00 (281 values) |
| `BLOCKY_CLOUDS_WIND_ANGLE` | 0.0 | 0.0 10.0 20.0 30.0 40.0 50.0 ... 350.0 (36 values) |
| `SUN_ANGULAR_RADIUS` | 2.0 | 0.1 0.2 0.3 0.4 0.5 0.6 ... 10.0 (100 values) |
| `MOON_ANGULAR_RADIUS` | 3.0 | 0.1 0.2 0.3 0.4 0.5 0.6 ... 3.0 (30 values) |
| `VANILLA_SUN` | Off | on/off |
| `VANILLA_MOON` | Off | on/off |
| `STARS` | On | on/off |
| `STARS_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `STARS_COVERAGE` | 0.50 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `GALAXY` | Off | on/off |
| `GALAXY_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |

## Fog

| Option | Default | Values |
|---|---|---|
| `VL` | On | on/off |
| `OVERWORLD_FOG_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `NETHER_FOG_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `BORDER_FOG` | On | on/off |
| `CAVE_FOG` | On | on/off |
| `BLOOMY_FOG` | Off | on/off |
| `BLOOMY_FOG_INTENSITY` | 1.0 | 0.0 0.1 0.2 0.3 0.4 0.5 ... 2.0 (21 values) |
| `BORDER_FOG_HIDE_SUNSET_GRADIENT` | On | on/off |
| `BLOOMY_RAIN` | On | on/off |
| `LOD_DISTANCE` | 0 | 0 8 12 16 24 32 ... 1024 (16 values) |
| `VL_RENDER_SCALE` | 0.50 | 0.50 0.51 0.52 0.53 0.54 0.55 ... 1.00 (51 values) |
| `AIR_FOG_CLOUDY_NOISE` | On | on/off |
| `AIR_FOG_COLORED_LIGHT_SHAFTS` | Off | on/off |
| `AIR_FOG_RAYLEIGH_FALLOFF_START` | 30.0 | 0.0 1.0 2.0 3.0 4.0 5.0 ... 128.0 (129 values) |
| `AIR_FOG_RAYLEIGH_FALLOFF_HALF_LIFE` | 30.0 | 0.0 1.0 2.0 3.0 4.0 5.0 ... 128.0 (129 values) |
| `AIR_FOG_MIE_FALLOFF_START` | 7.0 | 0.0 1.0 2.0 3.0 4.0 5.0 ... 128.0 (129 values) |
| `AIR_FOG_MIE_FALLOFF_HALF_LIFE` | 7.0 | 0.0 1.0 2.0 3.0 4.0 5.0 ... 128.0 (129 values) |
| `AIR_FOG_RAYLEIGH_DENSITY` | 0.0005 | 0.0001 0.0002 0.0003 0.0004 0.0005 0.0006 ... 0.0100 (100 values) |
| `AIR_FOG_RAYLEIGH_R` | 0.31 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_G` | 0.67 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_B` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_DENSITY_RAIN` | 0.0005 | 0.0001 0.0002 0.0003 0.0004 0.0005 0.0006 ... 0.0100 (100 values) |
| `AIR_FOG_RAYLEIGH_R_RAIN` | 0.31 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_G_RAIN` | 0.67 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_B_RAIN` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_DENSITY_ARID` | 0.0003 | 0.0001 0.0002 0.0003 0.0004 0.0005 0.0006 ... 0.0100 (100 values) |
| `AIR_FOG_RAYLEIGH_R_ARID` | 0.65 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_G_ARID` | 0.80 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_B_ARID` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_DENSITY_SNOWY` | 0.0010 | 0.0001 0.0002 0.0003 0.0004 0.0005 0.0006 ... 0.0100 (100 values) |
| `AIR_FOG_RAYLEIGH_R_SNOWY` | 0.50 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_G_SNOWY` | 0.81 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_B_SNOWY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_DENSITY_TAIGA` | 0.0006 | 0.0001 0.0002 0.0003 0.0004 0.0005 0.0006 ... 0.0100 (100 values) |
| `AIR_FOG_RAYLEIGH_R_TAIGA` | 0.31 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_G_TAIGA` | 0.85 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_B_TAIGA` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_DENSITY_JUNGLE` | 0.0013 | 0.0001 0.0002 0.0003 0.0004 0.0005 0.0006 ... 0.0100 (100 values) |
| `AIR_FOG_RAYLEIGH_R_JUNGLE` | 0.40 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_G_JUNGLE` | 0.95 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_B_JUNGLE` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_DENSITY_SWAMP` | 0.0014 | 0.0001 0.0002 0.0003 0.0004 0.0005 0.0006 ... 0.0100 (100 values) |
| `AIR_FOG_RAYLEIGH_R_SWAMP` | 0.67 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_G_SWAMP` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_RAYLEIGH_B_SWAMP` | 0.94 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `AIR_FOG_MIE_DENSITY_MORNING` | 0.0070 | 0.0001 0.0002 0.0003 0.0004 0.0005 0.0006 ... 0.0100 (100 values) |
| `AIR_FOG_MIE_DENSITY_NOON` | 0.0001 | 0.0001 0.0002 0.0003 0.0004 0.0005 0.0006 ... 0.0100 (100 values) |
| `AIR_FOG_MIE_DENSITY_EVENING` | 0.0050 | 0.0001 0.0002 0.0003 0.0004 0.0005 0.0006 ... 0.0100 (100 values) |
| `AIR_FOG_MIE_DENSITY_MIDNIGHT` | 0.0050 | 0.0001 0.0002 0.0003 0.0004 0.0005 0.0006 ... 0.0100 (100 values) |
| `AIR_FOG_MIE_DENSITY_RAIN` | 0.030 | 0.001 0.002 0.003 0.004 0.005 0.006 ... 0.100 (100 values) |
| `AIR_FOG_MIE_DENSITY_SNOW` | 0.015 | 0.001 0.002 0.003 0.004 0.005 0.006 ... 0.100 (100 values) |
| `AIR_FOG_MIE_DENSITY_BLUE_HOUR` | 0.0020 | 0.0001 0.0002 0.0003 0.0004 0.0005 0.0006 ... 0.0100 (100 values) |
| `NETHER_FOG_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |

## Materials

| Option | Default | Values |
|---|---|---|
| `NORMAL_MAPPING` | Off | on/off |
| `SPECULAR_MAPPING` | Off | on/off |
| `POM` | Off | on/off |
| `HARDCODED_SPECULAR` | On | on/off |
| `HARDCODED_EMISSION` | On | on/off |
| `HARDCODED_SSS` | On | on/off |
| `RAIN_PUDDLES` | On | on/off |
| `TEXTURE_FORMAT` | TEXTURE_FORMAT_LAB | TEXTURE_FORMAT_LAB TEXTURE_FORMAT_OLD |
| `EMISSION_STRENGTH` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `DIRECTIONAL_LIGHTMAPS` | Off | on/off |
| `DIRECTIONAL_LIGHTMAPS_INTENSITY` | 0.20 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `POM_SAMPLES` | 40 | 1 2 3 4 5 6 ... 128 (128 values) |
| `POM_DEPTH` | 0.25 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `POM_SHADOW` | Off | on/off |
| `POM_SHADOW_SAMPLES` | 40 | 1 2 3 4 5 6 ... 128 (128 values) |
| `POM_SLOPE_NORMALS` | Off | on/off |
| `POM_DISTANCE` | 32 | 1 2 3 4 5 6 ... 32 (32 values) |
| `REFRACTION` | REFRACTION_ALL | REFRACTION_OFF REFRACTION_ALL REFRACTION_WATER_ONLY |
| `REFRACTION_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `ENVIRONMENT_REFLECTIONS` | On | on/off |
| `SKY_REFLECTIONS` | On | on/off |
| `SSR_ROUGHNESS_SUPPORT` | On | on/off |
| `SSR_RAY_COUNT` | 4 | 1 2 3 4 5 6 |
| `SSR_INTERSECTION_STEPS_SMOOTH` | 16 | 4 5 6 7 8 9 ... 32 (29 values) |
| `SSR_INTERSECTION_STEPS_ROUGH` | 8 | 4 5 6 7 8 9 ... 32 (29 values) |
| `SSR_REFINEMENT_STEPS` | 4 | 0 1 2 3 4 5 ... 8 (9 values) |
| `SSR_ROUGHNESS_THRESHOLD` | 2.0 | 0.0 0.1 0.2 0.3 0.4 0.5 ... 4.0 (41 values) |

## Water

| Option | Default | Values |
|---|---|---|
| `WATER_PARALLAX` | On | on/off |
| `WATER_DISPLACEMENT` | On | on/off |
| `WATER_CAUSTICS` | Off | on/off |
| `WATER_CAUSTICS_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `WATER_EDGE_HIGHLIGHT` | On | on/off |
| `WATER_EDGE_HIGHLIGHT_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `WATER_TEXTURE` | WATER_TEXTURE_HIGHLIGHT_UNDERGROUND | WATER_TEXTURE_OFF WATER_TEXTURE_HIGHLIGHT WATER_TEXTURE_VANILLA WATER_TEXTURE_HIGHLIGHT_UNDERGROUND |
| `SNELLS_WINDOW` | Off | on/off |
| `BIOME_WATER_COLOR` | On | on/off |
| `WATER_WAVES` | On | on/off |
| `WATER_WAVE_ITERATIONS` | 3 | 1 2 3 4 5 6 |
| `WATER_WAVE_STRENGTH` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `WATER_WAVE_FREQUENCY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `WATER_WAVE_SPEED_STILL` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `WATER_WAVE_SPEED_FLOWING` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `WATER_WAVE_PERSISTENCE` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `WATER_WAVE_LACUNARITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `WATER_WAVES_HEIGHT_VARIATION` | On | on/off |
| `WATER_ABSORPTION_R` | 0.39 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `WATER_ABSORPTION_G` | 0.14 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `WATER_ABSORPTION_B` | 0.07 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `WATER_SCATTERING` | 0.01 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `WATER_ABSORPTION_R_UNDERWATER` | 0.20 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `WATER_ABSORPTION_G_UNDERWATER` | 0.08 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `WATER_ABSORPTION_B_UNDERWATER` | 0.04 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `WATER_SCATTERING_UNDERWATER` | 0.03 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |

## Post-Processing

| Option | Default | Values |
|---|---|---|
| `BLOOM` | On | on/off |
| `BLOOM_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `BLOOM_SPREAD` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `BLOOM_UPSAMPLING_FILTER` | texture | texture bicubic_filter |
| `DOF` | Off | on/off |
| `DOF_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `DOF_SAMPLES` | 40 | 1 2 3 4 5 6 ... 80 (80 values) |
| `DOF_FOCUS` | -1.0 | 0.0 1.0 2.0 3.0 4.0 5.0 ... 50.0 (51 values) |
| `MOTION_BLUR` | Off | on/off |
| `MOTION_BLUR_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `TAA` | On | on/off |
| `FXAA` | On | on/off |
| `TAAU` | Off | on/off |
| `TAAU_RENDER_SCALE` | 0.75 | 0.50 0.51 0.52 0.53 0.54 0.55 ... 1.00 (51 values) |
| `CAS` | On | on/off |
| `CAS_INTENSITY` | 0.50 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `VIGNETTE` | On | on/off |
| `VIGNETTE_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `tonemap` | tonemap_lottes | tonemap_aces_fit tonemap_aces_full tonemap_lottes tonemap_hejl_2015 tonemap_hejl_burgess tonemap_tech ... tonemap_reinhard_jodie (10 values) |
| `GRADE_BRIGHTNESS` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `GRADE_CONTRAST` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `GRADE_SATURATION` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `GRADE_WHITE_BALANCE` | 6500 | 4000 4100 4200 4300 4400 4500 ... 9000 (51 values) |
| `GRADE_ORANGE_SAT_BOOST` | 0.00 | -0.50 -0.49 -0.48 -0.47 -0.46 -0.45 ... 0.50 (101 values) |
| `GRADE_TEAL_SAT_BOOST` | 0.10 | -0.50 -0.49 -0.48 -0.47 -0.46 -0.45 ... 0.50 (101 values) |
| `GRADE_GREEN_SAT_BOOST` | 0.00 | -0.50 -0.49 -0.48 -0.47 -0.46 -0.45 ... 0.50 (101 values) |
| `GRADE_GREEN_HUE_SHIFT` | 0.0 | -8.0 -7.0 -6.0 -5.0 -4.0 -3.0 ... 8.0 (17 values) |
| `PURKINJE_SHIFT` | On | on/off |
| `PURKINJE_SHIFT_INTENSITY` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `AUTO_EXPOSURE` | AUTO_EXPOSURE_OFF | AUTO_EXPOSURE_OFF AUTO_EXPOSURE_SIMPLE AUTO_EXPOSURE_HISTOGRAM |
| `AUTO_EXPOSURE_BIAS` | 0.0 | -2.0 -1.9 -1.8 -1.7 -1.6 -1.5 ... 2.0 (41 values) |
| `AUTO_EXPOSURE_MIN` | -1.0 | -2.0 -1.9 -1.8 -1.7 -1.6 -1.5 ... 2.0 (41 values) |
| `AUTO_EXPOSURE_MAX` | 0.0 | -2.0 -1.9 -1.8 -1.7 -1.6 -1.5 ... 2.0 (41 values) |
| `AUTO_EXPOSURE_RATE_DIM_TO_BRIGHT` | 2.0 | 0.5 1.0 1.5 2.0 2.5 3.0 ... 6.0 (12 values) |
| `AUTO_EXPOSURE_RATE_BRIGHT_TO_DIM` | 1.0 | 0.5 1.0 1.5 2.0 2.5 3.0 ... 6.0 (12 values) |
| `MANUAL_EXPOSURE_VALUE` | 0.0 | -6.0 -5.0 -4.0 -3.0 -2.0 -1.0 ... 17.0 (24 values) |
| `MANUAL_EXPOSURE_USE_SCREEN_BRIGHTNESS` | Off | on/off |
| `HISTOGRAM_BINS` | 32 | 32 64 128 |
| `HISTOGRAM_TARGET` | 0.5 | 0.0 0.1 0.2 0.3 0.4 0.5 ... 0.9 (10 values) |

## Miscellaneous

| Option | Default | Values |
|---|---|---|
| `INFO` | 2 | 0 1 2 3 |
| `DEBUG_VIEW` | DEBUG_VIEW_NONE | DEBUG_VIEW_NONE DEBUG_VIEW_SAMPLER DEBUG_VIEW_HISTOGRAM DEBUG_VIEW_WEATHER |
| `DEBUG_SAMPLER` | colortex1 | colortex1 colortex2 colortex3 colortex4 colortex5 colortex6 ... shadowcolor1 (22 values) |
| `WHITE_WORLD` | Off | on/off |
| `TONEMAP_COMPARISON` | Off | on/off |
| `tonemap_left` | tonemap_lottes | tonemap_aces_fit tonemap_aces_full tonemap_lottes tonemap_hejl_burgess tonemap_tech tonemap_uncharted_2 ... tonemap_reinhard_jodie (9 values) |
| `tonemap_right` | tonemap_lottes | tonemap_aces_fit tonemap_aces_full tonemap_lottes tonemap_hejl_burgess tonemap_tech tonemap_uncharted_2 ... tonemap_reinhard_jodie (9 values) |
| `FANCY_NETHER_PORTAL` | On | on/off |
| `CUSTOM_SKY` | Off | on/off |
| `CUSTOM_SKY_BRIGHTNESS` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `ENCHANTMENT_GLINT_BRIGHTNESS` | 1.00 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 2.00 (201 values) |
| `DITHERED_TRANSLUCENCY_FALLBACK` | Off | on/off |
| `USE_HALF_PRECISION_FP` | On | on/off |
| `DISTANCE_VIEW` | Off | on/off |
| `DISTANCE_VIEW_METHOD` | DISTANCE_VIEW_DISTANCE | DISTANCE_VIEW_DISTANCE DISTANCE_VIEW_DEPTH |
| `DISTANCE_VIEW_MAX_DISTANCE` | 16.0 | 1.0 2.0 4.0 8.0 16.0 32.0 ... 2048.0 (12 values) |
| `BOX_MODE` | BOX_MODE_NONE | BOX_MODE_NONE BOX_MODE_COLOR BOX_MODE_RAINBOW |
| `BOX_COLOR_R` | 1.0 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `BOX_COLOR_G` | 1.0 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `BOX_COLOR_B` | 1.0 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `BOX_EMISSION` | 1.0 | 0.00 0.01 0.02 0.03 0.04 0.05 ... 1.00 (101 values) |
| `BOX_LINE_WIDTH` | 2 | 0 1 2 3 4 5 |

## Horizon HDR

| Option | Default | Values |
|---|---|---|
| `HDR_OUTPUT` | 0 | 0 1 |
| `HDR_PAPER_WHITE` | 203.0 | 80.0 100.0 120.0 160.0 203.0 250.0 ... 500.0 (9 values) |
| `HDR_PEAK_BRIGHTNESS` | 1000.0 | 400.0 600.0 800.0 1000.0 1200.0 1500.0 |
| `HDR_UI_BRIGHTNESS` | 203.0 | 80.0 100.0 120.0 160.0 203.0 250.0 ... 500.0 (9 values) |
| `hdr_tonemap` | tonemap_lottes_photon_hdr | tonemap_lottes_photon_hdr tonemap_uncharted_2 tonemap_reinhard tonemap_aces_full tonemap_none |
| `HDR_USE_FP16` | On | on/off |
| `USE_SEPARATE_ENTITY_DRAWS` | On | on/off |
