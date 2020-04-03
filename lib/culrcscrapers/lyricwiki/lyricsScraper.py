#-*- coding: UTF-8 -*-
import sys
import re
import json
import urllib.request
import urllib.parse
import socket
from html.parser import HTMLParser
import xbmc
import xbmcaddon
from lib.utils import *

__title__ = 'lyricwiki'
__priority__ = '200'
__lrc__ = False

LIC_TXT = 'we are not licensed to display the full lyrics for this song at the moment'

socket.setdefaulttimeout(10)

class LyricsFetcher:
    def __init__(self):
        self.url = 'http://lyrics.wikia.com/api.php?func=getSong&artist=%s&song=%s&fmt=realjson'

    def get_lyrics(self, song):
        log('%s: searching lyrics for %s - %s' % (__title__, song.artist, song.title))
        lyrics = Lyrics()
        lyrics.song = song
        lyrics.source = __title__
        lyrics.lrc = __lrc__
        try:
            req = urllib.request.urlopen(self.url % (urllib.parse.quote(song.artist), urllib.parse.quote(song.title)))
            response = req.read()
        except:
            return None
        req.close()
        data = json.loads(response)
        try:
            self.page = data['url']
        except:
            return None
        if not self.page.endswith('action=edit'):
            log('%s: search url: %s' % (__title__, self.page))
            try:
                req = urllib.request.urlopen(self.page)
                response = req.read().decode('utf-8')
            except urllib.request.HTTPError as error: # strange... sometimes lyrics are returned with a 404 error
                if error.code == 404:
                    response = error.read().decode('utf-8')
                else:
                    return None
            req.close()
            matchcode = re.search("class='lyricbox'>(.*?)<div", response)
            try:
                lyricscode = (matchcode.group(1))
                htmlparser = HTMLParser()
                lyricstext = htmlparser.unescape(lyricscode).replace('<br />', '\n')
                lyr = re.sub('<[^<]+?>', '', lyricstext)
                if LIC_TXT in lyr:
                    return None
                lyrics.lyrics = lyr
                return lyrics
            except:
                return None
        else:
            return None
