from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class FirstPage(Screen):

    def __init__(self, **kwargs):
        super(FirstPage, self).__init__(**kwargs)

        basis = AnchorLayout()

        self.buttons(basis=basis)
        self.add_widget(basis)

    def buttons(self, basis: AnchorLayout):

        box = BoxLayout(
            spacing=5,
            orientation='vertical',
            size_hint=[.6, .2]
        )

        greetings = Label(text='Анна привет')

        but_start = Button(text='Start')
        but_start.background_color = [0, 146, 23, 0.9]
        but_start.on_press = self.changeScreen

        but_info = Button(text='Информация')
        but_info.background_color = [0, 49, 255, 0.9]

        box.add_widget(but_start)
        box.add_widget(but_info)
        box.add_widget(greetings)

        basis.add_widget(box)

    def changeScreen(self) -> None:
        self.manager.current = 'second'
