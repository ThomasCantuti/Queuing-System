import matplotlib.pyplot as plt
import numpy as np

from formulas import Formulas

class Graphs():
    def __init__(self):
        pass

    def drawGraph(self):

        input = {
            "Y": 4,
            "arrivalRate": 10,
            "serviceRate": 50,
            "state": 4
        }

        f = Formulas(input.get("Y"), 
             input.get("arrivalRate"), 
             input.get("serviceRate"), 
             input.get("state"))
        
        for i in range(0, 10 * f.getServiceRate()):
            f.setArrivalRate(i)
            print("A:", f.getTrafficIntensity(), "=> Ls:", f.getServerLength())
            
            x = f.getTrafficIntensity()
            y = f.getServerLength()

            plt.plot(x, y, 'ro-')

        plt.title("General Graph")
        plt.xlabel("A")
        plt.ylabel("Ls")
        plt.savefig("img/testGraph.jpg")
        plt.show()
