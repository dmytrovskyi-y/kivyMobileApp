from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from program_screens.second_screen import SecondScreen


class ShowResult(Screen):
    def __init__(self, **kwargs):
        super(ShowResult, self).__init__(** kwargs)
        data = SecondScreen.DATA

        basis_layout = AnchorLayout()


        self.add_widget(Label(text=f'this page is under construction {data}'))

    def button_back(self):
        test_button_back = Button(text='back')
        test_button_back.on_press = self.back_second_screen
        self.add_widget(self.button_back)


    def back_second_screen(self):
        pass
    #     self.manager.current = 'second'