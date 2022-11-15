"""
CP1404/CP5632 - Practical 8
Dynamic Labels App
Estimate: 30 minutes
Actual:      minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicLabels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Alex', 'Bob', 'Charles', 'Delta']

    def build(self):
        Window.size = (700, 300)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_label()
        return self.root

    def create_label(self):
        pass


DynamicLabels().run()
