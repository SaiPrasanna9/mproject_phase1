import kivy

kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
	
	def build(self):
		# use a (r, g, b, a) tuple
		btn = Button(text ="Push Me !",
				font_size ="20sp",
				background_color =(1, 1, 1, 1),
				color =(1, 1, 1, 1),
				size =(32, 32),
				size_hint =(.2, .2),
				pos =(300, 250))

		# bind() use to bind the button to function callback
		btn.bind(on_press = self.callback)
		return btn

	# callback function tells when button pressed
	def callback(self, event):
		print("button pressed")
		print('Yoooo !!!!!!!!!!!')
		

# creating the object root for ButtonApp() class
root = ButtonApp()

# run function runs the whole program
# i.e run() method which calls the target
# function passed to the constructor.
root.run()
