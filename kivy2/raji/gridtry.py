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
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
class clockApp(App):
    
    def hy(self):
        #super(check_box, self).__init__(**kwargs)
        #layout= GridLayout(cols=2, padding=10)
        #self.cols = 2
        self.layout = GridLayout(cols=2)
        # Add checkbox, widget and labels
        self.layout.add_widget(Label(text ='Male',color = (0,0,0,1),font_size="25dp"))
        self.active = CheckBox(active = False,color=(0,0,0,1),width="230")
        self.layout.add_widget(self.active)
       
        self.layout.add_widget(Label(text ='Female',color = (0,0,0,1),font_size="25dp"))
        self.active = CheckBox(active = False,color=(0,0,0,1),width="230")
        self.layout.add_widget(self.active)
 
        self.layout.add_widget(Label(text ='Other',color = (0,0,0,1),font_size="25dp"))
        self.active = CheckBox(active = False, color=(0,0,0,1),width="230")
        self.layout.add_widget(self.active)
        self.root.add_widget(self.layout)
if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    #runTouchApp(CircularButton())
    clockApp().run()