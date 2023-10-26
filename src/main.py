from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from dataPage import DataPage
from graphicPage import GraphicPage

from libs.formulas import Formulas

class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dataPage = DataPage()
        graphicPage = GraphicPage()
        self.add_widget(dataPage)
        self.add_widget(graphicPage)



class QueuesystemApp(App):
    pass

# QueuesystemApp().run()

# testing

input = {
    "Y": 4,
    "arrivalRate": 10,
    "serviceRate": 15,
    "state": 4
}

f = Formulas(input.get("Y"), 
             input.get("arrivalRate"), 
             input.get("serviceRate"), 
             input.get("state"))

for k in range(0, input.get("state") + 1):
    print("P(", k, ") =>", f.getServerLength())
    
    
