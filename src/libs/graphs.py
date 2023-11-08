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

    def create_A_Ls_Graph(self):
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
        for i in range(0, self.xLength * int(self.formulas.getServiceRate())):
            self.formulas.setArrivalRate(i)
            # print("A:", self.formulas.getTrafficIntensity(), "=> Ls:", self.formulas.getServerLength())
            
            x = self.formulas.getTrafficIntensity()
            y = self.formulas.getServerLength()

            # plt.plot(x, y, 'ro-')
            plt.scatter(x, y, color=Styles.light_1_color)

        plt.title("A - Ls Graph",  fontweight='bold', color=Styles.light_1_color)
        plt.xlabel("A", fontweight='bold', color=Styles.light_2_color)
        plt.ylabel("Ls", fontweight='bold', color=Styles.light_2_color)
        plt.savefig("img/A_Ls_Graph.jpg")
        # plt.show()
        
    def create_A_Ws_Graph(self):
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
        for i in np.arange(1, self.xLength, 0.1):
            self.formulas.setServiceRate(i)
            # print("A:", self.formulas.getTrafficIntensity(), "=> Ls:", self.formulas.getServerLength())
            
            x = self.formulas.getServiceRate()
            y = self.formulas.getServerWait()

            # plt.plot(x, y, 'ro-')
            plt.scatter(x, y, color=Styles.light_1_color)

        plt.title("Mu - Ws Graph",  fontweight='bold', color=Styles.light_1_color)
        plt.xlabel("Mu", fontweight='bold', color=Styles.light_2_color)
        plt.ylabel("Ws", fontweight='bold', color=Styles.light_2_color)
        plt.savefig("img/A_Ws_Graph.jpg")
        # plt.show()
    
    def create_k_Pk_Graph(self):
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
        for k in range(0, self.formulas.getY()):
            # print("A:", self.formulas.getTrafficIntensity(), "=> Ls:", self.formulas.getServerLength())
            
            x = k
            y = self.formulas.getProbabilityAtState(k)

            # plt.plot(x, y, 'ro-')
            plt.scatter(x, y, color=Styles.light_1_color)

        plt.title("k - Pk Graph",  fontweight='bold', color=Styles.light_1_color)
        plt.xlabel("K", fontweight='bold', color=Styles.light_2_color)
        plt.ylabel("Pk", fontweight='bold', color=Styles.light_2_color)
        plt.savefig("img/k_Pk_Graph.jpg")
        # plt.show()
    
    def create_A_Py_Graph(self):
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
        for i in range(0, self.xLength * int(self.formulas.getServiceRate())):
            self.formulas.setArrivalRate(i)
            # print("A:", self.formulas.getTrafficIntensity(), "=> Ls:", self.formulas.getServerLength())
            
            x = self.formulas.getTrafficIntensity()
            y = self.formulas.getProbabilityAtStateY()

            plt.scatter(x, y, color=Styles.light_1_color)

        plt.title("A - Py Graph",  fontweight='bold', color=Styles.light_1_color)
        plt.xlabel("A", fontweight='bold', color=Styles.light_2_color)
        plt.ylabel("Py", fontweight='bold', color=Styles.light_2_color)
        plt.savefig("img/A_Py_Graph.jpg")
        # plt.show()
