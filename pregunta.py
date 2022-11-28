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
    
    #Columna monto:

    df.monto_del_credito = df.monto_del_credito.str.strip('$')
    df.monto_del_credito = df.monto_del_credito.str.replace('\.00','')
    df.monto_del_credito = df.monto_del_credito.str.replace(',','')
    
    #Fechas:

    df.fecha_de_beneficio=pd.to_datetime(df.fecha_de_beneficio)
    
    #Comunas como entero
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)
    
    # Minúsculas todo lo que sea texto:

    col_texts=['sexo','tipo_de_emprendimiento','idea_negocio','barrio','línea_credito']

    for i in col_texts:
      df[i]=df[i].str.lower()
    
    #Eliminar duplicados y NAN's

    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)
    
    return df
