from kivy.uix.screenmanager import ScreenManager, RiseInTransition

from program_screens.result_screen import ShowResult
from program_screens.start_screen import FirstPage
from program_screens.second_screen import SecondScreen


class Manager(ScreenManager):
    """
    Менеджер экранов. Управляет экранами преложенная
    Логика взаимодействия и изменения скриннов приложения
    """
    def __init__(self, **kwargs):
        super(Manager, self).__init__(** kwargs)

        self.transition = RiseInTransition()  # анимация при переключении скринов

        self.add_widget(FirstPage(name='first'))
        self.add_widget(SecondScreen(name='second'))
        self.add_widget(ShowResult(name='result'))
