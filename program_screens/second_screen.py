from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from calculate.result import Calculate
from dataWidgets.inputText import BaseInputWidget


class BlockyLayout(GridLayout):
    def __init__(self, text_info: str, number_of_tickets, starting_number, **kwargs):
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
    # MONEY = 0
    # DATA = {500: [], 400: [], 300: [], 250: [], 200: [], 150: [], 100: [], 50: []}

    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)

        self.info_text = 'Укажите начальный номер билета и их количество.'
        self.user_data = {500: [], 400: [], 300: [], 250: [], 200: [], 150: [], 100: [], 50: []}
        print('__init__ SecondScreen > user_data > ', self.user_data)

        basis_layout = BoxLayout(orientation='vertical')

        self.customization_basis(basis_layout)

        self.field_sum_of_money(basis_layout)
        self.create_widgets_input(basis_layout)
        self.field_buttons(basis_layout)

        self.add_widget(basis_layout)

    def customization_basis(self, basis: BoxLayout) -> None:
        basis.padding = [2, 5, 5, 2]
        basis.spacing = 5

    def create_widgets_input(self, basis):

        self.widgets_input = {key: [BaseInputWidget(text='0'), BaseInputWidget(text='0')] for key in self.user_data}

        add_widgets = [
            BlockyLayout(
                text_info=Label(text=f'Билет номер {key}'),
                number_of_tickets=self.widgets_input.get(key)[0],
                starting_number=self.widgets_input.get(key)[1]
            ) for key in self.widgets_input
        ]

        for wid in add_widgets:
            basis.add_widget(wid)

    def field_sum_of_money(self, basis: BoxLayout):
        self.money = BaseInputWidget(text='0')

        basis.add_widget(self.money)
        basis.add_widget(Label(text=self.info_text))
    #

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

        if not int(self.money.text) % 2:
            # self.manager.some_value

            sss = {

                key: [int(value1.text), int(value2.text)]
                for key, [value1, value2] in self.widgets_input.items()
            }

            result = Calculate(
                sum_money=int(self.money.text),
                data_dict=sss
            )


            self.lists = [4, 5, 6]
            self.manager.get_screen("result").lists = list(self.lists)

            self.manager.current = 'result'

        else:
            self.money.text = self.money.text + ' < число должно быть четным'





    # def field_five_hundred(self, basis: BoxLayout):
    #     text_info = 'билета № 500'
    #     self.f_number_of_tickets = BaseInputWidget(text='0')
    #     self.f_starting_number = BaseInputWidget(text='0')
    #
    #     ll = BlockyLayout(
    #         text_info=Label(text=text_info),
    #         number_of_tickets=self.f_number_of_tickets,
    #         starting_number=self.f_starting_number
    #     )
    #     basis.add_widget(ll)
    #
    # def field_four_hundred(self, basis: BoxLayout):
    #     text_info = 'билета № 400'
    #     self.fo_number_of_tickets = BaseInputWidget(text='0')
    #     self.fo_starting_number = BaseInputWidget(text='0')
    #
    #     ll = BlockyLayout(
    #         text_info=Label(text=text_info),
    #         number_of_tickets=self.fo_number_of_tickets,
    #         starting_number=self.fo_starting_number
    #     )
    #     basis.add_widget(ll)
    #
    # def field_three_hundred(self, basis: BoxLayout):
    #     text_info = 'билета № 300'
    #
    #     self.th_number_of_tickets = BaseInputWidget(text='0')
    #     self.th_starting_number = BaseInputWidget(text='0')
    #
    #     ll = BlockyLayout(
    #         text_info=Label(text=text_info),
    #         number_of_tickets=self.th_number_of_tickets,
    #         starting_number=self.th_starting_number
    #     )
    #     basis.add_widget(ll)
    #
    # def twenty_five_hundred(self, basis: BoxLayout):
    #     text_info = 'билета № 250'
    #
    #     self.twenty_five_number_of_tickets = BaseInputWidget(text='0')
    #     self.twenty_five_starting_number = BaseInputWidget(text='0')
    #
    #     ll = BlockyLayout(
    #         text_info=Label(text=text_info),
    #         number_of_tickets=self.twenty_five_starting_ticks,
    #         starting_number=self.twenty_five_starting_number
    #     )
    #     basis.add_widget(ll)
    #
    # def field_two_hundred_fifty(self, basis: BoxLayout):
    #     text_info = 'билета № 200'
    #
    #     self.tw_number_of_tickets = BaseInputWidget(text='0')
    #     self.tw_starting_number = BaseInputWidget(text='0')
    #
    #     ll = BlockyLayout(
    #         text_info=Label(text=text_info),
    #         number_of_tickets=self.tw_number_of_tickets,
    #         starting_number=self.tw_starting_number
    #     )
    #     basis.add_widget(ll)
    #
    # def field_hundred_fifty(self, basis: BoxLayout):
    #     text_info = 'билета № 100'
    #
    #     self.hu_fif_number_of_tickets = BaseInputWidget(text='0')
    #     self.hu_fif_starting_number = BaseInputWidget(text='0')
    #
    #     ll = BlockyLayout(
    #         text_info=Label(text=text_info),
    #         number_of_tickets=self.hu_fif_number_of_tickets,
    #         starting_number=self.hu_fif_starting_number
    #     )
    #     basis.add_widget(ll)
    #
    # def field_hundred(self, basis: BoxLayout):
    #     text_info = 'билета № 100'
    #
    #     self.hu_number_of_tickets = BaseInputWidget(text='0')
    #     self.hu_starting_number = BaseInputWidget(text='0')
    #
    #     ll = BlockyLayout(
    #         text_info=Label(text=text_info),
    #         number_of_tickets=self.hu_number_of_tickets,
    #         starting_number=self.hu_starting_number
    #     )
    #     basis.add_widget(ll)
    #
    # def field_fifty(self, basis: BoxLayout):
    #     text_info = 'билета № 50'
    #
    #     self.fif_number_of_tickets = BaseInputWidget(text='0')
    #     self.fif_starting_number = BaseInputWidget(text='0')
    #
    #     ll = BlockyLayout(
    #         text_info=Label(text=text_info),
    #         number_of_tickets=self.fif_number_of_tickets,
    #         starting_number=self.fif_starting_number
    #     )
    #     basis.add_widget(ll)