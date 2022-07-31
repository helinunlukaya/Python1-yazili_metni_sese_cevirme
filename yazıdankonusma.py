from gtts import gTTS
import os
from os import path
dosya= open (" kulkedisi.txt",encoding="utf-8")
yazi=dosya.read()
cikti=gTTS (text=yazi,lang="tr",slow=False)
dosya.close()
