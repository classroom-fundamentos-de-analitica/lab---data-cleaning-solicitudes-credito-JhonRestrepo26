"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #
    df.dropna(axis=0, inplace = True)
    

    df.monto_del_credito = df.monto_del_credito.str.strip('$')
    df.monto_del_credito = df.monto_del_credito.str.replace('\.00','')
    df.monto_del_credito = df.monto_del_credito.str.replace(',','')
    df.monto_del_credito = df.monto_del_credito.astype(int)
    
    #Fechas:

    df.fecha_de_beneficio=pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)
    
    #Comunas como flotante
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)
    
    # Minúsculas todo lo que sea texto, además quitar guiones:

    col_texts=['sexo','tipo_de_emprendimiento','idea_negocio','barrio','línea_credito']

    for i in col_texts:
      df[i]=df[i].str.lower()           #May en min
      df[i]=df[i].str.replace('_',' ')  #Espaciado
      df[i]=df[i].str.replace('-',' ')
    
    #Duplicados
    df.drop_duplicates(inplace = True)
    
    return df
