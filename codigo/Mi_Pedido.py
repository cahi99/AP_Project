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
    dialog = None
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


    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Desea enviar este pedido?",
                buttons=[
                    MDFlatButton(
                        text="CANCELAR",
                        on_release=self.dialog_close
                    ),
                    MDFlatButton(
                        text="ENVIAR",
                        on_release=lambda a: self.Envio()
                    ),
                ],
            )
        self.dialog.open()
    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)

    def Envio(self,empresa='Productos',datos=conjunt):
        self.dialog.dismiss(force=True)
        conecta=data.conecta(credenciales=p.Empresa)
        sheet1= conecta.open(empresa).sheet1
        sheet = conecta.open(empresa).worksheet('Pedido')
        for i in datos:
            sheet.insert_row(i)
        hoja1= pd.DataFrame(sheet1.get_all_values(),columns=sheet1.get_all_values()[0])
        hoja1=hoja1[1:]
        hoja2= pd.DataFrame(sheet.get_all_values())
        for j in range(len(hoja2.values)+1):
            for i in range(len(hoja1[0:])+1):
              if i+1< len(hoja1) or j<len(hoja2.values):
                  print(i+1,j)
                  if hoja1['Productos'][i+1]==hoja2.values[j-1][0]: 
                    print(hoja1['Productos'][i+1],hoja2.values[j-1][0])
                    sheet1.update_cell(i+2,4,int(hoja1['Cantidad'][i+1])-int(hoja2.values[j-1][5]))
                    if j!=0:
                      sheet.update_cell(j,4,int(hoja2.values[j-1][3])-int(hoja2.values[j-1][5]))
                    print(int(hoja2.values[j-1][5]))
                    break
        
        print('si entra wey')
        print(datos)

        """
        hoja1= pd.DataFrame(sheet.get_all_values(),columns=sheet.get_all_values()[0])
        hoja1=hoja1[1:]
        #hoja1= pd.DataFrame(sheet.get_all_values())
        #hoja1=hoja1[1:]
    
        """
#class MyButton(MDFlatButton):


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