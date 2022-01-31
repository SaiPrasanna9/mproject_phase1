from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
import random
import datetime as dateTime
from datetime import datetime, timedelta

import speech_recognition as sr
import pyttsx3

import spacy
#import multiprocessing



from dateutil.parser import parse


nlp = spacy.load('en_core_web_sm')
r = sr.Recognizer()
m = sr.Microphone()



kv = '''
<RootFloatLayout>:

    Label:
        text: root.label_string

    Button:
        text: "Back"
        font_size: 0.4 * self.height
        size_hint: 0.1, 0.08
        pos_hint: {"x": 0.45, "y": 0.05}
        # on_release:
        #     app.root.current = "cog"
        #     root.manager.transition.direction = "right"

    Button:
        text: "Start"
        size_hint: 0.2, 0.2
        pos_hint: { "x": 0.2, "y": 0.1}
        on_release:
            app.in_session()

    Button:
        text: "Stop"
        size_hint: 0.2, 0.2
        pos_hint: { "x": 0.6, "y": 0.1}
        on_release:
            app.stop_function()
    
'''

Builder.load_string(kv)

class RootFloatLayout(FloatLayout):

    label_string = StringProperty('Hello World!')
    some=''
    def record(self):
        # GUI Blocking Audio Capture
        with m as source:
            self.audio = r.listen(source)
            print("here4 listening")
        try:
            value = r.recognize_google(self.audio)
            print("llllllllllllllllllll"*30,value,"llllllllll"*30)
        except Exception:
            print("some error")
        #self.come(audio)
    def rstart(self):
        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(r.energy_threshold))  


    def play_tech(self):
        # this is my way of randomizing ,
        #  make one that matches your liking by studying the random() built in Class
        #  or make your own !
        sounds = ['Ding Dong','Bird Chirp','Buzzz','Whistle']
        if random.randint(1,200) == 2:
            self.label_string = "Sound: "+sounds[random.randint(0,3)]
            self.rstart()
            #Clock.schedule_interval(self.update_time, 0)
            self.record()
        if(self.some=='Started'):
            self.rstart()
            #Clock.schedule_interval(self.update_time, 0)
            self.record()

        
    def on_session_begin(self,dt):
        # place all the activities you want to run when on_session() method is called here
        self.play_tech()

        # to stop the event when the on_session() method has done its job,
        # return False  

class StackOverFLow(App):
    def build(self):
        self.root_layout = RootFloatLayout()
        return self.root_layout
    
    def in_session(self):
        # creates a Clock based event that runs the on_session_begin () once (1) every 60 seconds
        self.root_layout.label_string = "Session is on!"
        self.some='Started'
        self.event = Clock.schedule_interval(self.root.on_session_begin, 1./60.)

        

    def stop_function(self):
        # stops calling the on_session_begin() method, even midway
        self.root_layout.label_string = "Stopped!"
        self.some='Stopped'

        self.event.cancel()

if __name__ == '__main__':
    StackOverFLow().run()