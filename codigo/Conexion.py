import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import pandas as pd
#pedidos=[]

def conecta(credenciales='codigo/credenciales.json'):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credenciales,scope)
    client = gspread.authorize(creds)
    return client

def Datos(empresa='Productos'):
    sheet = conecta().open(empresa).sheet1
    hoja1= pd.DataFrame(sheet.get_all_values(),columns=sheet.get_all_values()[0])
    hoja1=hoja1[1:]
    return hoja1

print(Datos())



