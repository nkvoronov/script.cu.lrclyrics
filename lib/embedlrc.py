from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from lib.utils import *

LANGUAGE = ADDON.getLocalizedString

def getEmbedLyrics(song, getlrc):
    lyrics = Lyrics()
    lyrics.song = song
    lyrics.source = LANGUAGE(32002)
    lyrics.lrc = getlrc
    filename = song.filepath
    ext = os.path.splitext(filename)[1].lower()
    lry = None
    if ext == '.mp3':
        lry = getID3Lyrics(filename, getlrc)
        if not lry:
            try:
                text = getLyrics3(filename, getlrc)
                if text:
                    enc = chardet.detect(text)
                    lry = text.decode(enc['encoding'])
            except:
                pass
    elif  ext == '.flac':
        lry = getFlacLyrics(filename, getlrc)
    elif  ext == '.m4a':
        lry = getMP4Lyrics(filename, getlrc)
    if not lry:
        return None
    lyrics.lyrics = lry
    return lyrics

'''
Get lyrics embed with Lyrics3/Lyrics3V2 format
See: http://id3.org/Lyrics3
     http://id3.org/Lyrics3v2
'''
def getLyrics3(filename, getlrc):
    f = xbmcvfs.File(filename)
    f.seek(-128-9, os.SEEK_END)
    buf = f.readBytes(9)
    if (buf != b'LYRICS200' and buf != b'LYRICSEND'):
        f.seek(-9, os.SEEK_END)
        buf = f.readBytes(9)
    if (buf == b'LYRICSEND'):
        ''' Find Lyrics3v1 '''
        f.seek(-5100-9-11, os.SEEK_CUR)
        buf = f.readBytes(5100+11)
        f.close();
        start = buf.find(b'LYRICSBEGIN')
        content = buf[start+11:]
        if (getlrc and isLRC(content)) or (not getlrc and not isLRC(content)):
            return content
    elif (buf == b'LYRICS200'):
        ''' Find Lyrics3v2 '''
        f.seek(-9-6, os.SEEK_CUR)
        size = int(f.readBytes(6))
        f.seek(-size-6, os.SEEK_CUR)
        buf = f.readBytes(11)
        if(buf == b'LYRICSBEGIN'):
            buf = f.readBytes(size-11)
            f.close();
            tags=[]
            while buf!= '':
                tag = buf[:3]
                length = int(buf[3:8])
                content = buf[8:8+length]
                if (tag == 'LYR'):
                    if (getlrc and isLRC(content)) or (not getlrc and not isLRC(content)):
                        return content
                buf = buf[8+length:]

def ms2timestamp(ms):
    mins = '0%s' % int(ms/1000/60)
    sec = '0%s' % int((ms/1000)%60)
    msec = '0%s' % int((ms%1000)/10)
    timestamp = '[%s:%s.%s]' % (mins[-2:],sec[-2:],msec[-2:])
    return timestamp

'''
Get USLT/SYLT/TXXX lyrics embed with ID3v2 format
See: http://id3.org/id3v2.3.0
'''
def getID3Lyrics(filename, getlrc):
    try:
        data = MP3(filename)
        lyr = ''
        for tag,value in data.items():
            if getlrc and tag.startswith('SYLT'):
                for line in data[tag].text:
                    txt = line[0].strip()
                    stamp = ms2timestamp(line[1])
                    lyr += '%s%s\r\n' % (stamp, txt)
            elif not getlrc and tag.startswith('USLT'):
                if data[tag].text:
                    lyr = data[tag].text
            elif tag.startswith('TXXX'):
                if getlrc and tag.upper().endswith('SYNCEDLYRICS'): # TXXX tags contain arbitrary info. only accept 'TXXX:SYNCEDLYRICS'
                    lyr = data[tag].text[0]
                elif not getlrc and tag.upper().endswith('LYRICS'): # TXXX tags contain arbitrary info. only accept 'TXXX:LYRICS'
                    lyr = data[tag].text[0]
            if lyr:
                return lyr
    except:
        return

def getFlacLyrics(filename, getlrc):
    try:
        tags = FLAC(filename)
        if 'lyrics' in tags:
            lyr = tags['lyrics'][0]
            match = isLRC(lyr)
            if (getlrc and match) or ((not getlrc) and (not match)):
                return lyr
    except:
        return

def getMP4Lyrics(filename, getlrc):
    try:
        tags = MP4(filename)
        if '©lyr' in tags:
            lyr = tags['©lyr'][0]
            match = isLRC(lyr)
            if (getlrc and match) or ((not getlrc) and (not match)):
                return lyr
    except:
        return

def isLRC(lyr):
    match = re.compile('\[(\d+):(\d\d)(\.\d+|)\]').search(lyr)
    if match:
        return True
