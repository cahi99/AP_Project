import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import pandas as pd

def conecta(credenciales='credenciales'):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('codigo/Empresas/'+credenciales+'.json',scope)
    client = gspread.authorize(creds)
    return client

def Datos(credenciales='credenciales',empresa='Productos'):
    sheet = conecta(credenciales).open(empresa).sheet1
    hoja1= pd.DataFrame(sheet.get_all_values(),columns=sheet.get_all_values()[0])
    hoja1=hoja1[1:]
    return hoja1




