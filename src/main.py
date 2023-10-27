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
        self.add_widget(graphicPage)
        self.add_widget(dataPage)

class QueuesystemApp(App):
    pass

QueuesystemApp().run()

'''

# testing

def runSimulation(Y: int, arrivalRate: float, serviceRate: float):
    input = {
        "Y": Y,
        "arrivalRate": arrivalRate,
        "serviceRate": serviceRate
    }

    formulas = Formulas(input.get("Y"), 
                input.get("arrivalRate"), 
                input.get("serviceRate"))
    

# SAMPLE GRAPH
# for i in range(0, 10 * f.getServiceRate()):
#     f.setArrivalRate(i)
#     print("A:", f.getTrafficIntensity(), "=> Ls:", f.getServerLength())
    
#     x = f.getTrafficIntensity()
#     y = f.getServerLength()

#     plt.plot(x, y, 'ro-')

# plt.title("General Graph")
# plt.xlabel("A")
# plt.ylabel("Ls")
# plt.savefig("img/testGraph.jpg")
# plt.show()
'''