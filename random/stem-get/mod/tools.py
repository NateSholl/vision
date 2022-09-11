from __future__ import unicode_literals
from re import I
import youtube_dl as yt
from spleeter.separator import Separator
import keyfinder as kf
import os


def downloadAudio():

    url = input('Enter URL = ')
    dlOptions = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'aac',
            'preferredquality': '192',
        }]
    }
    with yt.YoutubeDL(dlOptions) as ytDown:
        info = ytDown.extract_info(url, download=True)
        fileName = ytDown.prepare_filename(info)
        grabDot = 0
        for i in range(0,len(fileName)):
            if fileName[-i] == '.':
                grabDot = i - 1
                break
        convfileName = fileName[0:-grabDot] + 'aac'
        return convfileName

def ripStems(fileName):

    separator = Separator("spleeter:4stems")
    separator.separate_to_file(f'{fileName}', './')

def findKey(fileName):

    key = kf.key(str(fileName))
    newFile = str(key) + '-' + fileName 
    os.rename(fileName, newFile)
    return newFile

