from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import MDList,TwoLineListItem,TwoLineIconListItem
from kivymd.uix.list import ImageLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.imagelist import SmartTileWithLabel
from Mi_Pedido import Screen3
import Productos
#import Conexion as data
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
import os
import shutil
Empresa='credenciales.json'
objet=""


class Screen1(Screen):
    def __init__(self, *args, **kwargs):
        super(Screen1,self).__init__(**kwargs)
        entries = os.listdir('codigo/Empresas')
        for i in [*entries]:
            self.ids.wig.add_widget(Lista(i))


class Lista(TwoLineIconListItem):
    def __init__(self, *args, **kwargs):
        super(Lista,self).__init__(**kwargs)
        I=str(args[0]).replace(".json","")
        self.text= I
        self.secondary_text='Productos'
        imagen = ImageLeftWidget(source=f'Imagenes/Proveedores/{I}.jpg')
        self.add_widget(imagen)

    def change(self,*args):
        global Empresa
        Empresa=str(args[0])
        sm.add_widget(Productos.Screen2(args[0],name='Screen2'))
        sm.current = 'Screen2'

sm= ScreenManager()

class DistApp(MDApp):
    def build(self):
        sm.add_widget(Screen1(name='Screen1'))
        sm.current = 'Screen1'
        return sm

if __name__ == '__main__':
    DistApp().run()