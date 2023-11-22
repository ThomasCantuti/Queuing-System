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
from kivy.uix.image import AsyncImage


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
            orientation: "vertical"
            id: system

""")

class DataPage(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color
    pkt_img = AsyncImage(source = "img/pkt.png",
                         size_hint = (None, None),
                         size = (dp(30), dp(30)),
                         pos_hint = {'center_x': 0, 'center_y': 1})
    '''server_img = AsyncImage(source = "img/smartphone.png",
                            size_hint = (None, None),
                            size = (dp(30), dp(30)),
                            pos_hint = {'center_x': 0.5, 'center_y': 0.5})'''
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.system.add_widget(self.pkt_img)
        
        '''for i in range(5):
            server_img = AsyncImage(source = "img/smartphone.png",
                                    size_hint = (None, None),
                                    size = (dp(30), dp(30)),
                                    pos_hint = {'center_x': 0.5, 'center_y': 0.5})
            self.ids.system.add_widget(server_img)
        '''
        self.pkt_img_vx = dp(5)
        #self.pkt_img_vy = dp(5)
        Clock.schedule_interval(self.pkt_move, 1/60)

    def pkt_move (self, dt, *args):
        x, y = self.pkt_img.pos
        x += self.pkt_img_vx
        #y += self.pkt_img_vy
        if self.pkt_img.pos[0] != self.center_x:
            self.pkt_img.pos = (x , y)
        

    '''
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
        #self.pkt_img.pos = (self.center_x - self.pkt_img.size[0] / 2,
        #                    self.center_y - self.pkt_img.size[1] / 2)
    
    
    '''

    def goToGraphic(self):
        self.manager.current = "graphicPage"
        