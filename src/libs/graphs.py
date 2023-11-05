import matplotlib.pyplot as plt
import numpy as np

from libs.formulas import Formulas
from styles import Styles

class Graphs():
    def __init__(self, input, xLength):        
        self.formulas = Formulas(input.get("Y"), 
                            input.get("arrivalRate"), 
                            input.get("serviceRate"))
        
        self.xLength = xLength

        
    def getXLength(self):
        return self.xLength
    
    def setXLength(self, xLength):
        self.xLength = xLength

    def createGeneralGraph(self):
        # graph surrounding bg color
        plt.figure(facecolor=Styles.secondary_color)

        ax = plt.axes()

        # graph bg color
        ax.set_facecolor(Styles.secondary_color)

        # graph axis values color
        ax.tick_params(axis='x', colors=Styles.light_2_color)
        ax.tick_params(axis='y', colors=Styles.light_2_color)

        # graph borders color
        for i in ['bottom', 'top', 'left' , 'right']:
            ax.spines[i].set_color(Styles.light_2_color)

        # display points
        for i in range(0, self.xLength * self.formulas.getServiceRate()):
            self.formulas.setArrivalRate(i)
            # print("A:", self.formulas.getTrafficIntensity(), "=> Ls:", self.formulas.getServerLength())
            
            x = self.formulas.getTrafficIntensity()
            y = self.formulas.getServerLength()

            # plt.plot(x, y, 'ro-')
            plt.scatter(x, y, color=Styles.light_1_color)

        plt.title("General Graph",  fontweight='bold', color=Styles.light_1_color)
        plt.xlabel("A", fontweight='bold', color=Styles.light_2_color)
        plt.ylabel("Ls", fontweight='bold', color=Styles.light_2_color)
        plt.savefig("img/testGraph.jpg")
        #plt.show()
