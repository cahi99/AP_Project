from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
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


class Myapp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    Myapp().run()
