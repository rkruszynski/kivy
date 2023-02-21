from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
import words
from random import randint

class BoxLayoutMain(BoxLayout):

    word = StringProperty("Hello!")

    def clicked(self):
        print("udalo sie")

    def get_random_int(self):
        # Just for debuging purposes
        return str(randint(1, 20))

    def get_random_word(self):
        word = words.return_random_word()
        self.word = word
        return word


class BoxLayoutTop(BoxLayout):

    pass

class BoxLayoutBottom(BoxLayout):
    pass


class MainWidged(Widget):
    pass

class MyFlashcardApp(App):
    pass

MyFlashcardApp().run()
