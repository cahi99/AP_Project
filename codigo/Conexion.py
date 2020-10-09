import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import pandas as pd

def conecta(credenciales='LaFrabil'):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('codigo/Empresas/'+credenciales+'.json',scope)
    client = gspread.authorize(creds)
    return client

def Datos(credenciales='LaFrabil',empresa='Productos'):
    sheet = conecta(credenciales).open(empresa).sheet1
    hoja1= pd.DataFrame(sheet.get_all_values(),columns=sheet.get_all_values()[0],header=0)
    hoja1.to_csv('codigo/Sin-Conexion/'+credenciales+'.csv')
    hoja1=hoja1[0:]
    return hoja1




