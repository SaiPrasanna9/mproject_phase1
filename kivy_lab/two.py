import kivy   
from kivy.app import App   
from kivy.uix.button import Button #import Button  
kivy.require("1.9.1")   
   
class kivyButtonApp(App):   
        
    def build(self):   
            
        btn = Button(text = "Press Me!", size_hint = (.2,.2), pos = (300,250))   
        return btn   
      
    
root = kivyButtonApp()   
root.run()