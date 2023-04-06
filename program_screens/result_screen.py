from typing import List

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class BlockHeadlines(GridLayout):
    def __init__(self, **kwargs):
        super(BlockHeadlines, self).__init__(** kwargs)

        self.cols = 4
        self.rows = 1
        self.padding = 10
        self.spacing = 10

    def add_list_widgets(self, widgets: List):

        for w_ in widgets:
            self.add_widget(w_)


class ShowResult(Screen):
    def __init__(self, **kwargs):
        super(ShowResult, self).__init__(** kwargs)
        self.box = BoxLayout(orientation='vertical')
        # widgets = [self.basis_layout.add_widget(Button(text=tee)) for tee in ('500', '600')]

    def display_data(self):
        print('display_data(self)')

        block_headlines = BlockHeadlines()
        #     padding=10,
        #     spacing=10
        # )

        headlines = ['Цена руб.', 'Продано к-во', 'Сумма', 'Конечный билет']
        headlines_sec = ['Осталось к-во', 'Сумма']

        head_layouts = [Label(text=t) for t in headlines]
        head_layouts_sec = [Label(text=t) for t in headlines_sec]

        block_headlines.add_list_widgets(head_layouts)

        for num, val in self.res_data.items():
            number_layout = [Label(text=num), Label(text=val)]

            block_in_box.add_widget(number_layout[0])
            block_in_box.add_widget(number_layout[1])
            block_in_box.add_widget(Label(text='test sum'))
            block_in_box.add_widget(Label(text='test final tick'))

        # for layout_ in head_layouts_sec:
        #     block_in_box

        self.box.add_widget(block_in_box)
        self.box.add_widget(Button(text=self.res_data['result']))
        self.add_widget(self.box)

    # def button_back(self, basis: AnchorLayout):
    #     box = BoxLayout(orientation='vertical')
    #
    #     widgets = [
    #         Button(text=tee)
    #         for tee in ('back', '600')
    #     ]
    #
    #     widgets[0].on_press = self.back_second_screen
    #     widgets[1].on_press = self.back_second_s
    #     add_w = [box.add_widget(widget=wid) for wid in widgets] #map(lambda _: box.add_widget, widgets)
    #     basis.add_widget(box)
    #
    def back_second_screen(self):
        print('work > back')

        print(self.res_data)
    #
    # def back_second_s(self):
    #     self.manager.current = 'second'
