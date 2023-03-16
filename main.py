from kivy import Config
from kivy.app import App
from kivy.core.window import Window

from program_screens.manager import Manager


Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (480, 900)


class MyApp(App):

    def build(self):
        return Manager()


if __name__ == '__main__':
    MyApp().run()




































# from kivy.app import App
# from kivy.uix.textinput import TextInput
#
#
# class MyTextInput(TextInput):
#     def on_parent(self, widget, parent):
#         self.focus = True
#
#
# class SampleApp(App):
#     def build(self):
#         return MyTextInput()
#
#
# SampleApp().run()
# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.core.window import Window
# from kivy.config import Config
# from get_result_calcul import base_f
#
#
# Config.set('kivy', 'keyboard_mode', 'systemanddock')
#
#
# Window.size = (480, 900)
#
#
# class Container(GridLayout):
#
#     def calculator(self):
#
#         try:
#             data = int(self.user_data.text)
#
#             if data % 2 == 0:
#             	raise ValueError
#
#         except (TypeError, ValueError):
#             data = 0
#
#         calculation = base_f(data)
#         print(calculation)
#
#         self.fifty.text = calculation.get('50')
#         self.one_h.text = calculation.get('100')
#         self.two_h.text = calculation.get('250')
#         self.three_h.text = calculation.get('300')
#         self.four_h.text = calculation.get('400')
#         self.five_h.text = calculation.get('500')
#         self.result.text = calculation.get('result')
#
#
# class MyApp(App):
#
#     def build(self):
#         return Container()
#
#
# if __name__ == '__main__':
#     MyApp().run()
