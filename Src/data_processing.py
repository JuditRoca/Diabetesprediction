import pandas as pd
import numpy as np

df_original = pd.read_csv("./data/raw/ds_salaries.csv")


#cambio usd a eur

tasa_cambio = 0.92

df_original["salario_eur"] = df_original["salary_in_usd"] * tasa_cambio

#groupby experiencia y salarios

exp_sal = df_original.groupby('experience_level')['salario_eur'].mean().round(2)

# Reemplazar las etiquetas por los salarios medios correspondientes
df_original['experience_level'] = df_original['experience_level'].map(exp_sal)

# Mapear las etiquetas de tamaño de empresa a valores numéricos
mapping = {'S': 1, 'M': 2, 'L': 3}
df_original['company_size'] = df_original['company_size'].map(mapping)

#encoder label de employment_type y job_title
from sklearn.preprocessing import LabelEncoder
cols = ['employment_type','job_title','employee_residence','company_location']
df_original[cols]=df_original[cols].apply(LabelEncoder().fit_transform)

#Eliminar variables redundantes.
df_original.drop(columns=["salary","salary_currency","salary_in_usd"], inplace=True)

from sklearn.model_selection import train_test_split

train_df, test_df = train_test_split(df_original, test_size=0.2, random_state=42)

def csv(nombre_archivo, archivo_guardar):


    ruta_archivo = './data/' + nombre_archivo + '.csv'
    archivo_guardar.to_csv(ruta_archivo, index=False)

csv("processed", df_original)
csv("test", test_df)
csv("train", train_df)