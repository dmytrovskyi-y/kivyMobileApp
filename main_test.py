from kivy import Config
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from dataWidgets.inputText import SumOfMoney, BaseInputWidget

Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (480, 900)


class MyApp(App):


    def build(self):


        box = BoxLayout(orientation='vertical')
        self.s = SumOfMoney()
        self.m = BaseInputWidget()
        box.add_widget(self.s)
        box.add_widget(self.m)
        but = Button(text='test')
        but.on_press = self.watch
        box.add_widget(but)

        return box

    def watch(self):
        print(self.s.text)

if __name__ == '__main__':
    MyApp().run()
