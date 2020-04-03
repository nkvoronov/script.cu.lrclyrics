from lib.scrapertest import *
from lib.utils import *

ADDON = xbmcaddon.Addon()
ADDONNAME = ADDON.getAddonInfo('name')
ADDONVERSION = ADDON.getAddonInfo('version')
LANGUAGE = ADDON.getLocalizedString

log('script version %s started' % ADDONVERSION)

def culrc_run(service):
    if not WIN.getProperty('culrc.running') == 'true':
        from lib import  gui
        gui.MAIN(mode=service)
    elif not WIN.getProperty('culrc.guirunning') == 'TRUE':
        # we're already running, user clicked button on osd
        WIN.setProperty('culrc.force','TRUE')
    else:
        log('script already running')
        if ADDON.getSettingBool('silent'):
            dialog = xbmcgui.Dialog()
            dialog.notification(ADDONNAME, LANGUAGE(32158), time=2000, sound=False)

if (__name__ == '__main__'):
    service = ADDON.getSettingBool('service')
    if sys.argv == [''] and not service:
        log('service not enabled')
    else:
        if len(sys.argv) == 2 and sys.argv[1] == 'test':
            from lib import scrapertest
            test_scrapers()
        else:
            culrc_run(service)

log('script version %s ended' % ADDONVERSION)
