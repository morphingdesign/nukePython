# NUKE_PATH
# NUKE_PATH env var set to target directory where this init.py is located.
nuke.pluginAddPath('./Gizmos/')
nuke.pluginAddPath('./Icons/')
# Nuke Survival Toolkit cloned from GitHub, path identified for source.
nuke.pluginAddPath('./NukeSurvivalToolkit/NukeSurvivalToolkit/')
# Cryptomatte Plugin cloned from GitHub, path identified for source.
nuke.pluginAddPath('./Cryptomatte/nuke')
# PixelFudger Plugin accessed via Nukepedia, path identified for source.
nuke.pluginAddPath('./Gizmos/PixelFudger/')

# Required for Cryptomatte Plugin; Path defined above via NUKE_Path.
# Ref docs for more info about plugin.
# Source: https://github.com/Psyop/Cryptomatte
import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte()