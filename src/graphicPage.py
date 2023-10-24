from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from styles import Styles

Builder.load_string("""
<GraphicPage>:
    name: "graphicPage"
    BoxLayout:
        orientation: "vertical"
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
                font_name: "robotoblack.ttf"
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
        BoxLayout:
            ScrollView:
                do_scroll_y: True
                Label:
                    id: placeholder
                    color: root.secondary_color
                    text_size: self.width, None
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding: [dp(20), dp(20)]

""")

class GraphicPage(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color

    def goToData(self):
        self.manager.current = "dataPage"