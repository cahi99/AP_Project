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
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
import os
import shutil
Empresa='credenciales.json'
objet=""

#from Conexion import Envio as LaData

#Window.size=(300,500)

class Screen1(Screen):
    def __init__(self, *args, **kwargs):
        super(Screen1,self).__init__(**kwargs)
        entries = os.listdir('codigo/Empresas')
        for i in [*entries]:
            self.ids.wig.add_widget(Lista(i))
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,  # function called when the user reaches directory tree root
            select_path=self.select_path,
            ext=[".py", "kv"],
        )
        self.file_manager.ext = [".json"]        
    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True
    def select_path(self, path):
        self.exit_manager()
        shutil.copy(path, 'codigo/Empresas')
        self.ids.wig.clear_widgets()
        entries = os.listdir('codigo/Empresas')
        for i in [*entries]:
            self.ids.wig.add_widget(Lista(i))
        toast(path)
    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

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
        sm.add_widget(Screen3(name='Screen3'))
        sm.current = 'Screen1'
        return sm

if __name__ == '__main__':
    DistApp().run()