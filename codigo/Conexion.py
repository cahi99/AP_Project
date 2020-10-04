import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import pandas as pd
#pedidos=[]

def Datos(credenciales='codigo/credenciales.json',empresa='Datos Prueba'):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credenciales,scope)
    client = gspread.authorize(creds)
    sheet = client.open(empresa).sheet1
    hoja1= pd.DataFrame(sheet.get_all_values(),columns=sheet.get_all_values()[0])
    hoja1=hoja1[1:]
    return hoja1
"""
def Envio(credenciales='codigo/credenciales.json',empresa='Datos Prueba',datos=pedidos):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credenciales,scope)
    client = gspread.authorize(creds)
    sheet = client.open(empresa).worksheet('Pedido')
    print('si entra wey')
    #hoja1= pd.DataFrame(sheet.get_all_values())
    #hoja1=hoja1[1:]
    for i in datos:
        sheet.insert_row(i)
    """

print(Datos())



