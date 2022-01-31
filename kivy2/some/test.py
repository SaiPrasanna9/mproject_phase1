from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

class TestApp(App):
    def build(self):
        root = FloatLayout()
        layout = BoxLayout(orientation='vertical', size=(50,50), size_hint=(0.5, 0.5))
        btn1 = Button(text='Hello', size=(100,50), size_hint=(None, None))
        btn2 = Button(text='World', size=(50,50), size_hint=(None, None))
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        root.add_widget(layout)
        return root
TestApp().run()