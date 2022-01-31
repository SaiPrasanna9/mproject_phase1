from kivy.app import App
from kivy.uix.button import Button
import os,signal
import speech_recognition as sr
import pyttsx3

import spacy
import multiprocessing


import kivy

kivy.require("1.9.1")



# Requires pyaudio
def record(*arg):
    r = sr.Recognizer()
    print("In function record")
        # Function to convert text to
        # speech
    def SpeakText(command):
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
    while(1):   
        # Exception handling to handle
        # exceptions at the runtime
        print("in while loop")
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:    
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input
                print("listening")
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
            
            
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
                
        except sr.UnknownValueError:
            print("couldn't recognize")




    
class recordApp(App):
    def build(self):
        btn = Button(text ="Push Me !",
                font_size ="20sp",
                background_color =(1, 1, 1, 1),
                color =(1, 1, 1, 1),
                size =(32, 32),
                size_hint =(.2, .2),
                pos =(300, 250))

        btn.bind(on_press = record)
        return btn

        #return Button(text="record", on_press=record)

recordApp().run()