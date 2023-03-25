from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class ShowResult(Screen):
    def __init__(self, **kwargs):
        super(ShowResult, self).__init__(** kwargs)

        self.basis_layout = AnchorLayout()
        # widgets = [self.basis_layout.add_widget(Button(text=tee)) for tee in ('500', '600')]

        self.button_back(self.basis_layout)
        self.add_widget(self.basis_layout)

    def button_back(self, basis: AnchorLayout):
        box = BoxLayout(orientation='vertical')

        widgets = [
            Button(text=tee)
            for tee in ('back', '600')
        ]

        widgets[0].on_press = self.back_second_screen
        add_w = [box.add_widget(widget=wid) for wid in widgets] #map(lambda _: box.add_widget, widgets)
        basis.add_widget(box)

    def back_second_screen(self):
        print('work > bakc')
        print('self.manager.some_value >', self.manager.some_value)

        print(self.lists)

    #     self.manager.current = 'second'