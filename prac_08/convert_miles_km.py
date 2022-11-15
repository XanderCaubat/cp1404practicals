"""
CP1404/CP5632 - Practical 8
Convert Miles to Kilometers App
Estimate: 20 minutes
Actual:     minutes
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

KM_PER_MILE = 1.6


class KmMilesConverterApp(App):

    def build(self):
        Window.size = (200, 100)
        self.title = "Miles/Km Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        result = self.get_miles() * KM_PER_MILE
        self.root.ids.output_label.text = str(f"{result:.2f} km")

    def get_miles(self):
        try:
            miles = float(self.root.ids.input_distance.text)
            return miles
        except ValueError:
            return 0

    def handle_increment(self, increment):
        new_result = self.get_miles() + increment
        self.root.ids.input_distance.text = str(new_result)
        self.handle_conversion(new_result)

    def handle_decrement(self, decrement):
        new_result = self.get_miles() - decrement
        self.root.ids.input_distance.text = str(new_result)
        self.handle_conversion(new_result)


KmMilesConverterApp().run()
