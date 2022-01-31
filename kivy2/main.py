from time import strftime
from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.base import runTouchApp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.vector import Vector
from kivy.lang import Builder
from kivy.uix.checkbox import CheckBox
class clockApp(App):
    sw_started= False
    sw_seconds = 0
    def update_time(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = (
            '%02d:%02d.[size=20]%02d[/size]'%
            (int(minutes), int(seconds),
             int(seconds* 100 % 100))
        )
        self.root.ids.stopwatch.color=(0,0,1,1)
        #self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')
        self.root.ids.time.color=(1,0,1,1)
    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)
    def start_stop(self):
        self.root.ids.start_stop.text =(
            'Start' if self.sw_started else 'Stop'
        )
        self.root.ids.start_stop.background_color =(
            (0,1,0,1) if self.sw_started else (1,0,0,1)
        )
        self.sw_started = not self.sw_started
    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.root.ids.start_stop.color= (0,1,0,1)
            self.sw_started = False
        self.sw_seconds = 0
    def checkbox_click(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")
    
if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    #runTouchApp(CircularButton())
    clockApp().run()