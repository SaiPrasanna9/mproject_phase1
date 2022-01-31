from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBLayout
from kivy.properties import ObjectProperty
kv='''
#: import audio_player plyer.audio
<AudioInterface>:
	audio: audio_player
	orientation: 'vertical'

	MDLabel:
		id: state
		text: 'Audio is': +str(root.audio.state)
	MDLabel:
		id: audio_location
		text: "Audio is saved at - "+str(root.audio.file_path)

	MDRectangleFlatButton:
		id: record_button
		text:'START RECORD'
		on_release:root.start_recording()

	MDRectangleFlatButton:
	id: play_button
	text: 'PLAY'
	on_release:root.start_playing()
'''


class AudioInterface(MDBoxLayout):
	audio = ObjectProperty()
	has_recording=True
	def start_recording(self):
		state=self.audio.state
		if state=='ready':
			self.audio.start()
		if state=='recording':
			self.audio.stop()
			self.has_recording=True

	def start_playing(self):
		state= self.audio.state
		if state=='playing':
			self.audio.stop()
		else:
			self.audio.stop()

	def update_labels(self):
		record_button=self.ids['record_button']
		play_button=self.ids['play_button']
		state_label=self.ids['state']
		
		state=self.audio.state
		play_button.disabled=not self.has_recording
		

		state_label.text='AudioPlayer State:'+ state
		
		if state=='ready':
			record_button.text='START RECORD'
			
		if state=='recording':
			record_button.text='STOP RECORD'
			play_button.disabled=True

		if state=='playing':
			play_button.text='STOP AUDIO'
		else:
			play_button.text='STOP AUDIO'
			record_button.disabled=False
		


class AudioApp(MDApp)	
	def build(self):
		pass





if __name__ == '__main__':
	AudioApp.run()

	