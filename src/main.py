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

input = {
    "Y": 20,
    "arrivalRate": 8,
    "serviceRate": 18,
}

g = Graphs(input, 10)

# g.create_A_Ls_Graph()
# g.create_A_Ws_Graph()
# g.create_k_Pk_Graph()
g.create_A_Py_Graph()
