"""
CP1404/CP5632 - Practical 8
Convert Miles to Kilometers App
Estimate: 20 minutes
Actual:     minutes
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class KmMilesConverterApp(App):

    def build(self):
        Window.size = (200, 100)
        self.title = "Miles/Km Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        result = float(value) * 1.6
        self.root.ids.output_label.text = str(f"{result:.2f} km")


KmMilesConverterApp().run()
