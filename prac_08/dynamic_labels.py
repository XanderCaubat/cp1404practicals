"""
CP1404/CP5632 - Practical 8
Dynamic Labels App
Estimate: 30 minutes
Actual:   20 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabels(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Alex', 'Bob', 'Charles', 'Delta']

    def build(self):
        Window.size = (400, 300)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_label()
        return self.root

    def create_label(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()
