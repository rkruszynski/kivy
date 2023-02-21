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

    word = StringProperty("foo")

    def clicked(self):
        print("udalo sie")

    def get_random_int(self):
        return str(randint(1, 20))

    def get_random_word(self):
        # with open("word.txt", "w") as last_word:
        #     word = words.return_random_word()
        #     last_word.write(word)
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
    # def build(self):
    #     content = words.set_difficulty('r', "Wysoki", "6")
    #     words.save_file('w', content)
    #     word = words.return_random_word()
    #     return Label(text=word)

    def get_spanish_translation(self, word):
        return words.return_spain_translation(word)

    # def get_random_int(self):
    #     from random import randint
    #     return randint(1, 20)

    def get_random_word(self):
        return words.return_random_word()

MyFlashcardApp().run()
