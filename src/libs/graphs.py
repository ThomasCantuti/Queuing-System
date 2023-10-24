import matplotlib.pyplot as plt
import numpy as np

class Graphs():
    def __init__(self):
        pass
    
    def getGraph(self):
        x = np.linspace(0.1, 2 * np.pi, 41)
        y = np.sin(x)

        plt.stem(x, y)
        plt.show()