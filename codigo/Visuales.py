
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.list import MDList,TwoLineListItem,TwoLineIconListItem
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.list import ImageLeftWidget
from kivy.properties import ObjectProperty
from kivymd.uix.card import MDCard
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import  RightContent
from kivy.clock import Clock
#from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
#import distribuidores
#from distribuidores import Lista
#import distribuidores
from distribuidores import Screen1
from Productos import Screen2
from Mi_Pedido import Screen3
Window.size=(300,500)

#sm=ScreenManager()
"""class Screen1(distribuidores.Screen1):
    pass"""
"""
class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass
class DistribuidoresScreen(Screen):
    pass


###Distribuidor
class Screen1(Screen):
    def __init__(self, *args, **kwargs):
        super(Screen1,self).__init__(**kwargs)

class Lista(MDList):
    def __init__(self, *args, **kwargs):
        super(Lista,self).__init__(**kwargs)
        for i in ['Proesa',"Dipor",'Pronaca','LaFrabil','PlastiLopez']:
            imagen = ImageLeftWidget(source=f'Imagenes/Proveedores/{i}.jpg')
            items= TwoLineIconListItem(text=i,secondary_text='Productos')
            items.add_widget(imagen)
            #tile = SmartTileWithLabel(source="/Imagenes/1.jpg",text='Foto')
            #list_view.add_widget(tile)
            self.add_widget(items)

################################################################

###Productos
class Screen2(Screen):
    pass


class Screen3(Screen):
    pass

class MyCard(MDCard):
    def __init__(self, *args, **kwargs):
        super(MyCard,self).__init__(**kwargs)
        self.ids.n_producto.text=args[0]
        self.ids.id_image.source=args[1]
        self.ids.plus.icon='plus'
        self.ids.cero.text='0'
        self.ids.minus.icon='minus'
################################################################
class MyCard1(MDCard):
    pass
class Mylist(TwoLineListItem):
    def __init__(self, *args, **kwargs):
        super(Mylist,self).__init__(**kwargs)
        self.text=args[0]
        self.on_press=print(self.text)
        self.secondary_text= 'Distribuidores'

class Subtotales(MDGridLayout):
    def __init__(self, *args, **kwargs):
        super(Subtotales,self).__init__(**kwargs)
        self.ids.val.text= args[0]
        self.ids.lbl.text= args[1]

#sm.add_widget(Screen2(name='Screen2'))
"""
class MenuScreen(Screen):
    pass
class LoggApp(MDApp):
    def build(self):
        sm=Builder.load_file('logg.kv')
        sm.add_widget(Screen2())
        #sm.current='menu'
        return sm
        """
        sm=Builder.load_file('visuales.kv')
        for i,j in zip(['Plato 6','Plato 8','Plato 9'],['plato_6.jpg','plato_8.jpg','plato_9.jpg']):
            sm.ids.box.add_widget(MyCard(i,"codigo/Imagenes/Productos/"+j))
        sm.ids.wig.add_widget(Lista())
        for i,j in zip(['Valor Subtotal','IVa','Valor Total','Valor Total + Iva'],['88','7','82','89']):
            sm.ids.conjuntos.add_widget(Subtotales(i,j))
        return sm
        """
LoggApp().run()
