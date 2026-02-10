from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.label import Label
import random

class Body(Screen):

    def number_clicked(self, value):
        self.ids.inputs.text += value

    def delete_last(self):
        self.ids.inputs.text = self.ids.inputs.text[:-1]

    def clear(self):
        self.ids.inputs.text = "0"

    def calculate_result(self):
        Clock.schedule_once(self.go_to_valentine, 0.5)

    def go_to_valentine(self, dt):
        self.manager.current = "valentine"


class CrashScreen(Screen):
    def on_enter(self):
        anim = Animation(opacity=0, duration=0.1) + Animation(opacity=1, duration=0.1)
        anim.repeat = True
        anim.start(self.ids.crash_label)

        Clock.schedule_once(self.go_to_valentine, 3)

    def go_to_valentine(self, dt):
        self.manager.current = 'valentine'


class ValentineScreen(Screen):

    def trigger_rejection_crash(self):
        self.manager.current = "crash"


class FinalScreen(Screen):

    def on_enter(self):
        for _ in range(30):
            Clock.schedule_once(
                lambda dt: self.spawn_item(),
                random.random() * 2
            )

    def spawn_item(self):
        icons = ["<3", "<3", "<3", "<3"]

        l = Label(
            text=random.choice(icons),
            font_size="30sp",
            pos=(random.randint(0, Window.width), -100)
        )

        self.add_widget(l)

        anim = Animation(
            y=Window.height + 100,
            duration=random.uniform(3, 6),
            opacity=0
        )
        anim.start(l)


class MyApp(App):

    def build(self):
        Builder.load_file("calculator.kv")

        sm = ScreenManager()
        sm.add_widget(Body(name="menu"))
        sm.add_widget(CrashScreen(name='crash'))
        sm.add_widget(ValentineScreen(name="valentine"))
        sm.add_widget(FinalScreen(name="final"))

        return sm


if __name__ == "__main__":
    MyApp().run()
