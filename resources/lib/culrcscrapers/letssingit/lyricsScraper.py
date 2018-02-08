#-*- coding: UTF-8 -*-
import re
import urllib.request
import urllib.parse
import socket
import difflib
from utilities import *

__title__ = 'letssingit'
__priority__ = '230'
__lrc__ = False


socket.setdefaulttimeout(10)

class LyricsFetcher:
    def __init__(self):
        self.url = 'https://search.letssingit.com/?s=%s&a=search&l=archive'

    def get_lyrics(self, song):
        log('%s: searching lyrics for %s - %s' % (__title__, song.artist, song.title))
        lyrics = Lyrics()
        lyrics.song = song
        lyrics.source = __title__
        lyrics.lrc = __lrc__
        query = '%s+%s' % (urllib.parse.quote_plus(song.artist), urllib.parse.quote_plus(song.title))
        print('0===================')
        if 1:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:25.0) Gecko/20100101 Firefox/25.0', 'Referer': 'https://www.letssingit.com/'}
            print(self.url % query)
            request = urllib.request.Request(self.url % query, None, headers)
            print('2===================')
            req = urllib.request.urlopen(request)
            print('3===================')
            response = req.read().decode('utf-8')
            print('4===================')
            print(str(response))
#        except:
 #           return
        req.close()
        matchcode = re.search('</td><td><a href="(.*?)"', response)
        if matchcode:
            lyricscode = (matchcode.group(1))
            clean = lyricscode.lstrip('http://www.letssingit.com/').rsplit('-',1)[0]
            result = clean.replace('-lyrics-', ' ')
            if (difflib.SequenceMatcher(None, query.lower().replace('+', ''), result.lower().replace('-', '')).ratio() > 0.8):
                if 1:
                    request = urllib.request.Request(lyricscode)
                    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:25.0) Gecko/20100101 Firefox/25.0')
                    req = urllib.request.urlopen(request)
                    resp = req.read().decode('utf-8')
    #            except:
     #               return
                req.close()
                match = re.search('id=lyrics>(.*?)<div i', resp, flags=re.DOTALL)
                if match:
                    lyrics.lyrics = match.group(1).replace('<br>', '')
                    return lyrics
