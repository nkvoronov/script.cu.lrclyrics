#-*- coding: UTF-8 -*-
import time
from utilities import *
from culrcscrapers.alsong import lyricsScraper as lyricsScraper_alsong
from culrcscrapers.baidu import lyricsScraper as lyricsScraper_baidu
from culrcscrapers.darklyrics import lyricsScraper as lyricsScraper_darklyrics
from culrcscrapers.genius import lyricsScraper as lyricsScraper_genius
from culrcscrapers.gomaudio import lyricsScraper as lyricsScraper_gomaudio
from culrcscrapers.lyricscom import lyricsScraper as lyricsScraper_lyricscom
from culrcscrapers.lyricsmode import lyricsScraper as lyricsScraper_lyricsmode
from culrcscrapers.letssingit import lyricsScraper as lyricsScraper_letssingit
from culrcscrapers.lyricwiki import lyricsScraper as lyricsScraper_lyricwiki
from culrcscrapers.minilyrics import lyricsScraper as lyricsScraper_minilyrics
from culrcscrapers.ttplayer import lyricsScraper as lyricsScraper_ttplayer
from culrcscrapers.xiami import lyricsScraper as lyricsScraper_xiami

FAILED = []

def test_scrapers():
    dialog = xbmcgui.DialogProgress()
    TIMINGS = []

    # test alsong
    dialog.create(ADDONNAME, LANGUAGE(32163) % 'alsong')


    # test ttplayer
    dialog.update(90, LANGUAGE(32163) % 'ttplayer')
    log('==================== ttplayer ====================')
    song = Song('Abba', 'Elaine')
    st = time.time()
    lyrics = lyricsScraper_ttplayer.LyricsFetcher().get_lyrics(song)
    ft = time.time()
    tt = ft - st
    TIMINGS.append(['ttplayer',tt])
    if lyrics:
        log(lyrics.lyrics)
    else:
        FAILED.append('ttplayer')
        log('FAILED: ttplayer')
    if dialog.iscanceled():
        return

    # test xiami
    dialog.create(ADDONNAME, LANGUAGE(32163) % 'xiami')
    log('==================== xiami ====================')
    song = Song('Bush', 'Swallowed')
    st = time.time()
    lyrics = lyricsScraper_xiami.LyricsFetcher().get_lyrics(song)
    ft = time.time()
    tt = ft - st
    TIMINGS.append(['xiami',tt])
    if lyrics:
        log(lyrics.lyrics)
    else:
        FAILED.append('xiami')
        log('FAILED: xiami')
    if dialog.iscanceled():
        return

    dialog.close()
    log('=======================================')
    log('FAILED: %s' % str(FAILED))
    log('=======================================')
    for item in TIMINGS:
        log('%s - %i' % (item[0], item[1]))
    log('=======================================')
    if FAILED:
        dialog = xbmcgui.Dialog().ok(ADDONNAME, LANGUAGE(32165) % ' / '.join(FAILED))
    else:
        dialog = xbmcgui.Dialog().ok(ADDONNAME, LANGUAGE(32164))
