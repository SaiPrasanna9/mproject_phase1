# Resize the Window - Non Pep8 Compliant, mandated by Kivy


from cal_setup import get_calendar_service
import datetime as dateTime
from datetime import datetime, timedelta

import speech_recognition as sr
import pyttsx3

import spacy
#import multiprocessing

nlp = spacy.load('en_core_web_sm')

from dateutil.parser import parse

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '200')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

def detect_past_sentence(sentence):
    sent = sentence
    return (sent.root.tag_ == "VBD" or
                            any(w.dep_ == "aux" and w.tag_ == "VBD" for w in sent.root.children))

def getweek(week):
    if (week == 'sunday'):
        return 6
    elif (week == 'monday'):
        return 0
    elif (week == 'tuesday'):
        return 1
    elif (week == 'wednesday'):
        return 2
    elif (week == 'thursday'):
        return 3
    elif (week == 'friday'):
        return 4
    elif (week == 'saturday'):
        return 5

# Root Widget
class Root(BoxLayout):
    pass


class RecordButton(Button):
    sw_started= False
    sw_seconds = 0
    # String Property to Hold output for publishing by Textinput
    output = StringProperty('')
    def update_time(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        self.ids.stopwatch.text = (
            '%02d:%02d.[size=20]%02d[/size]'%
            (int(minutes), int(seconds),
             int(seconds* 100 % 100))
        )
        self.ids.stopwatch.color=(0,0,1,1)
        self.ids.time.text = strftime('[b]%H[/b]:%M:%S')
        self.ids.time.color=(1,0,1,1)
    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)

    
    
    
    def start_stop(self):
        self.text =(
            'Start' if self.sw_started else 'Stop'
        )
        self.background_color =(
            (0,1,0,1) if self.sw_started else (1,0,0,1)
        )

        self.sw_started = not self.sw_started
        '''self.root.ids.start_stop.text =(
            'Start' if self.sw_started else 'Stop'
        )
        self.root.ids.start_stop.background_color =(
            (0,1,0,1) if self.sw_started else (1,0,0,1)
        )

        self.sw_started = not self.sw_started
        if(self.root.ids.start_stop.text =='Start'):'''


    def record(self):
        
        self.start_stop()
        # GUI Blocking Audio Capture
        if(self.text=='Start'):
            print("dckdmcdmdfndfnv fdnvj")
            with m as source:
                audio = r.listen(source)
                print("here4 listening")
            
            try:
                # recognize speech using Google Speech Recognition
                print('fomde here')
                value = r.recognize_google(audio)
                MyText=value
                print("here5 recognized")
                MyText = MyText.lower()
                example=MyText
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
                    rem_list = {}
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
                                rem_list[key1] = value
                            else:
                                rem_list[key] = value
                some=" "
                for i in rem_list:
                    some=some+i+" ---- "+rem_list[i]
                print("some ",some)
                self.output=some

                #self.output = "You said \"{}\"".format(value)

                r_list=[]
                for rem in rem_list.keys():
                    a=rem_list[rem]
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


                
            
            except sr.UnknownValueError:
                self.output = ("Oops! Didn't catch that")
            
            except sr.RequestError as e:
                self.output = ("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))


class SpeechApp(App):
    def build(self):
        # Calibrate the Microphone to Silent Levels
        print("A moment of silence, please...")
        print("here2")
        with m as source:
            r.adjust_for_ambient_noise(source)
            #print("Set minimum energy threshold to {}".format(r.energy_threshold))
            print("here3")
        # Create a root widget object and return as root
        return Root()


# When Executed from the command line (not imported as module), create a new SpeechApp
if __name__ == '__main__':
    print("here1")
    SpeechApp().run()


