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
#import Conexion as data
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
import os
import shutil
Empresa=''
objet=""


class Screen4(Screen):
    def __init__(self, *args, **kwargs):
        super(Screen4,self).__init__(**kwargs)
        pass
    def on_enter(self):
        entries = os.listdir('codigo/Pedidos')
        for i in [*entries]:
            self.ids.wig.add_widget(Listadatos(i))


class Listadatos(TwoLineIconListItem):
    def __init__(self, *args, **kwargs):
        super(Listadatos,self).__init__(**kwargs)
        I=str(args[0]).replace("Pedido-","")
        I=str(I).replace(".csv","")
        self.text= I
        self.secondary_text='Pedido'
        imagen = ImageLeftWidget(source=f'Imagenes/Proveedores/{I}.jpg')
        self.add_widget(imagen)
        global Empresa
        Empresa= args[0]

    def change(self=TwoLineIconListItem,*args):
        print('la empresa es:'+args[0]+" .")
        Empresa = args[0]
        #sm.add_widget(Pedido.Screen5(args[0],name='Screen5'))
        #sm.current = 'Screen5'


class mispedidosApp(MDApp):
    def build(self):
        return Screen4()

if __name__ == '__main__':
    mispedidosApp().run()