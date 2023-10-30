from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from styles import Styles

Builder.load_string("""

<CLabel>:
    font_name: "DMSans.ttf"
    font_size: 26
    color: root.text_color_1
    text_size: self.width, None
    # size_hint_y: None
    anchor_x: "left"
    padding: [dp(20), dp(20)]

<TextParameter>:
    font_name: "DMSans.ttf"
    font_size: 26
    color: root.text_color_1
    text_size: self.width, None
    size_hint_x: None
    size: self.texture_size

<CTextInput>:
    padding: dp(15)
    size_hint_y: None
    height: dp(50)
    multiline: False

""")

class CLabel(Label):
    text_color_1 = Styles.light_1_color

class TextParameter(Label):
    text_color_1 = Styles.light_1_color

class CTextInput(TextInput):
    pass