from kivy.uix.textinput import TextInput


class BaseInputWidget(TextInput):
    """
     Базовый Виджет - поле ввода теста(номеров)

    """

    def __init__(self, **kwargs):
        super(BaseInputWidget, self).__init__(**kwargs)

        self.focus_flag = 0
        self.multiline = False

        # self.position = 'horizontal'
        self.font_size = '15sp'
        self.foreground_color = [255, 255, 0, 0.9]
        self.background_color = [0, 0, 0, 0.7]
        # self.border_color = [1, 0, 0, 1]

    def bind(self):
        """
        Настройка работы виджета при взаимодействии с виджетом
        :return: None
        """
        self.focus = self.on_focus

    def on_focus(self, instance, value):
        """
        Указывает логику работы виджетта, когда с ним впервые взаимодействуют.

        :param instance:
        :param value:
        :return:
        """

        if value and self.focus_flag in (0, 2):
            self.text = ''
            self.focus_flag = 1

        else:

            if self.text and not self.text.isdigit() and self.focus_flag == 1:
                self.text = '0'
                self.focus_flag = 2
                self.background_color = [255, 0, 0, 0.7]

            elif not self.text and self.focus_flag == 1:
                self.text = '0'
                self.focus_flag = 0

            else:
                self.foreground_color = [1, 1, 1, 1]
                self.background_color = [0, 128, 0, 0.7]
