from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

KM_TO_MILES_RATE = 1.60934


def handle_errors(input_value):
    try:
        checked_value = float(input_value)
        return checked_value
    except ValueError:
        return 0.0


class MilesToKmApp(App):
    output = StringProperty()

    def build(self):
        self.title = "Convert Miles to KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculations(self, value_in_miles):
        checked_value_in_miles = handle_errors(value_in_miles)
        value_in_km = KM_TO_MILES_RATE * checked_value_in_miles
        self.output = "{:.3f}".format(value_in_km)

    def change_value(self, value_to_change, increment):
        checked_value_to_change = handle_errors(value_to_change)
        changed_value = checked_value_to_change + increment
        self.root.ids.input_value.text = str(changed_value)


MilesToKmApp().run()
