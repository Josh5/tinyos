import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon

__settings__ = xbmcaddon.Addon(id='script.tiny')
__cwd__ = __settings__.getAddonInfo('path')

#Open the add-on settings page, then refresh plugin
__settings__.openSettings()
WINDOW = xbmcgui.getCurrentWindowId()
if WINDOW == 10000:
    printDebug("Currently in home - refreshing to allow new settings to be taken")
    xbmc.executebuiltin("XBMC.ActivateWindow(Home)")

