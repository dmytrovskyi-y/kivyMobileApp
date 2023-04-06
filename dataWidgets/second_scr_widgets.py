from typing import List

from kivy.uix.gridlayout import GridLayout


class BlockInformLayout(GridLayout):
    """
    Блок виджетов ввода информаии о билите.
    """
    def __init__(self, list_wid: List, **kwargs):
        super(BlockInformLayout, self).__init__(** kwargs)

        self.cols = 3

        self.add_widgets_(list_wid)

    def add_widgets_(self, list_wid: List):
        for w_ in list_wid:
            self.add_widget(w_)


class BlockInputLayout(GridLayout):
    def __init__(self, text_info: str, number_of_tickets, starting_number, **kwargs):
        super(BlockInputLayout, self).__init__(**kwargs)

        # self.text_info = text_info
        # self.number_of_tickets = number_of_tickets
        # self.starting_number = starting_number

        self.cols = 3
        self.padding = 0
        self.spacing = 10
        # self.orientation = 'tb-lr'

        self.add_widget(text_info)
        self.add_widget(number_of_tickets)
        self.add_widget(starting_number)

    def add_widgets_(self, list_wid: List):

        for w_ in list_wid:
            self.add_widget(w_)
