from ctypes import *
from Talk import *
from Record import *
from Send import *

def Processing():

 global ANSWER
 if ANSWER == 0:
     return 0

 elif 'chrome' in ANSWER.lower():
     print("chrome")

 elif 'skype' in ANSWER.lower():
    print("skype")


 elif 'cd rom' in ANSWER.lower() or\
   'cd-rom' in ANSWER.lower() or\
   'open d' in ANSWER.lower() or\
   'dvd' in ANSWER.lower() or\
   'dvd-rom' in ANSWER.lower() or\
   'dvd rom' in ANSWER.lower() or\
   'cdrom' in ANSWER.lower() or\
   'cd - rom' in ANSWER.lower():
    winmm = windll.winmm
    winmm.mciSendStringA("set cdaudio door open", "", 0,0)

#Если слышит что- то связанное с dvd то открывает лоток дисковода

if __name__ == "__main__":
    Send()
    Processing()