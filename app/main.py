from kivymd.app import MDApp
from kivy.properties import NumericProperty
from kivy.graphics import Color, Rectangle
from kivy.core.clipboard import Clipboard
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton





class ColorMixerApp(MDApp):
    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(0)

    def build(self):
        self.color_rect = None
        self.init_color_preview()
        return self.root

    def init_color_preview(self):
        preview = self.root.ids.color_preview
        with preview.canvas:
            self.color_instruction = Color(0, 0, 0, 1)
            self.color_rect = Rectangle(pos=preview.pos, size=preview.size)
        preview.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.color_rect.pos = self.root.ids.color_preview.pos
        self.color_rect.size = self.root.ids.color_preview.size

    def update_color(self, *args):
        self.r = int(self.root.ids.red_slider.value)
        self.g = int(self.root.ids.green_slider.value)
        self.b = int(self.root.ids.blue_slider.value)

        r_norm = self.r / 255
        g_norm = self.g / 255
        b_norm = self.b / 255

        self.color_instruction.rgb = (r_norm, g_norm, b_norm)

        hex_color = f"#{self.r:02X}{self.g:02X}{self.b:02X}"
        self.root.ids.hex_label.text = hex_color

    def copy_to_clipboard(self):
        hex_value = self.root.ids.hex_label.text
        Clipboard.copy(hex_value)

        snackbar = MDSnackbar(
            MDLabel(
                text=f"{hex_value} скопирован в буфер",
                theme_text_color="Custom",
                text_color=self.theme_cls.primary_color,
            ),
            size_hint_x=0.8,
            pos_hint={"center_x": 0.5},
            y=50,
            buttons=[
                MDFlatButton(
                    text="OK",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: snackbar.dismiss(),
                )
            ],
        )
        snackbar.open()





if __name__ == "__main__":
    ColorMixerApp().run()
