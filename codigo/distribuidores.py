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

#Window.size=(300,500)


class lista(ScrollView):
    def llamar(self):
        scroll = ScrollView()
        list_view= MDList()
        scroll.add_widget(list_view)
        for i in ['Proesa',"Dipor",'Pronaca','LaFrabil','PlastiLopez']:
            imagen = ImageLeftWidget(source=f'Imagenes/Proveedores/{i}.jpg')
            items= TwoLineIconListItem(text=i,secondary_text='Productos')
            items.add_widget(imagen)
            #tile = SmartTileWithLabel(source="/Imagenes/1.jpg",text='Foto')
            #list_view.add_widget(tile)
            list_view.add_widget(items)
        return scroll

class DistApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(lista().llamar())
        screen.add_widget(Builder.load_file('dist.kv'))
        return screen
    def navigation_draw(self):
        pass


        
DistApp().run()