from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from styles import Styles
from libs.formulas import Formulas
from libs.graphs import Graphs
from kivy.uix.image import AsyncImage


Builder.load_string("""
                    
#: import CLabel CustomWidgets
#: import TextParameter CustomWidgets
#: import TitleLabel CustomWidgets
#: import CTextInput CustomWidgets 
                    
<GraphicPage>:
    name: "graphicPage"
    BoxLayout:
        orientation: "vertical"
        # Parte superiore
        BoxLayout:
            canvas.before:
                Color:
                    rgba: root.bg_color
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint_y: None
            height: dp(60)
            Label:
                text: "Queue System M/M/Y/Y Graphic"
                font_name: "DMSans.ttf"
                font_size: "20sp"
            AnchorLayout:
                anchor_x: "right"
                padding: [0,0,dp(30),0]
                Button:
                    canvas.before:
                        Rectangle:
                            pos: self.pos
                            size: self.size
                            source: "img/eye.png"
                    size_hint: None, None
                    size: dp(35), dp(35)
                    background_normal: ""
                    background_color: 0,0,0,0
                    on_press: root.goToData()
        
        # Dati + grafico
        BoxLayout:
            canvas.before:
                Color:
                    rgba: root.bg_color
                Rectangle:
                    pos: self.pos
                    size: self.size
            # Sinistra -> Dati
            BoxLayout:
                orientation: "vertical"
                # input
                BoxLayout:
                    orientation: "vertical"
                    CLabel:
                        text: "Input"
                    BoxLayout:
                        padding: [dp(20), dp(20)]
                        CTextInput:
                            id: arrival
                            hint_text: "lambda"
                        CTextInput:
                            id: mu
                            hint_text: "mu"
                        CTextInput:
                            id: y
                            hint_text: "y"
                        CTextInput:
                            id: state
                            hint_text: "K"
                    BoxLayout:
                        padding: [dp(20), dp(20)]
                        Button:
                            id: start
                            text: "Start"
                            size_hint_y: None
                            height: dp(50)
                            on_press: root.inputStart()
                        Button:
                            id: reset
                            text: "Reset"
                            size_hint_y: None
                            height: dp(50)
                            on_press: root.resetValue()
                # output
                BoxLayout:
                    orientation: "vertical"
                    BoxLayout:
                        CLabel:
                            text: "Output"
                    # Pk
                    BoxLayout:
                        size_hint_x: None
                        TitleLabel:
                            text: "Pk: "
                        TextParameter:
                            id: Pk
                    # Py
                    BoxLayout:
                        size_hint_x: None
                        TitleLabel:
                            text: "Py: "
                        TextParameter:
                            id: Py
                    # Ls
                    BoxLayout:
                        size_hint_x: None
                        TitleLabel:
                            text: "Ls: "
                        TextParameter:
                            id: Ls
                    # Ws
                    BoxLayout:
                        size_hint_x: None
                        width: self.minimum_width
                        TitleLabel:
                            text: "Ws: "
                        TextParameter:
                            id: Ws
            
            # Destra -> Grafico
            BoxLayout:
                id: graph
                anchor_x: "right"
                padding: [0,0,dp(20),0]
                #canvas.before:
                    #Color:
                        #rgba: root.bg_color
                AsyncImage:
                    id: img
                    pos: self.pos
                    size: self.size
                    source: root.image_source.source
            
""")

class GraphicPage(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color
    text_color_1 = Styles.light_1_color
    image_source = AsyncImage()
    image_source.source = "img/testGraph.jpg"

    def inputStart(self):
        self.ids.graph.remove_widget(self.image_source)

        formulas = Formulas(0,0,0,0)
        formulas.arrivalRate = float(self.ids.arrival.text)
        formulas.serviceRate = float(self.ids.mu.text)
        formulas.Y = int(self.ids.y.text)
        formulas.state = int(self.ids.state.text)

        self.ids.Pk.text = str(format(Formulas.getProbabilityAtState(formulas, formulas.state), ".2e"))
        self.ids.Py.text = str(format(Formulas.getProbabilityAtStateY(formulas), ".2e"))
        self.ids.Ls.text = str(round(Formulas.getServerLength(formulas), 2))
        self.ids.Ws.text = str(round(Formulas.getServerWait(formulas), 2))
        
        input ={
            "Y": int(self.ids.y.text),
            "arrivalRate": float(self.ids.arrival.text),
            "serviceRate": float(self.ids.mu.text)
        }
        graph = Graphs(input, 40)
        graph.createGeneralGraph()

        self.image_source.source = "img/testGraph.jpg"
        self.image_source.reload()

    
    def resetValue(self):
        #formulas = Formulas(0,0,0,0)
        self.ids.Pk.text = "0"
        self.ids.Py.text = "0"
        self.ids.Ls.text = "0"
        self.ids.Ws.text = "0"

    def goToData(self):
        self.manager.current = "dataPage"
