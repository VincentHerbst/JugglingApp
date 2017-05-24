from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget 
from kivy.graphics import Line 
from kivy.core.text import Label as CoreLabel


from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

from kivy.uix.scrollview import ScrollView
from kivy.graphics.instructions import InstructionGroup
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from kivy.uix.popup import Popup

#class Window(Window):
#    pass

class CustomPopup(Popup):
    pass

class ScrollableLabel(ScrollView):
    pass

class Cascade(Screen):
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

class MainScreen(Screen):
    pass


class Tricks(Screen):
    pass


class Progress(Screen):
    pass


class Materials(Screen):
    pass

class Blog(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("jonglier.kv")

class JonglierApp(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    JonglierApp().run()

