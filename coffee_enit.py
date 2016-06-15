# create an mp3 | added by Giovanni Gatto
from gTTSMulti import gTTS
import os

def tts2MP3(words,mp3name,language="en"):
	global tts
	'It creates an mp3 (default french) file thanks to google API'
	tts=gTTS(text=words,lang=language)
	tts.saveTmp("%s.mp3" % mp3name)
	#print("File %s.mp3 creato" % mp3name)

def listen():
	folder=os.listdir(os.getcwd())
	for files in folder:
		if files.endswith(".mp3"):
			os.startfile(files)

def enit(english,italian,fileName="coffee"):
	tts2MP3(english,fileName)
	print(english)
	tts2MP3(italian,fileName,"it")
	print(italian)


enit("DOSING","Dosaggio")
enit("Put the coffee ground into a filter holder so that the coffee is evenly distributed","Metti il caffè in un portafiltro in modo che il caffè sia distribuito in modo uniforme.")
enit("You must use coffee ground specifically for the Espresso. You must use 7 grams for each espresso. 14 grams in total.","Devi usare una miscela di caffè specifica per l'espresso. Devi usare 7 grammi per ogni caffè. 14 in totale")
enit("Tap the filter-holder a  couple of times","Batti sul portafiltro un paio di volte")
enit("Make the coffee ground compact","Rendi compatto il caffè")
enit("Then we press a little bit the coffee into the filter holder to compact it","Poi premi un poco sul caffè nel portafiltro per compattarlo")

enit("Now the filter holder is ready","Adesso il portafiltro è pronto")

enit("the coffee should be poured in the cups in 25 seconds","Il caffè dovrebbe essere versato nella tazzina in 25 secondi")
enit("Put the two coffee into a mixer and add 5 spoons of sugar","Metti i due caffè nel mixer e aggiungi lo zucchero")
enit("Mix the coffee and the sugar, then add some ice cubes","Mixa il caffè e lo zucchero e aggiungi del ghiaccio")
enit("Pour the cream of coffee in two glasses","Versa la crema d caffè in due bicchieri")
enit("Finally, garnish with a lemon peel and a little bit of coffee ground.","Infine, guarnire con una buccia di limone e un poco di caffè macinato.")

tts.close()