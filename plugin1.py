# ------------------------------------------------------------
# menu.py
# Version 1.0.2
# Last Updated: 9/26/2022
# ------------------------------------------------------------

# ------------------------------------------------------------
# GLOBAL IMPORTS :::::::::::::::::::::::::::::::::::::::::::::
# ------------------------------------------------------------

import nuke
import platform
import nukescripts

# Define where .nuke directory is on each OS's network.
# Normal user nuke dir      Win_Dir = '\Users\jkirk\.nuke'
Win_Dir = 'Q:\.nuke'
MacOSX_Dir = ''
Linux_Dir = '/home/jkirk/.nuke'

#set global directory
if platform.system() == "Windows":
    dir = Win_Dir
elif platform.system() == "Darwin":
    dir = MacOSX_Dir
elif platform.system() == "Linux":
    dir = Linux_Dir
else:
    dir = None
    
# ------------------------------------------------------------
# CUSTOM PATHS :::::::::::::::::::::::::::::::::::::::::::::::
# ------------------------------------------------------------
nuke.pluginAddPath('./icons')


# ------------------------------------------------------------
# KNOB DEFAULTS ::::::::::::::::::::::::::::::::::::::::::::::
# ------------------------------------------------------------

nuke.knobDefault('Tracker4.label', 'Motion: [value transform]\nRef Frame: [value reference_frame]')
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()),nodeClass = 'Tracker4')
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()),nodeClass = 'FrameHold')

# ------------------------------------------------------------
# MOTION BLUR SHUTTER CENTERED :::::::::::::::::::::::::::::::
# ------------------------------------------------------------

nuke.knobDefault('Tracker4.shutteroffset','centered')
nuke.knobDefault('TimeBlur.shutteroffset','centered')
nuke.knobDefault('Transform.shutteroffset','centered')
nuke.knobDefault('TransformMasked.shutteroffset','centered')
nuke.knobDefault('CornerPin2D.shutteroffset','centered')
nuke.knobDefault('MotionBlur2D.shutteroffset','centered')
nuke.knobDefault('MotionBlur3D.shutteroffset','centered')
nuke.knobDefault('ScanlineRender.shutteroffset','centered')
nuke.knobDefault('Card3D.shutteroffset','centered')



# ------------------------------------------------------------
# CUSTOM MENUS :::::::::::::::::::::::::::::::::::::::::::::::
# ------------------------------------------------------------

utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')
utilitiesMenu.addCommand('Autocrop','nukescripts.autocrop()')

myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon= 'ArthurFist24px.png')
myGizmosMenu.addCommand('Autocrop','nukescripts.autocrop()')

# ------------------------------------------------------------
# KEYBOARD SHORTCUTS :::::::::::::::::::::::::::::::::::::::::
# ------------------------------------------------------------

nuke.menu('Nodes').addCommand('Transform/Tracker', 'nuke.createNode("Tracker4"', 'ctr;+alt+t', icon="Tracker.png", shortcutContext=2)
