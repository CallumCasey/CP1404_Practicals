from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicWidgetApp(App):
    def build(self):
        self.title = "Dynamic Widget App"
        self.root = Builder.load_file('dynamic_app.kv')
        for name in self.name_list:
            temp_label = Label(text=name)
            self.root.ids.list_names.add_widget(temp_label)
        return self.root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_list = ["Name One", "Name Two", "Name Three", "Name Four"]





DynamicWidgetApp().run()
