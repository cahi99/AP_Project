from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivymd.uix.menu import  RightContent

class MyCard(MDCard):
    def __init__(self, *args, **kwargs):
        super(MyCard,self).__init__(**kwargs)
        self.ids.n_producto.text=args[0]
        self.ids.id_image.source=args[1]
        self.ids.plus.icon='plus'
        self.ids.cero.text='0'
        self.ids.minus.icon='minus'



class ProductosApp(MDApp):
    def build(self):
        DR =Builder.load_file('productos.kv')
        for i,j in zip(['Plato 6','Plato 8','Plato 9'],['plato_6.jpg','plato_8.jpg','plato_9.jpg']):
            DR.ids.box.add_widget(MyCard(i,"codigo/Imagenes/Productos/"+j))
        #DR.ids.box.add_widget(MyCard("Plato 8","codigo/Imagenes/Productos/plato_8.jpg"))
        #DR.ids.box.add_widget(MyCard("Plato 9","codigo/Imagenes/Productos/plato_9.jpg"))
        return DR

if __name__ == '__main__':
    ProductosApp().run()