from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Randhir", "Ethan", "Jack", "Juliet", "Samuel"]

    def build(self):
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            self.root.ids.labels.add_widget(Label(text=name))


DynamicLabelsApp().run()
