from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class MilesToKmApp(App):
    output = StringProperty()

    def build(self):
        self.title = "Convert Miles to KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculations(self, value_in_miles):
        KM_TO_MILES_RATE = 1.60934
        value_in_km = KM_TO_MILES_RATE * value_in_miles
        self.output = "{:.3f}".format(value_in_km)

    def change_value(self, number, change_value):
        changed_value = number + change_value
        self.root.ids.input_value.text = str(changed_value)


MilesToKmApp().run()
