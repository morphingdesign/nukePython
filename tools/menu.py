# -----------------------------------------------------------
# menu.py
# v.1.1
# Updated: 20201029
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
# CONFIGURE HOTKEYS ((((((((((((((((((((((((((((((((((( START
# -----------------------------------------------------------
nuke.menu('Nodes').addCommand("Other/Backdrop", "nuke.createNode('BackdropNode')", "ctrl+shift+b", shortcutContext=2)

# -----------------------------------------------------------
# CONFIGURE HOTKEYS ))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------


# -----------------------------------------------------------
# CREATE GIZMO TOOLBAR (((((((((((((((((((((((((((((((( START
# -----------------------------------------------------------
# Create Menu
gizmoToolbar = nuke.menu('Nodes')
gizmoMenu = gizmoToolbar.addMenu('Gizmos', icon = 'HansIcon.png')

# Add gizmos to menu list
gizmoMenu.addCommand('Additive Keyer', "nuke.createNode('AdditiveKeyer2')")
gizmoMenu.addCommand('Despill Madness', "nuke.createNode('DespillMadness')")
gizmoMenu.addCommand('TX Bloom', "nuke.createNode('TX_Bloom')")

# -----------------------------------------------------------
# CREATE GIZMO TOOLBAR )))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------