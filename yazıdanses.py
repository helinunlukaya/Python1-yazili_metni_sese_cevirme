
from gtts import gTTS
import os
text=' Bir varmış bir yokmuş, evvel zaman içinde bir ülkede yaşayan zengin bir tüccar tatlı ve iyi kalpli kızı ile birlikte yaşıyordu. karısının ölümünden sonra evde kızının yalnız kalmasına üzülen babası, iki kızı olan kibirli bir kadınla evlendi. Düğünden bir süre sonra tüccar da ölünce, üvey anne üvey kızını evin hizmetçisi yaptı. Evin tüm işlerini yapmaktan çok yorulan kızcağız geceleri şöminenin yanı başında küllerin arasında uyuyordu.Bu yüzden ona Külkedisi adını takmışlardı. Yıllar sonra Kral oğlunun evleneceği kızı seçmesi için bir balo düzenledi.'
language = 'tr'
speech = gTTS(text = text, lang = language, slow = False)
speech.save("text.mp3")
os.system("text.mp3")