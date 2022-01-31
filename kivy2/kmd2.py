from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
#import audio_player
from plyer import audio
kv=''' 
#:import audio_player plyer.audio
<AudioInterfce>:
	audio:audio_player
	orientation:'vertical'
	padding:'250dp'
	spacing:'28dp'

	MDLabel:
		id:state
		text:'Audio is:'+str(root.audio.state)
		size_hint_y:None
	
	MDLabel:
		id:audio_location
		text:"Audio is saved at - "+str(root.audio.file_path)	
		size_hint_y:None
	MDRectangleFlatButton:
		id:record_button
		text:'Start Record'
		on_release:root.start_recording()
	MDRectangleFlatButton:
		id:play_button
		text:'Play'	
		on_release:root.start_playing()
'''
class AudioInterface(MDBoxLayout):
	audio= ObjectProperty()
	has_recording=False
	def start_recording(self):
		state=self.audio.state 
		if state=='ready':
			self.audio.start()
		if state=='recording':
			self.audio.stop()
			self.has_recording=True
	def start_playing(self):
		state=self.audio.state
		if state=='playing':
			self.audio.stop()
		else:
			self.audio.start()
		self.update_labels()				
	def update_labels(self):
		record_button=self.ids['record_button']
		play_button=self.ids['play_button']
		state_label=self.ids['state']
		state=self.audio.state	
		play_button.disabled=not self.has_recording	 
		state_label.text='AudioPlayer State: '+state
		if state=='ready':
			record_button.text='Start Record'
		if state=='recording':
			record_button.text='Stop Record'
			play_button.disabled=True
		if state=='playing':
			play_button.text='Stop Audio'
			record_button.disabled=True
		else:
			play_button.text='Play Audio'
			record_button.disabled=False	





class AudioApp(MDApp):
	def build(self):
		Builder.load_string(kv)
		return AudioInterface()
		#pass
if __name__=='main_':
	AudioApp().run()