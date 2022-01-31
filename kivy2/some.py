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

class StackOverFLow(App):
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
    StackOverFLow().run()
Share