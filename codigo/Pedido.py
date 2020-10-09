from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.banner import MDBanner
from kivymd.uix.menu import  RightContent
import Conexion as data
import Mis_Pedidos as p
#import Conexion as Data
#from Conexion import Envio as Data
from functools import reduce
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import pandas as pd
conjunt=[]


def valores(data,_iva=0.12):
  valor_subtotal=0
  iva=0
  valor_total=0
  for i in data:
    try:
        valor_subtotal+=float(i[1])*i[5]
        iva+=(float(i[1])*_iva)*i[5]
        valor_total+=(float(i[1])*(_iva+1))*i[5]
    except:
        valor_subtotal+=float(i[2])*i[6]
        iva+=(float(i[2])*_iva)*i[6]
        valor_total+=(float(i[2])*(_iva+2))*i[6]
  return [valor_subtotal,iva,valor_total]

class Screen5(Screen):
    dialog = None

    def on_enter(self):
        global dialog
        dialog=p.Empresa
        print('hola 1')
        print(conjunt)
        print(dialog)
        dialog=pd.read_csv('codigo/Pedidos/'+dialog,header=1,index_col=0)
        print(dialog)
        for i in range(len(dialog)):
            conjunt.append(i)
            print(i+1)
            if i < len(dialog):
                self.ids.scrll_v.add_widget(Mylist(str(dialog['Productos'][i+1])))
    

class Mylist(TwoLineListItem):
    def __init__(self, *args, **kwargs):
        super(Mylist,self).__init__(**kwargs)
        self.text=args[0]
        self.secondary_text= 'Distribuidores'

class PedidoApp(MDApp):
    def build(self):
        return Screen5()

if __name__ == '__main__':
    PedidoApp().run()