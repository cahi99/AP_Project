from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivymd.uix.menu import  RightContent
from Mi_Pedido import Screen3
import Conexion as data
import pandas as pd
info=data.Datos()
info2=[]
pedidos=[]
for i in info:
    info2.append(0)

class Screen2(Screen):
    def __init__(self, *args, **kwargs):
        super(Screen2,self).__init__(**kwargs)
        for i,j in zip(info['Productos'],info['Archivo_Imagen']):
            self.ids.box.add_widget(MyCard(i,"codigo/Imagenes/Productos/"+j))

class MyCard(MDCard):
    value=0
    def __init__(self, *args, **kwargs):
        super(MyCard,self).__init__(**kwargs)
        self.ids.n_producto.text=args[0]
        self.ids.id_image.source=args[1]
        self.ids.plus.icon='plus'
        self.ids.cero.text='0'
        self.ids.minus.icon='minus'
    
    def control_productos(self,nombre,icon):
        print(nombre)
        global info2
        global pedidos
        if self.ids.cero.text=='0':
            print('entro wey')
        for i in range(len(info)):
            if info['Productos'][i+1]== nombre:
                self.ids.minus.disabled= False
                self.ids.plus.disabled= False
                print(info['Productos'][i+1])
                print(icon)
                if icon== 'plus':
                    if info2[i] >= int(info['Cantidad'][i+1]):
                        print(info['Cantidad'][i+1])
                        print('si entra wey')
                        self.ids.plus.disabled= True
                    else:
                        print(info2[i])
                        info2[i]+=1
                        print(info2[i])
                if icon== 'minus':
                    print(info2[i])
                    #self.ids.minus.disabled= False
                    if info2[i]==1:
                        self.ids.minus.disabled= True
                        info2[i]=0
                    elif info2[i]==0:
                        self.ids.minus.disabled= True
                    else:
                        info2[i]-=1
                    print(info2[i])
                self.ids.cero.text= str(info2[i])
                if info2[i]>=0:
                    for k in pedidos:
                        if k[0] == info.values[i][0]:
                            pedidos.remove(k)
                    if info2[i] != 0:
                        pedidos.append([*info.values[i],info2[i]])
                
        print(pedidos)


class ProductosApp(MDApp):
    def build(self):
        return Screen2()

if __name__ == '__main__':
    ProductosApp().run()