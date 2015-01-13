"""
    Plugin for driving custom LCD display
"""

import os
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import math
import string
import time


__plugin__ = "script.plasma.saver"
__author__ = 'bfrigon [bfrigon@gmail.com]'
__url__ = "www.bfrigon.com"
__credits__ = ""
__version__ = "0.1.011"
__settings__ = xbmcaddon.Addon(id='script.plasma.saver')
__cwd__ = __settings__.getAddonInfo('path')


#----------
# SETTINGS
#---------
MAX_OSD_IDLE = 60


       
#================================================================================================================
#
# Plugin class
#
#================================================================================================================
class Plugin():


    #----------------------------------------------------------------------------
    # __init__
    #
    # Arguments : None
    # 
    # Returns: None
    #----------------------------------------------------------------------------
    def __init__(self):
        self.idle_trigger = False



    #----------------------------------------------------------------------------
    # run() : Start service loop
    #
    # Arguments : None
    #
    # Returns: None
    #----------------------------------------------------------------------------
    def run(self):
        while (not xbmc.abortRequested):
            time.sleep(0.5)
            
            dialogid = int(xbmcgui.getCurrentWindowDialogId())
            
            is_fullscreen = xbmc.getCondVisibility('VideoPlayer.IsFullscreen')
            is_playing_tv = xbmc.getCondVisibility('Pvr.IsPlayingTv')
            is_playing_video = xbmc.getCondVisibility('Player.HasVideo')
            osd_visible = (dialogid != 9999)
            
            idle = xbmc.getGlobalIdleTime()
            
            print idle
            
            if idle < MAX_OSD_IDLE or is_fullscreen and not osd_visible:
                continue
                
            if not (is_playing_tv or is_playing_video):
                continue
            
            xbmc.log('Idle warning: {0:d} seconds, going full screen'.format(idle))
            #xbmc.executebuiltin('Action(FullScreen)')
            xbmc.executebuiltin('Action(Close)')
    

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if (__name__ == "__main__"):
    plugin = Plugin()
    plugin.run()

