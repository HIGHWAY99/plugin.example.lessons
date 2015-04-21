#############################################################################
#############################################################################
import common
from common import *
from common import (addon_id,addon_name,addon_path)

#############################################################################
#############################################################################
def Menu0(): ## Main Menu ##
	cMI=[]
	#cMI.append(('Information','XBMC.Action(Info)'))
	
	
	ADDON.add_directory({'mode':'BrowsePlayExamples'},{'title':'[COLOR lavender]Folder:  Play Examples[/COLOR]'},fanart=addonFanart,img=addonIcon)
	ADDON.add_directory({'mode':'BrowseRegexExample'},{'title':'[COLOR lavender]Folder:  Regex Example[/COLOR]'},fanart=addonFanart,img=addonIcon)
	ADDON.add_directory({'mode':'BrowsePassText'},{'title':'[COLOR lavender]Folder:  Pass Text Example[/COLOR]'},fanart=addonFanart,img=addonIcon)
	
	
	
	
	setView('movies',getSet("front-view")); eod()
#############################################################################
#############################################################################
def Browse_PlayExamples():
	cMI=[]
	ADDON.add_video_item({'mode':'Play','url':'https://s3.amazonaws.com/pluscast/vod/wisn/master.m3u8'},{'title':'m3u8 Video:  ABC (WISN 12) News'},fanart=addonFanart,img=addonIcon,contextmenu_items=cMI,context_replace=False)
	cMI.append(('Information','XBMC.Action(Info)'))
	ADDON.add_video_item({'mode':'Play','url':'http://www.mediacollege.com/video-gallery/testclips/barsandtone.flv'},{'title':'FLV Video:  Bars and Tone'},fanart=addonFanart,img=addonIcon,contextmenu_items=cMI,context_replace=False)
	ADDON.add_video_item({'mode':'Play','url':'http://www.mediacollege.com/video-gallery/testclips/20051210-w50s.flv'},{'title':'FLV Video:  Windy 50s Mobility Scooter Race'},fanart=addonFanart,img=addonIcon,contextmenu_items=cMI,context_replace=False)
	ADDON.add_video_item({'mode':'Play','url':'http://www.mediacollege.com/video-gallery/testclips/20051210-w50s_56K.flv'},{'title':'FLV Video:  Windy 50s Mobility Scooter Race (56K)'},fanart=addonFanart,img=addonIcon,contextmenu_items=cMI,context_replace=False)
	ADDON.add_video_item({'mode':'PlayR','url':'https://www.youtube.com/watch?v=dN6JDgx2xcU'},{'title':'Youtube Video:  Change Splash boot image on XBMC or KODI'},fanart=addonFanart,img=addonIcon,contextmenu_items=cMI,context_replace=False)
	
	
	setView('movies',getSet("browse-view")); eod()
#############################################################################
#############################################################################

#############################################################################
#############################################################################

#############################################################################
#############################################################################
def Browse_RegexExample():
		html=nolines(getURL('http://www.mediacollege.com/adobe/flash/video/tutorial/example-flv.html'))
		s='<tr>\s*<td>\s*<a href="([^"]+)">\s*([^<]+)\s*</a>\s*</td><td>\s*\d+\s*\D+\s*</td><td>\s*\d+\D+\s*</td><td>\s*(\d+x\d+)\s*</td><td>\s*\d+\s*\D+\s*</td><td>\d+</td>\s*</tr'
		r=re.compile(s).findall(html)
		if r:
			iC=len(r)
			for url,name,resolution in r:
					mode='Play'; n2=''; cMI=[]; cMI.append(('Information','XBMC.Action(Info)')); nameL=name.replace(' ',''); 
					i=addonIcon; IsAFolder=False; 
					if mode=='Play':
						pars={'mode':mode,'url':'http://www.mediacollege.com/'+url.replace('../','')}; 
						cMI.append((url,'XBMC.Action(Info)')); 
						ADDON.add_video_item(pars,{'title':''+name+'  ('+resolution+')','plot':url,'plotoutline':url},fanart=addonFanart,img=i,total_items=iC,contextmenu_items=cMI,context_replace=False)
		setView('movies',getSet("browse-view")); eod()
#############################################################################
#############################################################################

def Browse_PassText(testMsg=''):
		if len(testMsg) > 0:
				ADDON.add_directory({'mode':'BrowsePassText','test':testMsg},{'title':testMsg},fanart=addonFanart,img=addonIcon)
		ADDON.add_directory({'mode':'BrowsePassText','test':'Welcome, user.'},{'title':'Pass Text:  Welcome, user.'},fanart=addonFanart,img=addonIcon)
		ADDON.add_directory({'mode':'BrowsePassText','test':'Good day, everyone.'},{'title':'Pass Text:  Good day, everyone.'},fanart=addonFanart,img=addonIcon)
		ADDON.add_directory({'mode':'BrowsePassText','test':'Hello World.'},{'title':'Pass Text:  Hello World.'},fanart=addonFanart,img=addonIcon)
		ADDON.add_directory({'mode':'BrowsePassText','test':'Example'},{'title':'Pass Text:  Example'},fanart=addonFanart,img=addonIcon)
		ADDON.add_directory({'mode':'BrowsePassText','test':''},{'title':'Pass Text:'},fanart=addonFanart,img=addonIcon)
		
		
		setView('movies',getSet("browse-view")); eod()
#############################################################################
#############################################################################

#############################################################################
#############################################################################

#############################################################################
#############################################################################
def GetPlayerCore():
	try:
		PlayerMethod=getSet("core-player")
		if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
		elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
		elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
		else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	except: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	return PlayerMeth
def PlayStreamWithResolver(url):
		play=xbmc.Player(GetPlayerCore()) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
		import urlresolver
		url=urlresolver.HostedMediaFile(url).resolve()
		try: ADDON.resolve_url(url)
		except: pass
		try: play.play(url)
		except: pass
def PlayStream(url):
		play=xbmc.Player(GetPlayerCore()) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
		try: ADDON.resolve_url(url)
		except: pass
		try: play.play(url)
		except: pass
def PlayURL(url):
		play=xbmc.Player(GetPlayerCore()) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
		try: play.play(url)
		except: pass
#############################################################################
#############################################################################
def zModeCheck(mode='',url=''):
	deb('mode',mode); 
	if (mode=='') or (mode=='main'): Menu0()
	elif mode=='BrowsePlayExamples': Browse_PlayExamples()
	elif mode=='BrowseRegexExample': Browse_RegexExample()
	elif mode=='BrowsePassText': Browse_PassText(addpr('test'))
	elif mode=='Play': PlayStream(url)
	elif mode=='PlayR': PlayStreamWithResolver(url)
	
	
	##
zModeCheck(addpr('mode'),addpr('url'))
#############################################################################
#############################################################################
