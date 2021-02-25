import urllib, pycurl
from ctypes import *


def Talk(text):

    def downloadFile(url, fileName):
        fp = open(fileName, "wb")
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.WRITEDATA, fp)
        curl.perform()
        curl.close()
        fp.close()

    def getGoogleSpeechURL(phrase):
        googleTranslateURL = "http://translate.google.com/translate_tts?tl=en&"
        parameters = {'q': phrase}
        data = urllib.urlencode(parameters)
        googleTranslateURL = "%s%s" % (googleTranslateURL, data)
        return googleTranslateURL

    def speakSpeechFromText(phrase):
        googleSpeechURL = getGoogleSpeechURL(phrase)
        downloadFile(googleSpeechURL, "ans.mp3")  # файл, полученный с сервера сохраняется под именем ans.mp3

    speakSpeechFromText(text)

    # используем кодеки, чтобы воспроизвести речь

    winmm = windll.winmm
    winmm.mciSendStringA('Open "ans.mp3" Type MPEGVideo Alias theMP3', 0, 0, 0)
    winmm.mciSendStringA('Play theMP3 Wait', 0, 0, 0)
    winmm.mciSendStringA("Close theMP3", "", 0, 0)