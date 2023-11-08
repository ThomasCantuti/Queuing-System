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
                        CTextInput:
                            id: xLength
                            hint_text: "xLength"
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
                    BoxLayout:
                        padding: [dp(20), dp(20)]
                        Button:
                            id: toggle
                            text: "Switch graph"
                            size_hint_y: None
                            height: dp(50)
                            on_press: root.switchGraph()

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
                AsyncImage:
                    pos: self.pos
                    size: self.size
                    source: root.image_source.source
            
""")

class GraphicPage(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color
    text_color_1 = Styles.light_1_color
    image_source = AsyncImage()
    image_source.source = "img/A_Ls_Graph.jpg"
    count_switch = 0

    def inputStart(self):
        self.count_switch = 0
        self.ids.graph.remove_widget(self.image_source)

        formulas = Formulas(0,0,0,0)
        formulas.arrivalRate = float(self.ids.arrival.text)
        formulas.serviceRate = float(self.ids.mu.text)
        formulas.Y = int(self.ids.y.text)
        formulas.state = int(self.ids.state.text)

        self.ids.Pk.text = str(round(Formulas.getProbabilityAtState(formulas, formulas.state), 4))
        self.ids.Py.text = str(format(Formulas.getProbabilityAtStateY(formulas), ".2e"))
        self.ids.Ls.text = str(round(Formulas.getServerLength(formulas), 2))
        self.ids.Ws.text = str(round(Formulas.getServerWait(formulas), 2))
        
        input ={
            "Y": int(self.ids.y.text),
            "arrivalRate": float(self.ids.arrival.text),
            "serviceRate": float(self.ids.mu.text),
            "state": int(self.ids.state.text)
        }

        graph_A_Ls = Graphs(input, int(self.ids.xLength.text))
        graph_A_Ls.create_A_Ls_Graph()

        graph_k_Pk = Graphs(input, int(self.ids.xLength.text))
        graph_k_Pk.create_k_Pk_Graph()

        graph_A_Ws = Graphs(input, int(self.ids.xLength.text))
        graph_A_Ws.create_A_Ws_Graph()

        graph_A_Py = Graphs(input, int(self.ids.xLength.text))
        graph_A_Py.create_A_Py_Graph()

        self.switchGraph()

    
    def resetValue(self):
        formulas = Formulas(0,0,0,0)
        self.ids.arrival.text = ""
        self.ids.mu.text = ""
        self.ids.y.text = ""
        self.ids.state.text = ""
        self.ids.xLength.text = ""
        self.ids.Pk.text = "0"
        self.ids.Py.text = "0"
        self.ids.Ls.text = "0"
        self.ids.Ws.text = "0"
    
    def switchGraph(self):

        if self.count_switch == 0:
            self.image_source.source = "img/A_Ls_Graph.jpg"
            self.image_source.reload()
            self.count_switch += 1
            
        elif self.count_switch == 1:
            self.image_source.source = "img/k_Pk_Graph.jpg"
            self.image_source.reload()
            self.count_switch += 1
        
        elif self.count_switch == 2:
            self.image_source.source = "img/A_Ws_Graph.jpg"
            self.image_source.reload()
            self.count_switch += 1
        
        elif self.count_switch == 3:
            self.image_source.source = "img/A_Py_Graph.jpg"
            self.image_source.reload()
            self.count_switch = 0


    def goToData(self):
        self.manager.current = "dataPage"
