from kivy.app import App
from kivy.config import Config
from kivy.core.text import LabelBase


class RecorderApp(App):
    pass


if __name__ == '__main__':
    Config.set('graphics', 'width', 960)
    Config.set('graphics', 'height', 540)
    LabelBase.register('Modern Pictograms', fn_regular='modernpics.ttf')

    RecorderApp().run()
