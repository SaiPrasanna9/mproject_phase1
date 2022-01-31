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

import random
import datetime as dateTime
from datetime import datetime, timedelta


from cal_setup import get_calendar_service
#import datetime as dateTime
#from datetime import datetime, timedelta

import speech_recognition as sr
import pyttsx3

import spacy
#import multiprocessing



from dateutil.parser import parse


nlp = spacy.load('en_core_web_sm')
r = sr.Recognizer()
m = sr.Microphone()



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

    #label_string = StringProperty('Hello World!')
    #some=''
    value=''
    rem_list={}

    mylist={}
    cbs={}
    ans={}
    selected_rem_list={}


    def record(self):
        # GUI Blocking Audio Capture
        with m as source:
            self.audio = r.listen(source)
            print("here4 listening")
        try:
            self.value =self.value +'. '+ r.recognize_google(self.audio)
            print("llllllllllllllllllll"*30,self.value,"llllllllll"*30)
        except Exception as e:
            print("some error",e)
        #self.come(audio)
    def rstart(self):
        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(r.energy_threshold))  


    def play_tech(self):
        # this is my way of randomizing ,
        #  make one that matches your liking by studying the random() built in Class
        #  or make your own !
        sounds = ['Ding Dong','Bird Chirp','Buzzz','Whistle']
        if random.randint(1,200) == 2:
            #self.label_string = "Sound: "+sounds[random.randint(0,3)]
            self.rstart()
            #Clock.schedule_interval(self.update_time, 0)
            self.record()
        if(self.some=='Started'):
            self.rstart()
            #Clock.schedule_interval(self.update_time, 0)
            self.record()

        
    def on_session_begin(self,dt):
        # place all the activities you want to run when on_session() method is called here
        self.rstart()
        self.record()

        # to stop the event when the on_session() method has done its job,
        # return False  
    def come(self):
        try:
            # recognize speech using Google Speech Recognition
            #print("google recognize")
            #value = r.recognize_google(self.audio)
            MyText=self.value
            print("here5 recognized")
            MyText = MyText.lower()
            example=MyText
            print("examople",example)
            if True:
                #request.method=='POST':
                #result = request.form

                #example = result['message']
                
                # example = "Hey Snigdha, how are you? It's been a long time. Yeah I am good. How is everything at your place ? Yeah everything's fine. All of our friends are planning something. Will it be possible for you to attend a get-together on 4 October?. Oh yes. I will definetly come. When does it start? The meet starts at 10 AM. Please come along with your family. Yeah sure. See you there. Alright bye"
                # example = "Hello doctor. Hello. Take a seat. Tell me what your problem is. I have been suffering from fever for the past 2 days. Okay, let me check your temperature. It's 103 degrees. You have high fever. Take this medicine at 2 PM today. If the fever does not subdue, take a corona test tomorrow. Meet me at 3 PM this wednesday."
                sen_doc = nlp(example)
                print("here6 after nlp")
                sentences = list(sen_doc.sents)
                # print(sentences)
                present_perfect=['had been','have been','has been']
                self.rem_list = {}
                for sentence in sentences:
                    #print(sentence,sentence.ents)
                    pp = False
                    for i in present_perfect:
                        #print(sentence,str(sentence).find(i),i)
                        if str(sentence).find(i)!=-1:
                            pp = True
                            break
                    print("before dtect past sentence")
                    if pp:
                        continue
                    sent = sentence
                    strue= (sent.root.tag_ == "VBD" or
                            any(w.dep_ == "aux" and w.tag_ == "VBD" for w in sent.root.children))
                    if strue == True :
                        continue
                    print("after detect")
                    date = False
                    time = False
                    ent1 = ""
                    ent2 = ""
                    list1 = []
                    list2 = []
                    pobj=''
                    notpobj = ['AM','PM','am','pm','January','january','February','february','March','march','April','april','May','may','June','june','July','july','August','august','September','september','October','october','November','november','December','december']
                    words = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
                    rem = {'appointment': 'Your appointment at', 'meet': 'Your meeting at ', 'meeting': 'Your meeting at',
                           'medicine': 'Take medicines at', 'medicines': 'Take medicines at', 'come': 'Your Meeting at','tablet': 'Take medicines at',
                           'party' : 'Attend Party at', }
                    for ent in sentence.ents:

                        #print(ent.text,ent.label_)
                        if ent.label_ == "DATE":
                            date_words = ent.text.split(" ")
                            print(ent.text)
                            if (ent.text.casefold() == 'today'):
                                list1.append(str(dateTime.date.today()))
                            elif (ent.text .casefold() == 'tomorrow'):
                                list1.append(str(dateTime.date.today() + dateTime.timedelta(days=1)))
                            elif ((date_words[0].casefold() == 'this') and date_words[1] in words):
                                n = int(dateTime.datetime.today().weekday())
                                week=date_words[1]
                                wee=0
                                if (week == 'sunday'):
                                    wee =6
                                elif (week == 'monday'):
                                    wee =0
                                elif (week == 'tuesday'):
                                    wee =1
                                elif (week == 'wednesday'):
                                    wee= 2
                                elif (week == 'thursday'):
                                    wee =3
                                elif (week == 'friday'):
                                    wee= 4
                                elif (week == 'saturday'):
                                    wee= 5



                                #w = int(getweek(date_words[1]))
                                w=wee
                                list1.append(str(dateTime.date.today() + dateTime.timedelta(days=w - n)))
                            elif (date_words[0].casefold() == 'next' and date_words[1] in words):
                                num = 6 - int(dateTime.datetime.today().weekday())

                                week=date_words[1]
                                wee=0
                                if (week == 'sunday'):
                                    wee =6
                                elif (week == 'monday'):
                                    wee =0
                                elif (week == 'tuesday'):
                                    wee =1
                                elif (week == 'wednesday'):
                                    wee= 2
                                elif (week == 'thursday'):
                                    wee =3
                                elif (week == 'friday'):
                                    wee= 4
                                elif (week == 'saturday'):
                                    wee= 5

                                num = num + wee + 1
                                list1.append(str(dateTime.date.today() + dateTime.timedelta(days=num)))
                            elif (date_words[0] in words):
                                n = int(dateTime.datetime.today().weekday())

                                week=date_words[0]
                                wee=0
                                if (week == 'sunday'):
                                    wee =6
                                elif (week == 'monday'):
                                    wee =0
                                elif (week == 'tuesday'):
                                    wee =1
                                elif (week == 'wednesday'):
                                    wee= 2
                                elif (week == 'thursday'):
                                    wee =3
                                elif (week == 'friday'):
                                    wee= 4
                                elif (week == 'saturday'):
                                    wee= 5
                                w = wee
                                list1.append(str(dateTime.date.today() + dateTime.timedelta(days=w - n)))
                            else:
                                list1.append(ent.text)
                            #print(ent.text)
                            ent1 = ent.text
                            date = True
                            print("here some")
                        if ent.label_ == "TIME":
                            list1.append(ent.text)
                            ent2 = ent.text
                            time = True
                    if date or time:
                        for token in sentence:
                            if token.dep_ == "ROOT" or token.dep_ == 'dobj' or token.dep_ == 'pobj' or token.dep_ == 'compound' or token.dep_ == 'nsubjpass':
                                if (token.dep_=='pobj' or token.dep_ == 'compound') and (token.text not in notpobj):
                                    pobj=pobj+' '+token.text

                                if token.dep_ != 'pobj':
                                    list2.append(token.text)

                                #print(token.text,":",ent1,ent2)
                            #print (token.text, token.tag_, token.head.text, token.dep_)
                    if len(list1) > 0 and len(list2) > 0:
                        key = ' '.join(list2)
                        key1=''
                        flag = False
                        words_in_key = key.split(" ")
                        for word in words_in_key:
                            #print(word)
                            if word.casefold() in rem:
                                flag = True
                                key1 = rem[word.casefold()]+' '+str(pobj)
                                break
                        value = ' '.join(list1)
                        #print(key1)
                        if flag:
                            self.rem_list[key1] = value
                        else:
                            self.rem_list[key] = value
            some=" "
            for i in self.rem_list:
                some=some+i+" ---- "+self.rem_list[i]
            self.layout = GridLayout(cols=2)
            #self.layout=FloatLayout()

            for i in (self.rem_list):
                #self.add_widget(Label(text =i+" :: "+rem_list[i],color = (1,0,1,1)))#root
                #self.active = CheckBox(active = False)
                #self.add_widget(self.active)#root

                self.layout.add_widget(Label(text =i +" :: "+self.rem_list[i],color = (1,0,1,1),font_size="25dp"))
                #self.active = CheckBox(active = False,color=(1,0,1,1),width="230")
                x = CheckBox(active = False,color=(1,0,1,1),width="230")
                self.cbs[x]=i

                self.layout.add_widget(x)
            self.add_widget(self.layout)

     
        except sr.UnknownValueError:
            self.output = ("Oops! Didn't catch that")
        
        except sr.RequestError as e:
            self.output = ("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

    def okok(self):
        for i in self.cbs:
            if i.active:
                print(self.cbs[i])
                x=self.cbs[i]
                print(self.rem_list[x])
                self.selected_rem_list[x]=self.rem_list[x]
        print("*selected list of reminers *"*50,self.selected_rem_list)
        for rem in self.rem_list.keys():
            a=self.rem_list[rem]
            try:
                add_date=parse(a, fuzzy_with_tokens=True)
                add_date=add_date[0]
                print("adding remainder to calendar")
                #add_rem([rem,add_date])

                d=add_date
                service = get_calendar_service()
                #d = datetime.now().date()
                tomorrow = datetime(d.year, d.month, d.day, d.hour,d.minute)
                start = tomorrow.isoformat()
                end = (tomorrow + timedelta(hours=1)).isoformat()
                event_result = service.events().insert(calendarId='primary',body={
                "summary": rem,
                        "description": rem,
                        "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
                        "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
                        }).execute()
                print("created event")
                print("id: ", event_result['id'])
                print("summary: ", event_result['summary'])
                print("starts at: ", event_result['start']['dateTime'])
                print("ends at: ", event_result['end']['dateTime'])

                print("added remainder in calendar")
            except Exception as e:
                print("unable to parse the generated reminder date {0}".format(a))



    def process_act(self,rem_list):
        #super(check_box, self).__init__(**kwargs)
        #layout= GridLayout(cols=2,padding=10)
        #self.cols = 2
 
        # Add checkbox, widget and labels
        for i in range(len(rem_list)):
            self.add_widget(Label(text =i+" :: "+rem_list[i],color = (1,0,1,1)))#root
            self.active = CheckBox(active = False,id=i)
            self.add_widget(self.active)#root
    def on_OK(self):
        for i in self.rem_list:
            if(self.ids.i.active):
                print(i,"*"*100)
    def onButtonPress(self):
        
        layout = GridLayout(cols = 1, padding = 10)
        #tkWindow = Tk()
        popupLabel = Button(text = "Process",font_size=20)
        closeButton = Button(text = "Cancel",font_size=20)
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)  

        # Instantiate the modal popup and display
        popup = Popup(title ='Processing',
                    content = layout,
                    size_hint =(None, None), size =(200, 200))
        popup.open()
        #popupLabel.bind(on_press=lambda x:self.reset())
        popupLabel.bind(on_press=lambda x:self.come())
        #popupLabel.bind(on_press=lambda x:self.process_act(rem_list))
        popupLabel.bind(on_press=popup.dismiss)
        #popupLabel.bind(on_press=clockApp().run())

        # Attach close button press with popup.dismiss action
        #closeButton.bind(on_press=lambda x:self.reset())
        closeButton.bind(on_press = popup.dismiss)                

class ReminderApp(App):
    def build(self):
        self.root_layout = RootFloatLayout()
        return self.root_layout

    def press_ok(self):
        self.root.okok()
    
    def in_session(self):
        # creates a Clock based event that runs the on_session_begin () once (1) every 60 seconds
        #self.root_layout.label_string = "Session is on!"
        self.some='Started'
        self.value=''
        #self.event = Clock.schedule_interval(self.root.on_session_begin, 1./60.)
        self.event = Clock.schedule_interval(self.root.on_session_begin, 1./60.)
        

    def stop_function(self):
        # stops calling the on_session_begin() method, even midway
        #self.root_layout.label_string = "Stopped!"
        #self.some='Stopped'

        self.event.cancel()
        self.root.onButtonPress()

if __name__ == '__main__':
    ReminderApp().run()