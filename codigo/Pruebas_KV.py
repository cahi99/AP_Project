import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)
class Touch(Widget):
    btn= ObjectProperty(None)
    def on_touch_down(self, touch):
        print('Mouse Down',touch)
        self.btn.opactity=0.5
    def on_touch_move(self, touch):
        print('Mouse Move',touch)
    def on_touch_up(self, touch):
        print('Mouse Up',touch)


class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    def btn(self):
        print('Name:',self.name.text,"Email:",self.email.text)
    """
    def __init__(self,**kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols=1

        self.inside = GridLayout()
        self.inside.cols=2

        self.inside.add_widget(Label(text="Name: "))
        self.name= TextInput(multiline=False)
        self.inside.add_widget(self.name)


        self.inside.add_widget(Label(text="LastName: "))
        self.lname= TextInput(multiline=False)
        self.inside.add_widget(self.lname)


        self.inside.add_widget(Label(text="NickName: "))
        self.nname= TextInput(multiline=False)
        self.inside.add_widget(self.nname)

        self.add_widget(self.inside)

        self.submit = Button(text='Enviar',font_size=35)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self,instance):
        variable = self.name.text
        print('Precionado perro: '+variable)
    """

class MyApp(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    MyApp().run()
