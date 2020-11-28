# -----------------------------------------------------------
# menu.py
# v.1.2
# Updated: 2020127
# -----------------------------------------------------------


# -----------------------------------------------------------
# SET NUKE DIRECTORY (((((((((((((((((((((((((((((((((( START
#
# >>>>> ALERT: REPLACE <USERNAME>. <<<<<
#
# -----------------------------------------------------------
# Note: Omit "\" at end of filepath.
dir  = r'C:\Users\<USERNAME>\.nuke'

# -----------------------------------------------------------
# SET NUKE DIRECTORY )))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# GLOBAL IMPORTS (((((((((((((((((((((((((((((((((((((( START
# -----------------------------------------------------------
import os
import nuke
import nukescripts
# -----------------------------------------------------------
# GLOBAL IMPORTS )))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# CRYPTOMATTE PLUGIN SNIPPET (((((((((((((((((((((((((( START
# Ref plugin docs for more info.
# -----------------------------------------------------------
import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte_ui()
# -----------------------------------------------------------
# CRYPTOMATTE PLUGIN SNIPPET )))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# PIXELFUDGER PLUGIN SNIPPET (((((((((((((((((((((((((( START
# Ref plugin docs for more info.
# -----------------------------------------------------------
import pixelfudger
# -----------------------------------------------------------
# CRYPTOMATTE PLUGIN SNIPPET )))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# CONFIGURE HOTKEYS ((((((((((((((((((((((((((((((((((( START
# -----------------------------------------------------------
nuke.menu('Nodes').addCommand("Other/Backdrop", "nuke.createNode('BackdropNode')", "ctrl+shift+b", shortcutContext=2)

# -----------------------------------------------------------
# CONFIGURE HOTKEYS ))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------


# -----------------------------------------------------------
# CREATE GIZMO TOOLBAR (((((((((((((((((((((((((((((((( START
# -----------------------------------------------------------
# Create Gizmo Menu
gizmoToolbar = nuke.menu('Nodes')
gizmoMenu = gizmoToolbar.addMenu('Gizmos', icon = 'HansIcon.png')

# Filter SubMenu
filterMenu = gizmoMenu.addMenu('Filter', index = 10)
filterMenu.addCommand('Aberration', "nuke.createNode('Aberration')")
# Already accessible via NukeSurvivalToolkit
#filterMenu.addCommand('BM Optical Glow', "nuke.createNode('bm_OpticalGlow')")
filterMenu.addCommand('TX Bloom', "nuke.createNode('TX_Bloom')")

# Keyer SubMenu
keyerMenu = gizmoMenu.addMenu('Keyer', index = 20)
keyerMenu.addCommand('Additive Keyer', "nuke.createNode('AdditiveKeyer2')")
# Already accessible via NukeSurvivalToolkit
# Icon includes as part of Nukepedia download
#keyerMenu.addCommand('aP Matte', "nuke.createNode('aPMatte'), icon = 'aPMatte.png'")
keyerMenu.addCommand('Despill Madness', "nuke.createNode('DespillMadness')")

# Transform SubMenu
transformMenu = gizmoMenu.addMenu('Transform', index = 30)
transformMenu.addCommand('ARRI Lens Distortion', "nuke.createNode('ArriLensDistortion')")

# -----------------------------------------------------------
# CREATE GIZMO TOOLBAR )))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------