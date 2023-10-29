from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from styles import Styles
from libs.formulas import Formulas

Builder.load_string("""
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
                            source: "back.png"
                    size_hint: None, None
                    size: dp(35), dp(35)
                    background_normal: ""
                    background_color: 0,0,0,0
                    on_press: root.goToData()
        
        # Sinistra -> Dati
        BoxLayout:
            canvas.before:
                Color:
                    rgba: root.bg_color
                Rectangle:
                    pos: self.pos
                    size: self.size
            BoxLayout:
                anchor_x: "left"
                anchor_y: "top"
                padding: [dp(30),0,0,0]
                orientation: "vertical"
                # input
                BoxLayout:
                    anchor_y: "top"
                    pos_hint: {'x' : 0, 'y' : 1}
                    Label:
                        font_name: "DMSans.ttf"
                        font_size: 26
                        color: root.text_color_1
                        text_size: self.width, None
                        anchor_x: "left"
                        #padding: [dp(20), dp(20)]
                        text: "Input"
                    TextInput:
                        id: lambda
                        padding: dp(15)
                        size_hint_y: None
                        height: dp(50)
                        multiline: False
                        hint_text: "lambda"
                    TextInput:
                        id: mu
                        padding: dp(15)
                        size_hint_y: None
                        height: dp(50)
                        multiline: False
                        hint_text: "mu"
                    TextInput:
                        id: y
                        padding: dp(15)
                        size_hint_y: None
                        height: dp(50)
                        multiline: False
                        hint_text: "y"
                    Button:
                        id: start
                        text: "Start"
                        size_hint_y: None
                        height: dp(50)

                # output
                BoxLayout:
                    anchor_y: "top"
                    pos_hint: {'x' : 0, 'y' : 1}
                    Label:
                        font_name: "DMSans.ttf"
                        font_size: 26
                        color: root.text_color_1
                        text_size: self.width, None
                        anchor_x: "left"
                        anchor_y: "top"
                        size_hint_y: None
                        #padding: [dp(20), dp(20)]
                        text: "Output"
            
            # Destra -> Grafico
            AnchorLayout:
                anchor_x: "right"
                #padding: [0,0,dp(30),0]
                canvas.before:
                    #Color:
                    #    rgba: root.bg_color
                    Rectangle:
                        pos: self.pos
                        size: self.size
                        source: "img/testGraph.jpg"
            
                
                    

""")

class GraphicPage(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color
    text_color_1 = Styles.light_1_color


    def goToData(self):
        self.manager.current = "dataPage"
