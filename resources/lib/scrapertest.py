from utilities import *
from culrcscrapers.alsong import lyricsScraper as lyricsScraper_alsong
from culrcscrapers.baidu import lyricsScraper as lyricsScraper_baidu
from culrcscrapers.darklyrics import lyricsScraper as lyricsScraper_darklyrics
from culrcscrapers.genius import lyricsScraper as lyricsScraper_genius
from culrcscrapers.gomaudio import lyricsScraper as lyricsScraper_gomaudio
from culrcscrapers.lyricsmode import lyricsScraper as lyricsScraper_lyricsmode
from culrcscrapers.lyricwiki import lyricsScraper as lyricsScraper_lyricwiki
from culrcscrapers.minilyrics import lyricsScraper as lyricsScraper_minilyrics
from culrcscrapers.ttplayer import lyricsScraper as lyricsScraper_ttplayer

FAILED = []

def test_scrapers():
    dialog = xbmcgui.DialogProgress()

    # test alsong
    dialog.create(ADDONNAME, LANGUAGE(32163) % 'alsong')
    log("==================== alsong ====================")
    song = Song('Blur', "There's No Other Way")
    lyrics = lyricsScraper_alsong.LyricsFetcher().get_lyrics(song)
    if lyrics:
        log(lyrics.lyrics)
    else:
        FAILED.append('alsong')
        log("FAILED: alsong")
    if dialog.iscanceled():
        return

    # test baidu
    dialog.update(11, LANGUAGE(32163) % 'baidu')
    log("==================== baidu ====================")
    song = Song('Blur', "There's No Other Way")
    lyrics = lyricsScraper_baidu.LyricsFetcher().get_lyrics(song)
    if lyrics:
        log(lyrics.lyrics)
    else:
        FAILED.append('baidu')
        log("FAILED: baidu")
    if dialog.iscanceled():
        return

    # test darklyrics
    dialog.update(22, LANGUAGE(32163) % 'darklyrics')
    log("==================== darklyrics ====================")
    song = Song('Neurosis', 'Lost')
    lyrics = lyricsScraper_darklyrics.LyricsFetcher().get_lyrics(song)
    if lyrics:
        log(lyrics.lyrics)
    else:
        FAILED.append('darklyrics')
        log("FAILED: darklyrics")
    if dialog.iscanceled():
        return

    # test genius
    dialog.update(33, LANGUAGE(32163) % 'genius')
    log("==================== genius ====================")
    song = Song('Maren Morris', 'My Church')
    lyrics = lyricsScraper_genius.LyricsFetcher().get_lyrics(song)
    if lyrics:
        log(lyrics.lyrics)
    else:
        FAILED.append('genius')
        log("FAILED: genius")
    if dialog.iscanceled():
        return

    # test gomaudio
    dialog.update(44, LANGUAGE(32163) % 'gomaudio')
    log("==================== gomaudio ====================")
    song = Song('Lady Gaga', 'Just Dance')
    lyrics = lyricsScraper_gomaudio.LyricsFetcher().get_lyrics(song, 'd106534632cb43306423acb351f8e6e9', '.mp3')
    if lyrics:
        log(lyrics.lyrics)
    else:
        FAILED.append('gomaudio')
        log("FAILED: gomaudio")
    if dialog.iscanceled():
        return

    # test lyricsmode
    dialog.update(55, LANGUAGE(32163) % 'lyricsmode')
    log("==================== lyricsmode ====================")
    song = Song('Maren Morris', 'My Church')
    lyrics = lyricsScraper_lyricsmode.LyricsFetcher().get_lyrics(song)
    if lyrics:
        log(lyrics.lyrics)
    else:
        FAILED.append('lyricsmode')
        log("FAILED: lyricsmode")
    if dialog.iscanceled():
        return

    # test lyricwiki
    dialog.update(66, LANGUAGE(32163) % 'lyricwiki')
    log("==================== lyricwiki ====================")
    song = Song('Maren Morris', 'My Church')
    lyrics = lyricsScraper_lyricwiki.LyricsFetcher().get_lyrics(song)
    if lyrics:
        log(lyrics.lyrics)
    else:
        FAILED.append('lyricwiki')
        log("FAILED: lyricwiki")
    if dialog.iscanceled():
        return

    # test minilyrics
    dialog.update(77, LANGUAGE(32163) % 'minilyrics')
    log("==================== minilyrics ====================")
    song = Song('Ace Of Base', 'All That She Wants')
    lyrics = lyricsScraper_minilyrics.LyricsFetcher().get_lyrics(song)
    if lyrics:
        log(lyrics.lyrics)
    else:
        FAILED.append('minilyrics')
        log("FAILED: minilyrics")
    if dialog.iscanceled():
        return

    # test ttplayer
    dialog.update(88, LANGUAGE(32163) % 'ttplayer')
    log("==================== ttplayer ====================")
    song = Song('Abba', 'Elaine')
    lyrics = lyricsScraper_ttplayer.LyricsFetcher().get_lyrics(song)
    if lyrics:
        log(lyrics.lyrics)
    else:
        FAILED.append('ttplayer')
        log("FAILED: ttplayer")
    if dialog.iscanceled():
        return

    dialog.close()
    log("=======================================")
    log('FAILED: %s' % str(FAILED))
    log("=======================================")
    if FAILED:
        dialog = xbmcgui.Dialog().ok(ADDONNAME, LANGUAGE(32165) % ' / '.join(FAILED))
    else:
        dialog = xbmcgui.Dialog().ok(ADDONNAME, LANGUAGE(32164))
