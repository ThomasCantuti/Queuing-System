from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from graphicPage import GraphicPage

class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        graphicPage = GraphicPage()
        self.add_widget(graphicPage)
        

class QueuesystemApp(App):
    pass

QueuesystemApp().run()
