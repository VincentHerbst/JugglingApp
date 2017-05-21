from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget 
from kivy.graphics import Line 

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

