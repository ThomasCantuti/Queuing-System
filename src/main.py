from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from dataPage import DataPage
from graphicPage import GraphicPage

import matplotlib.pyplot as plt
import numpy as np

# from formulas import Formulas
# from graphs import Graphs

class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dataPage = DataPage()
        graphicPage = GraphicPage()
        self.add_widget(dataPage)
        self.add_widget(graphicPage)



class QueuesystemApp(App):
    pass

QueuesystemApp().run()