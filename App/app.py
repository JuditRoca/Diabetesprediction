import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle
import streamlit as st
from PIL import Image

with open('../models/train_model.pkl', 'rb') as archivo_entrada:
    model_pretrained = pickle.load(archivo_entrada)

#lista valores pais empleado
paises_trabajador = {
    'IL': 78, 'MY': 77, 'PR': 76, 'US': 75, 'CA': 74, 'CN': 73, 'NZ': 72, 'BA': 71, 'IE': 70, 'DO': 69,
    'RU': 68, 'SE': 67, 'JP': 66, 'UZ': 65, 'CH': 64, 'IQ': 59, 'IR': 60, 'JE': 61, 'DZ': 62, 'AE': 63,
    'LT': 58, 'DE': 57, 'MX': 56, 'GB': 55, 'SG': 54, 'BG': 53, 'AU': 52, 'NL': 51, 'HR': 50, 'CL': 49,
    'BE': 48, 'AT': 47, 'FI': 46, 'HK': 45, 'NG': 44, 'CO': 43, 'CY': 42, 'SI': 41, 'FR': 40, 'ES': 39,
    'LU': 38, 'LV': 37, 'UA': 36, 'GR': 35, 'PT': 34, 'BO': 33, 'RO': 32, 'IT': 31, 'AM': 29, 'KW': 30,
    'BR': 28, 'CF': 27, 'PH': 26, 'PL': 25, 'KE': 24, 'CZ': 23, 'IN': 22, 'AR': 21, 'VN': 20, 'AS': 19,
    'EE': 18, 'DK': 17, 'TN': 16, 'PK': 15, 'HU': 14, 'MT': 13, 'RS': 12, 'TH': 11, 'EG': 10, 'HN': 8,
    'CR': 9, 'TR': 7, 'GH': 6, 'MD': 5, 'ID': 4, 'SK': 3, 'MA': 2, 'MK': 1
}

#lista valores pais empresa

paises_empresa = {
    'IL': 72, 'PR': 71, 'US': 70, 'RU': 69, 'CA': 68, 'NZ': 67, 'BA': 66, 'IE': 65, 'JP': 64, 'SE': 63,
    'CN': 58, 'IR': 59, 'IQ': 60, 'DZ': 61, 'AE': 62, 'MX': 57, 'LT': 56, 'DE': 55, 'GB': 54, 'CH': 53,
    'AU': 52, 'NL': 51, 'NG': 50, 'BE': 49, 'HR': 48, 'AT': 47, 'FI': 46, 'FR': 45, 'HK': 44, 'CO': 43,
    'SI': 42, 'PL': 41, 'LV': 40, 'UA': 39, 'ES': 38, 'RO': 37, 'SG': 36, 'GR': 35, 'PT': 34, 'PH': 31,
    'AM': 32, 'CR': 33, 'CF': 30, 'EE': 29, 'DK': 28, 'BS': 27, 'KE': 26, 'LU': 25, 'IT': 24, 'BR': 23,
    'CL': 22, 'MY': 21, 'CZ': 20, 'ID': 19, 'IN': 18, 'AS': 17, 'MT': 16, 'HU': 15, 'AR': 14, 'TH': 13,
    'EG': 12, 'PK': 10, 'HN': 11, 'TR': 9, 'GH': 8, 'MD': 7, 'SK': 6, 'VN': 5, 'AL': 3, 'MA': 4, 'BO': 2,
    'MK': 1
}


st.set_page_config(page_title="Salary Prediction", page_icon=":moneybag:",layout="wide",
     initial_sidebar_state="expanded")

df_processed = pd.read_csv("../data/processed.csv")
df_raw = pd.read_csv("../data/Raw/ds_salaries.csv")


