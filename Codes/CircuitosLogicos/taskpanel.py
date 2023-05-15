from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.properties import BooleanProperty, StringProperty


class Task(Button):
    # true if task is selected
    is_active = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(Task, self).__init__(**kwargs)
        self.text = "Task"
        self.font_size = 16
        self.background_down = ''
        self.background_normal = ''
        self.size_hint = (None, .9)
        self.width = 80
        self.pos_hint = {'x': 1, 'y': .05}
        self.background_color = (0.2, 0.2, 0.2, 1)

    def on_is_active(self, instance, value):
        if self.is_active:
            self.color = (0, 0, 1, 1)
        else:
            self.color = (1, 1, 1, 1)




class DrawCircuit(Task):
    def __init__(self, **kwargs):
        super(DrawCircuit, self).__init__(**kwargs)
        self.text = "Circuit"


# removed the help, truthtable, and simplify buttons


class Panel(BoxLayout):
    task = StringProperty("Circuito")

    def __init__(self, **kwargs):
        super(Panel, self).__init__(**kwargs)
        self.size_hint = (1, .9)
        self.pos_hint = {'x': 1, 'y': .05}
        self.drawcircuit = DrawCircuit()
        self.add_widget(self.drawcircuit)
        with self.canvas.before:
            Color(.2, .2, .2, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class TaskPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(TaskPanel, self).__init__(**kwargs)
        self.panel = Panel()
        self.add_widget(self.panel)


if __name__ == '__main__':
    class TestApp(App):

        def build(self):
            root = TaskPanel()
            return root


    TestApp().run()
