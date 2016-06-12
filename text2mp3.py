# create an mp3 | added by Giovanni Gatto, from the pndurette gTTS repository 12/06/2016 for python 3.4
from gtts import gTTS

def text2MP3(words,mp3name,language="it"):
	'Create an mp3 file thanks to google API'
	tts=gTTS(text=words,lang=language)
	tts.save("%s.mp3" % mp3name)
	print("File %s.mp3 creato" % mp3name)

# es.1 text2MP3("hello","hello","en")
# es.2 text2MP3("merci beaucoup","merci","fr")

# This text will become an mp3
u1 = "Ungaretti nacque ad Alessandria d'Egitto nel 1888. I genitori erano originari della provincia di Lucca."
u1 += "Il padre lavorava allo scavo del Canale di Suez e morì in un incidente quando Giuseppe aveva solo 2 anni, nel 1890." 
u1 += "La madre, Maria Lunardini, mandò avanti la gestione di un forno di proprietà,"
u1 += "con il quale potè far studiare Giuseppe in una delle più prestigiose scuole di Alessandria."
u1 += "Nel 1912 Giuseppe andò a studiare a Parigi. Qui conobbe molti intellettuali e artisti come Picasso e Marinetti.
u1 += "Pubblicò le prime poesie sulla rivista Lacerba."
# The call to te function (if you change language, ad "en", "fr" etc. as 3rd arg)
text2MP3(u1,"mp31") #mp31 is the name of the mp3 audio file that will be created 
# ------------------------------------------------------
