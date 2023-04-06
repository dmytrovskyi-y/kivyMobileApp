import re

from kivy.uix.textinput import TextInput


_pat = re.compile('[^0-9]')  # регулярное выражения для ввода данных


class SumOfMoney(TextInput):
    """
    Виджет ввода общей суммы зразаботаных денег.
    """
    def __init__(self, **kwargs):
        super(SumOfMoney, self).__init__(**kwargs)

        self.multiline = False
        self.halign = 'right'

        # self.background_color = [12, 70, 156, .1]
        self.padding = 10
        self.hint_text = 'Введите общую сумму доходи. Только четное число!'
        # self.hint_text_color = [12, 70, 156, .9]

    def on_focus(self, instanse, value):
        """
        Вызов метода происходит когда пользователь нажал на поле для ввода данных.
        Прописана логика проверки числа. Если число не четное или равно 0, пользователь получаеть
        сообщения об ошибке, в поле для ввода.
        """
        self.hint_text = ''

        if value:
            self.text = ''

        else:
            # self.background_color = [12, 34, 55, .2]

            if not self.text:  # если не ввели число
                self.hint_text = 'Это обязательное поле для ввода!'

            elif not int(self.text) or int(self.text) % 2 > 0:
                self.hint_text = 'Число должно быть четным!'
                self.text = ''

    def insert_text(self, substring, from_undo=False):
        """
        Переопределяем метод, для котроля ввода символов.
        Позволяет вводить только числа
        """
        s = ''.join(re.sub(_pat, '', s) for s in substring)
        return super().insert_text(s, from_undo=from_undo)


class BaseInputWidget(TextInput):
    """
     Базовый Виджет - поле ввода теста(номеров)

    """

    def __init__(self, name_, **kwargs):
        super(BaseInputWidget, self).__init__(**kwargs)

        self.name_ = name_
        self.focus_flag = 0
        # self.text = '0'
        self.halign = 'right'
        self.hint_text = self.name_


        # self.position = 'horizontal'
        self.font_size = '15sp'
        self.foreground_color = [255, 255, 0, 0.9]
        self.background_color = [0, 0.8, 0, 0.7]
        # self.border_color = [1, 0, 0, 1]

    # def bind(self):
        """
        Настройка работы виджета при взаимодействии с виджетом
        :return: None
        """
        # self.focus = self.on_focus

    def insert_text(self, substring, from_undo=False):

        s = ''.join(re.sub(_pat, '', s) for s in substring)
        return super().insert_text(s, from_undo=from_undo)

    def on_focus(self, instance, value):
        """
        Указывает логику работы виджетта, когда с ним впервые взаимодействуют.

        :param instance:
        :param value:
        :user_data:
        :return:
        """

        if value:
            self.text = ''
            self.foreground_color = [55, 25, 0, 1]

        else:
            if not self.text:

                self.text = '0'

