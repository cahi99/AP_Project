from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.gridlayout import MDGridLayout
from kivy.lang import Builder
from kivymd.uix.menu import  RightContent
import Productos as p
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
    valor_subtotal+=float(i[1])*i[5]
    iva+=(float(i[1])*_iva)*i[5]
    valor_total+=(float(i[1])*(_iva+1))*i[5]
  return [valor_subtotal,iva,valor_total]

class Screen3(Screen):
    def __init__(self, *args, **kwargs):
        super(Screen3,self).__init__(**kwargs)
        #self.ids.inviar.bind(on_press= lambda a:Data(datos=p.pedidos))
        print('holita')
    
    def on_pre_enter(self):
        self.ids.conjuntos.clear_widgets()
    def on_enter(self):
        #conjunt=p.pedidos
        print(conjunt)
        self.ids.scrll_v.clear_widgets()
        for i in p.pedidos:
            conjunt.append(i)
            self.ids.scrll_v.add_widget(Mylist('producto '+str(i[0])))
        for i,j in zip(['Valor Subtotal','IVA','Valor Total'],valores(p.pedidos)):
            #print('holata')
            self.ids.conjuntos.add_widget(Subtotales(i,str(j)))
    def Envio(self,credenciales='codigo/credenciales.json',empresa='Datos Prueba',datos=conjunt):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(credenciales,scope)
        client = gspread.authorize(creds)
        sheet = client.open(empresa).worksheet('Pedido')
        print('si entra wey')
        print(datos)
        #hoja1= pd.DataFrame(sheet.get_all_values())
        #hoja1=hoja1[1:]
        for i in datos:
            sheet.insert_row(i)
    

class MyCard(MDCard):
    pass
class Mylist(TwoLineListItem):
    def __init__(self, *args, **kwargs):
        super(Mylist,self).__init__(**kwargs)
        self.text=args[0]
        self.secondary_text= 'Distribuidores'

class Subtotales(MDGridLayout):
    def __init__(self, *args, **kwargs):
        super(Subtotales,self).__init__(**kwargs)
        self.ids.val.text= args[0]
        self.ids.lbl.text= args[1]

class MipedidoApp(MDApp):
    def build(self):
        return Screen3()

if __name__ == '__main__':
    MipedidoApp().run()