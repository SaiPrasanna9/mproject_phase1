import os,signal
import speech_recognition as sr
import pyttsx3

import spacy
import multiprocessing


import kivy

kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.button import Button


nlp = spacy.load('en_core_web_sm')

class ButtonApp(App):
	
	def audio_to_text(self):
		# Python program to translate
		# speech to text and text to speech

		# Initialize the recognizer
		r = sr.Recognizer()

		# Function to convert text to
		# speech
		def SpeakText(command):
			
			# Initialize the engine
			engine = pyttsx3.init()
			engine.say(command)
			engine.runAndWait()
					
		# Loop infinitely for user to
		# speak
		while(1):	
			# Exception handling to handle
			# exceptions at the runtime
			try:
				# use the microphone as source for input.
				with sr.Microphone() as source2:	
					# wait for a second to let the recognizer
					# adjust the energy threshold based on
					# the surrounding noise level
					r.adjust_for_ambient_noise(source2, duration=0.2)
					
					#listens for the user's input
					audio2 = r.listen(source2)
					print("processing")
					
					# Using ggogle to recognize audio
					MyText = r.recognize_google(audio2)
					MyText = MyText.lower()

					print("Did you say "+MyText)
					#SpeakText(MyText)

					print("generating reminders")
					#print(generate_rem(MyText))
					rem_list=self.generate_rem(MyText)
					print(rem_list)
					#{'take me': '2:00 p.m. 2021-09-03'}
					r_list=[]
					for rem in rem_list.keys():
						a=rem_list[rem]
						try:
							add_date=parse(a, fuzzy_with_tokens=True)
							add_date=add_date[0]
							print("adding remainder to calendar")
							self.add_rem([rem,add_date])
							print("added remainder in calendar")
						except Exception as e:
							print("unable to parse the generated reminder date {0}".format(a))

						#d_datetime=datetime.now()
						'''if 'today' in a:

						if "a.m." in a:
							a=a.replace("a.m.","AM")
							p=datetime.strptime(a, "%H:%M %p %Y-%m-%d")
						elif "p.m." in a:
							a=a.replace("p.m.","PM")
							p=datetime.strptime(a, "%H:%M %p %Y-%m-%d")'''
						
						
			
			except sr.RequestError as e:
				print("Could not request results; {0}".format(e))
				
			except sr.UnknownValueError:
				print("couldn't recognize")


	def build(self):
		# use a (r, g, b, a) tuple
		btn = Button(text ="Push Me !",
				font_size ="20sp",
				background_color =(1, 1, 1, 1),
				color =(1, 1, 1, 1),
				size =(32, 32),
				size_hint =(.2, .2),
				pos =(300, 250))

		btn.bind(on_press = self.callback)
		return btn

	# callback function tells when button pressed
	def callback(self, event):

		print("button pressed")
		print('Yoooo !!!!!!!!!!!')
		print("recording")
		self.audio_to_text()
		


root = ButtonApp()
root.run()
