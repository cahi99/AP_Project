
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
#from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

Window.size=(300,500)

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass
class DistribuidoresScreen(Screen):
    pass

sm=ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(DistribuidoresScreen(name='distribuidor'))


class DistribuidorApp(MDApp):
    def build(self):
        screen=Builder.load_file('logg.kv')
        return screen

DistribuidorApp().run()
