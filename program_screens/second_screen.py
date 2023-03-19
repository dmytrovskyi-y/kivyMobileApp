from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from dataWidgets.inputText import BaseInputWidget


class BlockyLayout(GridLayout):
    def __init__(self, text_info, number_of_tickets, starting_number, **kwargs):
        super(BlockyLayout, self).__init__(**kwargs)

        self.text_info = text_info
        self.number_of_tickets = number_of_tickets
        self.starting_number = starting_number

        self.cols = 3
        self.padding = 10
        self.orientation = 'tb-lr'

        self.add_widget(text_info)
        self.add_widget(number_of_tickets)
        self.add_widget(starting_number)


class SecondScreen(Screen):
    DATA = {'sumMoney': 0, 500: [], 400: [], 300: [], 250: [], 100: [], 50: []}

    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)

        self.info_text = 'Укажите начальный номер билета и их количество.'
        self.user_data = {500: [], 400: [], 300: [], 250: [], 100: [], 50: []}

        basis_layout = BoxLayout(orientation='vertical')

        self.customization_basis(basis_layout)
        self.field_sum_of_money(basis_layout)
        self.field_five_hundred(basis_layout)
        self.field_four_hundred(basis_layout)
        self.field_three_hundred(basis_layout)
        self.field_two_hundred_fifty(basis_layout)
        self.field_hundred(basis_layout)
        self.field_fifty(basis_layout)
        self.field_buttons(basis_layout)

        self.add_widget(basis_layout)

    def customization_basis(self, basis: BoxLayout):
        basis.padding = [2, 5, 5, 2]
        basis.spacing = 5

    def field_sum_of_money(self, basis: BoxLayout):
        self.money = BaseInputWidget(text='0')

        basis.add_widget(self.money)
        basis.add_widget(Label(text=self.info_text))

    def field_five_hundred(self, basis: BoxLayout):
        text_info = 'билета № 500'
        self.f_number_of_tickets = BaseInputWidget(text='0')
        self.f_starting_number = BaseInputWidget(text='0')

        ll = BlockyLayout(
            text_info=Label(text=text_info),
            number_of_tickets=self.f_number_of_tickets,
            starting_number=self.f_starting_number
        )
        basis.add_widget(ll)

    def field_four_hundred(self, basis: BoxLayout):
        text_info = 'билета № 400'
        self.fo_number_of_tickets = BaseInputWidget(text='0')
        self.fo_starting_number = BaseInputWidget(text='0')

        ll = BlockyLayout(
            text_info=Label(text=text_info),
            number_of_tickets=self.fo_number_of_tickets,
            starting_number=self.fo_starting_number
        )
        basis.add_widget(ll)

    def field_three_hundred(self, basis: BoxLayout):
        text_info = 'билета № 350'

        self.th_number_of_tickets = BaseInputWidget(text='0')
        self.th_starting_number = BaseInputWidget(text='0')

        ll = BlockyLayout(
            text_info=Label(text=text_info),
            number_of_tickets=self.th_number_of_tickets,
            starting_number=self.th_starting_number
        )
        basis.add_widget(ll)

    def field_two_hundred_fifty(self, basis: BoxLayout):
        text_info = 'билета № 200'

        self.tw_number_of_tickets = BaseInputWidget(text='0')
        self.tw_starting_number = BaseInputWidget(text='0')

        ll = BlockyLayout(
            text_info=Label(text=text_info),
            number_of_tickets=self.tw_number_of_tickets,
            starting_number=self.tw_starting_number
        )
        basis.add_widget(ll)

    def field_hundred(self, basis: BoxLayout):
        text_info = 'билета № 100'

        self.hu_number_of_tickets = BaseInputWidget(text='0')
        self.hu_starting_number = BaseInputWidget(text='0')

        ll = BlockyLayout(
            text_info=Label(text=text_info),
            number_of_tickets=self.hu_number_of_tickets,
            starting_number=self.hu_starting_number
        )
        basis.add_widget(ll)

    def field_fifty(self, basis: BoxLayout):
        text_info = 'билета № 50'

        self.fif_number_of_tickets = BaseInputWidget(text='0')
        self.fif_starting_number = BaseInputWidget(text='0')

        ll = BlockyLayout(
            text_info=Label(text=text_info),
            number_of_tickets=self.fif_number_of_tickets,
            starting_number=self.fif_starting_number
        )
        basis.add_widget(ll)

    def field_buttons(self, basis: BoxLayout):

        layout_buttons = GridLayout(cols=2, padding=10, spacing=10)

        but_result = Button(text='Расчет')
        but_back = Button(text='Главная')

        but_back.size_hint = (0.4, 0.15)
        but_back.pos_hint = {'x': 0.3, 'y': 0.3}

        but_back.on_press = self.back_to_screen_first
        but_result.on_press = self.back_to_screen_result

        layout_buttons.add_widget(but_result)
        layout_buttons.add_widget(but_back)
        basis.add_widget(layout_buttons)

    def back_to_screen_first(self) -> None:
        self.manager.current = 'first'

    def back_to_screen_result(self) -> None:
        self.manager.current = 'result'
        self.DATA['sumMoney'] = int(self.money.text)
        self.DATA[500].extend((int(self.f_number_of_tickets.text), int(self.f_starting_number.text)))
        self.DATA[400].extend((int(self.fo_number_of_tickets.text), int(self.fo_starting_number.text)))
        self.DATA[300].extend((int(self.th_number_of_tickets.text), int(self.th_starting_number.text)))
        self.DATA[250].extend((int(self.tw_number_of_tickets.text), int(self.tw_starting_number.text)))
        self.DATA[100].extend((int(self.hu_number_of_tickets.text), int(self.hu_starting_number.text)))
        self.DATA[50].extend((int(self.fif_number_of_tickets.text), int(self.fif_starting_number.text)))
        print(self.DATA)
