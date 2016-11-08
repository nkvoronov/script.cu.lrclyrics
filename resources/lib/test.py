import xbmcaddon

ADDON = xbmcaddon.Addon()
ADDONID = ADDON.getAddonInfo('id')
CWD = xbmc.translatePath(ADDON.getAddonInfo('path')).decode("utf-8")
PROFILE = xbmc.translatePath(ADDON.getAddonInfo('profile')).decode("utf-8")

from utilities import *
from culrcscrapers.baidu import lyricsScraper as lyricsScraper_baidu
from culrcscrapers.darklyrics import lyricsScraper as lyricsScraper_darklyrics
from culrcscrapers.genius import lyricsScraper as lyricsScraper_genius
from culrcscrapers.gomaudio import lyricsScraper as lyricsScraper_gomaudio
from culrcscrapers.lyricsmode import lyricsScraper as lyricsScraper_lyricsmode
from culrcscrapers.lyricwiki import lyricsScraper as lyricsScraper_lyricwiki
from culrcscrapers.ttplayer import lyricsScraper as lyricsScraper_ttplayer

FAILED = []

# test baidu
song = Song('Blur', "There's No Other Way")
lyrics = lyricsScraper_baidu.LyricsFetcher().get_lyrics(song)
log("=======================================")
if lyrics:
    log(lyrics.lyrics)
else:
    FAILED.append('baidu')
    log("FAILED: baidu")


# test darklyrics
song = Song('Neurosis', 'Lost')
lyrics = lyricsScraper_darklyrics.LyricsFetcher().get_lyrics(song)
log("=======================================")
if lyrics:
    log(lyrics.lyrics)
else:
    FAILED.append('darklyrics')
    log("FAILED: darklyrics")


# test genius
song = Song('Maren Morris', 'My Church')
lyrics = lyricsScraper_genius.LyricsFetcher().get_lyrics(song)
log("=======================================")
if lyrics:
    log(lyrics.lyrics)
else:
    FAILED.append('genius')
    log("FAILED: genius")


# TODO test gomaudio
song = Song('', '')
lyrics = lyricsScraper_gomaudio.LyricsFetcher().get_lyrics(song)
log("=======================================")
if lyrics:
    log(lyrics.lyrics)
else:
    FAILED.append('gomaudio')
    log("FAILED: gomaudio")


# test lyricsmode
song = Song('Maren Morris', 'My Church')
lyrics = lyricsScraper_lyricsmode.LyricsFetcher().get_lyrics(song)
log("=======================================")
if lyrics:
    log(lyrics.lyrics)
else:
    FAILED.append('lyricsmode')
    log("FAILED: lyricsmode")


# test lyricwiki
song = Song('Maren Morris', 'My Church')
lyrics = lyricsScraper_lyricwiki.LyricsFetcher().get_lyrics(song)
log("=======================================")
if lyrics:
    log(lyrics.lyrics)
else:
    FAILED.append('lyricwiki')
    log("FAILED: lyricwiki")


# test ttplayer
song = Song('Abba', 'Elaine')
lyrics = lyricsScraper_ttplayer.LyricsFetcher().get_lyrics(song)
log("=======================================")
if lyrics:
    log(lyrics.lyrics)
else:
    FAILED.append('ttplayer')
    log("FAILED: ttplayer")


log("=======================================")
log(FAILED)
log("=======================================")
