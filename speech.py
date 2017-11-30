#Ashaar Gautam
# CS 370
import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander

running = True
def say(text):
	subprocess.call('say ' + text, shell = True)

# Just plays audio files
def play_audio(filename):
	chunk = 1024# number of frames in the buffer
	wf = wave.open(filename, 'rb')# open the audio file as binary
	pa = pyaudio.PyAudio()# instantiate pyaudio

    #loading the file
	stream = pa.open(
	    format = pa.get_format_from_width(wf.getsampwidth()),
	    channels = wf.getnchannels(),
	    rate = wf.getframerate(),
        output = True
	)

	data_stream = wf.readframes(chunk)# read the data

	# play the stream
	while data_stream:
	    stream.write(data_stream)
	    data_stream = wf.readframes(chunk)

	stream.close()# stop the stream
	pa.terminate()# close pyaduio

r = sr.Recognizer()# instantiate SpeechRecognizer
cmd = Commander()# listen to you speech and recognize
def youTalk():
	print("Listening...")
	play_audio("./audio/suppressed.wav")# plays audio to begin listening

	with sr.Microphone() as source:
	    print("Say Something")
	    audio = r.listen(source)# listens to our speech

	play_audio("./audio/wet.wav")# plays sound to end listening

	command = ""

	try:
		command = r.recognize_google(audio)# uses google to determine what we say
	except:
	    print("Couldn't understand you bro.")# if it cant understand us

	print("Your command:")
	print(command)
	if command in ["quit","exit","bye","goodbye"]:
            global running 
	    running = False

	cmd.discover(command)
    #say('You said: ' + command)

while running == True:
	youTalk()
