import urllib, os
import requests
from requests import *
from urllib.request import Request, urlopen
from Talk import *


def Convert():
    print("Converting")
    os.system('\"C:\\Program Files (x86)\\CoolUtils\\TotalAudioConverter\\AudioConverter.exe\" C:\\Users\\Ariken\\PycharmProjects\\pyaudio\\output.wav C:\\Users\\Ariken\\PycharmProjects\\pyaudio\\output.flac')
    print("Done")


def Send():
    global ANSWER
    url = 'https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-EN'  # Здесь можно выбрать язык
    flac = open('C:\\Users\\Ariken\\PycharmProjects\\pyaudio\\output.flac', "rb").read()
    header = {'Content-Type': 'audio/x-flac; rate=16000'}

    req = Request(url, data=flac, headers=header)
    try:
        data = urlopen(request, timeout=self.operation_timeout)
    except HTTPError as e:
        raise RequestError("recognition request failed: {}".format(e.reason))
    except URLError as e:
        raise RequestError("recognition connection failed: {}".format(e.reason))

    a = data.read()

    print(a)
    ANSWER = eval(a)
    if ANSWER['status'] == 5:
        print('Sorry, I do not understand you.')
        Talk('Sorry, I do not understand you.')
        ANSWER = 0

    else:
        ANSWER = ANSWER['hypotheses'][0]['utterance']  # Отбираем то что google нам ответил(можно иначе)
        print(ANSWER)
    os.remove('C:\\Users\\Егор\\Desktop\\Расширение\\output.wav')  # Удаляем ненужные записи
    os.remove('C:\\Users\\Егор\\Desktop\\Расширение\\output.flac')
    return ANSWER
