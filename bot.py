from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

bot = ChatBot("AceBot")

conversa = ['Oi',
	'Olá',
		'Como você está?',
	'Bem, e você?',
		'Eu estou bem',
	'Que bom',
		'Que fazes?',
	'De bom nada e você?',
		'Mesma coisa',
	'Somos criaturas aborrecidas',
		'Talvez sim',
	'CONCORDE',
		'Não',
	'Então tchau coisa feia']
	
trainer = ListTrainer(bot)
trainer.train(conversa)

def ouvir_microfone():
	microfone = sr.Recognizer()
	with sr.Microphone() as source:
		microfone.adjust_for_ambient_noise(source)
		print("Microfone ativado...")
		audio = microfone.listen(source)
	try:
		frase = microfone.recognize_google(audio, language='pt-BR')
		print("Humano: " + frase)
	except sr.UnknowValueError:
		print('bot: Isso não funcionou')
	return frase

def criar_audio(audio):
	tts = gTTS(audio, lang="pt-BR")
	tts.save('bot.mp3')
	playsound('bot.mp3')	

while True:
	quest = ouvir_microfone()
	resposta = bot.get_response(quest)
	criar_audio(str(resposta))
	print('Bot: ', resposta)