def main():
    col1, col2 = st.columns((1,2))

    with col1:
        st.write(' ')

    with col2:
        st.image("../Data/portada.jpg")


    st.sidebar.header('Paramentros personalizados')
    # Página prediccion
    def user_input_parameters():

        #Nivel experiencia
        Año = st.sidebar.slider('Año', 2020, 2023)
        Nivel_experiencia = st.sidebar.selectbox('Nivel de experiencia', ("EN", "MI", "SE", "EX"))
        if Nivel_experiencia == "EN":
            Nivel_experiencia = 1
        elif Nivel_experiencia == "MI":
            Nivel_experiencia = 2
        elif Nivel_experiencia == "SE":
            Nivel_experiencia = 3
        elif Nivel_experiencia == "EX":
            Nivel_experiencia = 4
        #Tipo contrato
        Tipo_contrato = st.sidebar.selectbox('Tipo de contrato', ('FT', 'CT', 'FL', 'PT'))
        if Tipo_contrato == "FT":
            Tipo_contrato = 2
        elif Tipo_contrato == "CT":
            Tipo_contrato = 0
        elif Tipo_contrato == "FL":
            Tipo_contrato = 1
        elif Tipo_contrato == "PT":
            Tipo_contrato = 3
        #Puesto trabajo
        Puesto_trabajo = st.sidebar.selectbox('Puesto de trabajo', ('scientist','Data Science','cloud',
    'Data Analyst','Data Analytics','Data Engineer','Data Strategist','Machine Learning','ML','AI','MLOps','Head'))
        if Puesto_trabajo == "scientist":
            Puesto_trabajo = 1
        elif Puesto_trabajo == "Data Science":
            Puesto_trabajo = 1
        elif Puesto_trabajo == "cloud":
            Puesto_trabajo = 2
        elif Puesto_trabajo == "Data Analyst":
            Puesto_trabajo = 3
        elif Puesto_trabajo == "Data Analytics":
            Puesto_trabajo = 3
        elif Puesto_trabajo == "Data Engineer":
            Puesto_trabajo = 3
        elif Puesto_trabajo == "Data Strategist":
            Puesto_trabajo = 3
        elif Puesto_trabajo == "Machine Learning":
            Puesto_trabajo = 4
        elif Puesto_trabajo == "ML":
            Puesto_trabajo = 4
        elif Puesto_trabajo == "AI":
            Puesto_trabajo = 4
        elif Puesto_trabajo == "MLOps":
            Puesto_trabajo = 4
        elif Puesto_trabajo == "Head":
            Puesto_trabajo = 5
        else:
            Puesto_trabajo = 6
        #Ratio remoto
        Ratio_remoto = st.sidebar.selectbox('Ratio Remoto', ('100','50','0',))
        if Ratio_remoto == "100":
            Ratio_remoto = 100
        elif Ratio_remoto == "50":
            Ratio_remoto = 50
        elif Ratio_remoto == "0":
            Ratio_remoto = 0
        #pais empleado
        Pais_residencia_trabajador = st.sidebar.selectbox('Pais trabajador', sorted(paises_trabajador.keys()))
        valor_asignado_trab = paises_trabajador[Pais_residencia_trabajador]
        #Pais empresa
        Pais_empresa = st.sidebar.selectbox('Pais empresa', sorted(paises_trabajador.keys()))
        valor_empresa = paises_empresa[Pais_empresa]
        #Tamaño empresa
        Tamaño_empresa = st.sidebar.selectbox('Tamaño empresa', ('S','M','L',))
        if Tamaño_empresa == "S":
            Tamaño_empresa = 0
        elif Tamaño_empresa == "M":
            Tamaño_empresa = 1
        elif Tamaño_empresa == "L":
             Tamaño_empresa = 2

        data = {'Nivel_experiencia' : Nivel_experiencia,
                'Tipo_contrato':Tipo_contrato,
                'Puesto_trabajo':Puesto_trabajo,
                'Ratio_remoto': Ratio_remoto,
                'Pais_residencia_trabajador': valor_asignado_trab,
                "Pais_empresa": valor_empresa,
                "Año" : Año,
                "Tamaño_empresa": Tamaño_empresa
               }
        
        features = pd.DataFrame(data, index=[0])
        return features
    
    df = user_input_parameters()
    prediccion = model_pretrained.predict(df)
    st.success("El salario estimado sería de: " + str(round(prediccion[0], 2)))

if __name__ == '__main__':
    main()