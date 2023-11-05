from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from dataPage import DataPage
from graphicPage import GraphicPage

import matplotlib.pyplot as plt
import numpy as np

from libs.formulas import Formulas
from libs.graphs import Graphs
from styles import Styles

class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dataPage = DataPage()
        graphicPage = GraphicPage()
        self.add_widget(graphicPage)
        self.add_widget(dataPage)

class QueuesystemApp(App):
    pass

# QueuesystemApp().run()

# graficone

input = {
    "Y": 5,
    "arrivalRate": 8,
    "serviceRate": 18
}

graphs = Graphs(input, 40)
graphs.createGeneralGraph()

# input ={
#     "Y": self.ids.Y
# }
