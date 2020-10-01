from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.gridlayout import MDGridLayout
from kivy.lang import Builder
from kivymd.uix.menu import  RightContent

class MyCard(MDCard):
    pass
class Mylist(TwoLineListItem):
    def __init__(self, *args, **kwargs):
        super(Mylist,self).__init__(**kwargs)
        self.text=args[0]
        self.secondary_text= 'Distribuidores'

class Subtotales(RightContent):
    def __init__(self, *args, **kwargs):
        super(Subtotales,self).__init__(**kwargs)
        self.ids.val.text= args[0]
        self.ids.lbl.text= args[1]

class MipedidoApp(MDApp):
    def build(self):
        pd=Builder.load_file('mipedido.kv')
        for i in range(20):
            pd.ids.scrll_v.add_widget(Mylist('producto '+str(i)))
        for i,j in zip(['Valor Subtotal','IVa','Valor Total','Valor Total + Iva'],['88','7','82','89']):
            pd.ids.conjuntos.add_widget(Subtotales(i,j))
        return pd

MipedidoApp().run()