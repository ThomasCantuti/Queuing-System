from kivy.uix.scatter import Scatter
from kivy.graphics import Color, Line
from libs.formulas import Formulas
from libs.graphs import Graphs
import math

class GraphWidget (Scatter):
    def __init__(self, **kwargs):
        super(GraphWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, 1)  # Imposta il colore del grafico
            #graph = Graphs(100)
            #graph.createGeneralGraph()

            # ascisse
            Line(points=[0, 0, 200, 0])
            # ordinate
            Line(points=[0, 0, 0, 200])

            # Disegna il grafico
            for x in range(0, 200):
                y = math.sin(x / 10.) * 50 + 100
                Line(points=[x, y, x + 1, y])