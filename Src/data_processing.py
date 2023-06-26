import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_original = pd.read_csv("./data/raw/ds_salaries.csv")


#cambio usd a eur

tasa_cambio = 0.92

df_original["salario_eur"] = df_original["salary_in_usd"] * tasa_cambio
df_original.drop(columns=["salary", 'salary_currency', 'salary_in_usd'], inplace=True)

#job_title 
patterns = {                      #Lista de palabras sustituibles
    'scientist': 1,
    'Data Science':1,
    'cloud': 2,
    'Data Analyst':3,
    'Data Analytics':3,
    'Data Engineer':3,
    'Data Strategist':3,
    'Machine Learning' : 4,
    'ML' : 4,
    'AI':4,
    'MLOps': 4,
    'Head': 5,}

default_value = 6  #valor para los que no cumplan patterns

df_original['job_title_map'] = 0   # Crea la nueva columna y asigna el valor predeterminado (0)

for pattern, value in patterns.items():    # Itera sobre los patrones y actualiza los valores en la nueva columna
    df_original.loc[df_original['job_title'].str.contains(pattern, case=False), 'job_title_map'] = value

from formulas import apply_rank_encoding

apply_rank_encoding(df_original, "employee_residence")    #residencia empleado
apply_rank_encoding(df_original, "company_location")    #residencia compañia

#cambiamios experience_level
df_original["experience_level"] = df_original["experience_level"].replace({"EN": 1, "MI": 2, "SE": 3, "EX": 4})


#employment type
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df_original['employment_type_encoded'] = label_encoder.fit_transform(df_original['employment_type'])


#company size
size_mapping = {'S': 0, 'M': 1, 'L': 2}
df_original['company_size'] = df_original['company_size'].replace(size_mapping)

#asignamos variables a df_processed

df_processed = df_original[['work_year','salario_eur', 'experience_level', 'employment_type_encoded',
       'job_title_map', 'company_location', 'employee_residence',
       'company_size', 'remote_ratio']]

#funcion crear csv

def csv(nombre_archivo, archivo_guardar):


    ruta_archivo = './data/' + nombre_archivo + '.csv'
    archivo_guardar.to_csv(ruta_archivo, index=False)

#extraemos processed
csv("processed", df_processed)
