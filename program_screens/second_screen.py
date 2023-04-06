from typing import List

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from calculate.result import Calculate
from dataWidgets.inputText import BaseInputWidget, SumOfMoney
from dataWidgets.second_scr_widgets import BlockInputLayout, BlockInformLayout


class SecondScreen(Screen):

    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)

        self.money = None
        self.info_text = 'Укажите начальный номер билета и их количество.'
        self.num_ticket = [500, 400, 300, 250, 200, 150, 100, 50]

        self.basis_layout = BoxLayout(orientation='vertical')
        self.basis_layout.padding = [2, 5, 5, 2]
        # self.basis_layout.spacing = 5


        # self.field_sum_of_money(self.basis_layout)
        self.create_widgets_input()
        self.field_buttons(self.basis_layout)
        # ss = AnchorLayout()
        # ss.add_widget(self.basis_layout)
        self.add_widget(self.basis_layout)

    def create_widgets_input(self):

        self.money = SumOfMoney()
        self.basis_layout.add_widget(self.money)

        # infor_widgets = {
        #     key: [Label(text=f'Билет номер - {key}'), Label(text='Количество билетов'), Label(text='Начальный номер')]
        #     for key in self.num_ticket
        # }

        # base_inform_wid = {
        #     key: BlockInformLayout(infor_widgets[key])
        #     for key in self.num_ticket
        # }

        self.widgets_input = {
            key: [BaseInputWidget(name_="Начальный номер"),
                  BaseInputWidget(name_='Кол-во')]
            for key in self.num_ticket
        }

        self.add_widgets = {
            key: BlockInputLayout(
                text_info=Label(text=f'Билет номер - {key}'),
                number_of_tickets=self.widgets_input.get(key)[0],
                starting_number=self.widgets_input.get(key)[1]
            )
            for key in self.widgets_input
        }

        for key in self.num_ticket:
            # self.basis_layout.add_widget(base_inform_wid[key])
            self.basis_layout.add_widget(self.add_widgets[key])

    def field_buttons(self, basis: BoxLayout):

        self.layout_buttons = GridLayout(cols=2, padding=10, spacing=10)
        self.but_calculation = Button(text='Расчет')
        but_back = Button(text='Главная')

        but_back.size_hint = (0.4, 0.15)
        but_back.pos_hint = {'x': 0.3, 'y': 0.3}

        but_back.on_press = self.back_to_screen_first
        self.but_calculation.on_press = self.calculation

        self.layout_buttons.add_widget(self.but_calculation)
        self.layout_buttons.add_widget(but_back)
        basis.add_widget(self.layout_buttons)

    def back_to_screen_first(self) -> None:

        self.manager.current = 'first'

    def calculation(self) -> None:
        ss = int(self.money.text)
        if int(ss) >= 100 and not int(ss) % 2:
            print(int(self.money.text) % 2)
            print(ss)

            input_data = {

                key: [int(value1.text), int(value2.text)]
                for key, [value1, value2] in self.widgets_input.items()
            }

            self.result = Calculate(
                sum_money=ss,
                data_dict=input_data
            )
            if self.result.display():

                # self.manager.get_screen("result").res_data = self.result.display()

                self.but_calculation.text = 'Показать результат'
                self.but_calculation.background_color = [0, 128, 0, 0.7]
                self.but_calculation.on_press = self.go_screen_result
                self.basis_layout.add_widget(Button(text='Сбросить данные'))

        else:
            self.money.text = '0'

    def go_screen_result(self):

        self.manager.get_screen("result").res_data = self.result.display()
        self.manager.get_screen("result").back_second_screen()
        self.manager.get_screen("result").display_data()

        self.manager.su = '11'
        print(self.manager.su)
        self.manager.current = 'result'

    def reset_data(self):
        pass
