from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
import random

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
        pos_hint: { "x": 0.2, "y": 0.6}
        on_release:
            app.in_session()

    Button:
        text: "Stop"
        size_hint: 0.2, 0.2
        pos_hint: { "x": 0.6, "y": 0.6}
        on_release:
            app.stop_function()
    
'''

Builder.load_string(kv)

class RootFloatLayout(FloatLayout):

    label_string = StringProperty('Hello World!')

    def play_tech(self):
        # this is my way of randomizing ,
        #  make one that matches your liking by studying the random() built in Class
        #  or make your own !
        sounds = ['Ding Dong','Bird Chirp','Buzzz','Whistle']
        if random.randint(1,200) == 2:
            self.label_string = "Sound: "+sounds[random.randint(0,3)]
    
    def on_session_begin(self,dt):
        # place all the activities you want to run when on_session() method is called here
        self.play_tech()

        # to stop the event when the on_session() method has done its job,
        # return False  

class ReminderApp(App):
    def build(self):
        self.root_layout = RootFloatLayout()
        return self.root_layout
    
    def in_session(self):
        # creates a Clock based event that runs the on_session_begin () once (1) every 60 seconds
        self.root_layout.label_string = "Session is on!"
        self.event = Clock.schedule_interval(self.root.on_session_begin, 1./60.)
        

    def stop_function(self):
        # stops calling the on_session_begin() method, even midway
        self.root_layout.label_string = "Stopped!"
        self.event.cancel()

if __name__ == '__main__':
    ReminderApp().run()