from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from styles import Styles
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.properties import Clock
from kivy.metrics import dp
from kivy.uix.image import AsyncImage
from kivy.animation import Animation

Builder.load_string("""
<DataPage>:
    name: "dataPage"
    BoxLayout:
        orientation: "vertical"
        # parte superiore
        BoxLayout:
            canvas.before:
                Color:
                    rgba: root.bg_color
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint_y: None
            height: dp(60)
            AnchorLayout:
                anchor_x: "left"
                padding: [dp(30),0,0,0]
                Label:
                    text: "Tecnical Data"
                    font_name: "robotoblack.ttf"
                    font_size: "20sp"
                    halign: "center"
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
                    on_press: root.goToGraphic()
        
        # parte inferiore
        BoxLayout:
            ScrollView:
                do_scroll_y: True
                Button:
                    size_hint: None, None
                    size: 100, 50
                    text: "ciao"
                    on_press: root.on_click()

""")

class DataPage(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rect_size = dp(50)
        self.pipe_size = dp(50)
        with self.canvas:
            Color(0,1,0,1)
            self.pipe = Line(points = [self.x, self.center_y, self.right, self.center_y], width = 3)
            #Line(circle = (400,200,80), width = 2)
            #Line(rectangle = (700,500,150,100), width = 2)
            #self.rect = Rectangle(pos = self.center, size = (150, 100))
        #Clock.schedule_interval(self.update, 1)
    
    def on_click (self):
        #x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)

        diff = self.width - (x + w)
        if diff < inc:
            inc = diff

        x += inc
        #self.rect.pos = (x, y)
    
    def on_size (self, *args):
        #self.rect.pos = (self.center_x - self.rect_size / 2,
        #                 self.center_y - self.rect_size / 2)
        self.pipe.points = (self.x, 
                            self.center_y - self.pipe_size / 2,
                            self.right / 2, 
                            self.center_y - self.pipe_size / 2)
    
    def update (self, dt):
        #x, y = self.rect.pos
        #self.rect.pos = (x + 10, y)
        pass

    def goToGraphic(self):
        self.manager.current = "graphicPage"
        