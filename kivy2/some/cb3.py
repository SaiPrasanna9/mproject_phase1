from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

kv = '''
<RootFloatLayout>:


    Button:
        text: "Ok"
        font_size: 0.4 * self.height
        size_hint: 0.1, 0.08
        pos_hint: {"x": 0.45, "y": 0.05}
        on_press:
            app.press_ok()

    Button:
        text: "Start"
        size_hint: 0.2, 0.2
        pos_hint: { "x": 0.2, "y": 0.6}
        on_press:
            app.in_session()

    Button:
        text: "Stop"
        size_hint: 0.2, 0.2
        pos_hint: { "x": 0.6, "y": 0.6}
        on_press:
            app.stop_function()
    
'''


Builder.load_string(kv)


class RootFloatLayout(FloatLayout):
    mylist={}
    cbs={}
    ans={}
    def okok(self):
        for i in self.cbs:
            if i.active:
                print(self.cbs[i])
                x=self.cbs[i]
                print(self.mylist[x])
    def some1(self):
        self.mylist[0]="apple"
        self.mylist[1]="banana"
        self.mylist[2]="mango"
        #self.mylist[3]="papaya"
        #self.mylist[4]="orange"

        self.layout = GridLayout(cols=2)
            #self.layout=FloatLayout()
        for i in self.mylist:
            self.layout.add_widget(Label(text =str(i)+" " +self.mylist[i],color = (1,0,1,1),font_size="25dp"))
            x = CheckBox(active = False,color=(1,0,1,1),width="230")
            self.cbs[x]=i #self.mylist[i]
            self.layout.add_widget(x)
        self.add_widget(self.layout)

class ReminderApp(App):

    def build(self):
        self.root_layout = RootFloatLayout()
        return self.root_layout
    def press_ok(self):
        self.root.okok()
    
    def in_session(self):
        self.root.some1()
        

    def stop_function(self):
        self.root.some2()

if __name__ == '__main__':
    ReminderApp().run()
