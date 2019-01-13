#! /usr/bin/python3

import pafy
import os
import shutil

getLinkList = open("link.txt")
link = getLinkList.read()
getLinkList.close()

playListURL = link
playlist = pafy.get_playlist(playListURL)
sizePlayList = len(playlist['items'])

i = 0

videoName = ""
numerator = ""
finalName = ""

os.mkdir(playlist['title'])

while i < sizePlayList:
    videoUnit = playlist['items'][i]['pafy'].getbest()
    videoName = videoUnit.title
    numerator = numerator + str(0) + str(i+1) + " - "

    if len(numerator) >= 6:
        numerator = numerator[1:]
    finalName = numerator + videoName

    videoUnit.download()
    os.rename(videoUnit.title + ".mp4", finalName + ".mp4")

    shutil.move(finalName + ".mp4", playlist['title'])

    numerator = ""
    i += 1