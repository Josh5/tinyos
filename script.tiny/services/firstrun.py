import xbmcgui
import xbmc
import os
import shutil
import services.lib.extract as extract
from services.lib.service import service
from xbmcaddon import Addon
import subprocess
import time

__addonID__ = "script.tiny"
ADDON     = Addon( __addonID__ )
ADDON_DATA  = xbmc.translatePath( "special://profile/addon_data/%s/" % __addonID__ )
ADDON_DIR = ADDON.getAddonInfo( "path" )
LangXBMC  = xbmc.getLocalizedString
ROOTDIR            = ADDON_DIR
FILES = xbmc.translatePath( ADDON_DIR + "/resources/files/" )
DEST = xbmc.translatePath( "special://home/" )
src=None

def EXECUTE():
        dialog = xbmcgui.Dialog()      
        dp = xbmcgui.DialogProgress()
        dlg = xbmcgui.WindowXMLDialog('welcomeDialog.xml',ROOTDIR)
        dlg.doModal()
	
	#Execute XBMC built-in functions
        xbmc.executebuiltin('UpdateAddonRepos')
        xbmc.executebuiltin('UpdateLocalAddons')

def ensure_dir(f):
    print "Checking for location: "+f
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
	print "Not Found! Creating: "+d

def INSTALL1():
        dialog = xbmcgui.Dialog()      
        dp = xbmcgui.DialogProgress()
        dp.create("TinyOS First Run","Installing Files",'', 'Please Wait')
        
        ### Extract Files ###
        keyword      =  'update-DEMO'
        src = FILES+keyword+'.zip'
        path         =  xbmc.translatePath(os.path.join('special://home/addons','packages'))
        lib          =  os.path.join(path, keyword+'.zip')
        addonfolder  =  xbmc.translatePath(os.path.join('special://home',''))
	shutil.copy2(src, path)
        dp.update(0,"", "Extracting Zip... Please Wait")
        extract.all(lib,addonfolder,dp)
        
        ### Setup Home dir ###
        dp.update(70,"", "Setting up folders... Please Wait")
        
        #Link to External Media 
        if not os.path.exists('/root/ExternalDevices'):
            ln = "ln -s /media/ /root/ExternalDevices"
            subprocess.check_output(ln, shell=True)
        
	### Restart XBMC ###
        dp.update(100,"", "Reloading XBMC")
	time.sleep(3)
	xbmc.executebuiltin('RestartApp')


class firstrun(service):
    def onStart(self):
        #Apply update-DEMO        
        firstlock100 = os.path.join(ADDON_DATA,'.update-DEMO')
        if not os.path.isfile(firstlock100) :
        	        if not os.path.exists(ADDON_DATA):
                            os.mkdir(ADDON_DATA)

			if src==None or len(src)<1:
				INSTALL1()
			
			open(firstlock100,'w').close()	


class start(service):
    def onStart(self):
        #Exec start commands   
	if src==None or len(run)<1:
		EXECUTE()     		
