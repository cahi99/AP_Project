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
from Productos import Screen2
from Mi_Pedido import Screen3

#Window.size=(300,500)

class Screen1(Screen):
    def __init__(self, *args, **kwargs):
        super(Screen1,self).__init__(**kwargs)
        self.ids.wig.add_widget(Lista())

class Lista(MDList):
    def __init__(self, *args, **kwargs):
        super(Lista,self).__init__(**kwargs)
        for i in ['Proesa',"Dipor",'Pronaca','LaFrabil','PlastiLopez']:
            imagen = ImageLeftWidget(source=f'Imagenes/Proveedores/{i}.jpg')
            items= TwoLineIconListItem(text=i,secondary_text='Productos')
            items.bind(on_press=  self.change)
            items.add_widget(imagen)
            #tile = SmartTileWithLabel(source="/Imagenes/1.jpg",text='Foto')
            #list_view.add_widget(tile)
            self.add_widget(items)
    def change(self,*args):
        sm.current = 'Screen2'

sm= ScreenManager()
class DistApp(MDApp):
    def build(self):
        sm.add_widget(Screen2(name='Screen2'))
        sm.add_widget(Screen1(name='Screen1'))
        sm.add_widget(Screen3(name='Screen3'))
        sm.current = 'Screen1'
        return sm

if __name__ == '__main__':
    DistApp().run()