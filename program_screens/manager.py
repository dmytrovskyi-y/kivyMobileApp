from kivy.uix.screenmanager import ScreenManager, RiseInTransition

from .result_screen import ShowResult
from .start_screen import FirstPage
from .second_screen import SecondScreen


class Manager(ScreenManager):
    """
    Менеджер экранов. Управляет экранами преложенная
    Логика взаимодействия и изменения скриннов приложения
    """
    def __init__(self, **kwargs):
        super(Manager, self).__init__(** kwargs)

        self.su = '00000'
        self.transition = RiseInTransition()  # анимация при переключении экранов

        self.add_widget(FirstPage(name='first'))
        self.add_widget(SecondScreen(name='second'))
        self.add_widget(ShowResult(name='result'))
