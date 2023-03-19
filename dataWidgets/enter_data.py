
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from dataWidgets.inputText import BaseInputWidget


class WidgetEnterData(BoxLayout):
    def __init__(self, **kwargs):
        super(WidgetEnterData, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.info_text = 'Укажите начальный номер билета и количество.'
        self.test_text = ''
        self.test_text_1 = ''
        self.count_focus = True

        self.user_data = {500: [], 400: [], 350: [], 250: [], 100: [], 50: []}

        # text_b = Button(on_press=self.print_cmd, text='click me')
        # text_b.size_hint = (0.5, 0.5)

    def five_hundred(self):
        layout = GridLayout(cols=3, padding=10)

        self.number_of_tickets = BaseInputWidget(text='0')
        starting_number = BaseInputWidget(text='0')
        # self.text_1.padding = [2, 10, 10, 7]
        # self.text_1.bind(focus=self.on_focus)
        layout.add_widget(Label(text='Введите данные билетов № 500'))
        layout.add_widget(self.number_of_tickets)
        layout.add_widget(starting_number)

        self.add_widget(layout)
        # return layout

    # def on_focus(self, instance, value):
    #     if value and self.count_focus:
    #         print('User focused', instance, value)
    #         self.text_1.text = ''
    #         self.count_focus = False
    #     else:
    #         print('User defocused', instance, value)

    def print_cmd(self, value):
        print('My button <%s> state is <%s>' % (self, value.text))
        self.test_text = self.text_1.text
        print('test_text=', self.test_text)
        print('test_text_1=', self.test_text_1)

    def on_enter(instance, value):
        print('User pressed enter in', instance, value)
