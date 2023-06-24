import pandas as pd
import numpy as np

df_original = pd.read_csv("./data/raw/ds_salaries.csv")


#cambio usd a eur

tasa_cambio = 0.92

df_original["salario_eur"] = df_original["salary_in_usd"] * tasa_cambio

#sustituimos variables categoricas por el salario medio de cada tipo.

mean_encoding_experience_level = df_original.groupby('experience_level')['salario_eur'].mean()
df_original["experience_level_mean"] = df_original['experience_level'].map(mean_encoding_experience_level)

mean_encoding_employment_type = df_original.groupby('employment_type')['salario_eur'].mean()
df_original["employment_type_mean"] = df_original['employment_type'].map(mean_encoding_employment_type)

mean_encoding_job_title = df_original.groupby('job_title')['salario_eur'].mean()
df_original["job_title_mean"] = df_original['job_title'].map(mean_encoding_job_title)

mean_encoding_company_location = df_original.groupby('company_location')['salario_eur'].mean()
df_original["company_location_mean"] = df_original['company_location'].map(mean_encoding_company_location)

mean_encoding_employee_location = df_original.groupby('employee_residence')['salario_eur'].mean()
df_original["employee_location_mean"] = df_original['employee_residence'].map(mean_encoding_employee_location)

mean_encoding_company_size = df_original.groupby('company_size')['salario_eur'].mean()
df_original["company_size_mean"] = df_original['company_size'].map(mean_encoding_company_size)

mean_encoding_remote_ratio = df_original.groupby('employment_type')['salario_eur'].mean()
df_original["remote_ratio_mean"] = df_original['employment_type'].map(mean_encoding_remote_ratio)

#asignamos variables a df_processed

df_processed = df_original[['work_year','salario_eur', 'experience_level_mean', 'employment_type_mean',
       'job_title_mean', 'company_location_mean', 'employee_location_mean',
       'company_size_mean', 'remote_ratio_mean']]

#funcion crear csv

def csv(nombre_archivo, archivo_guardar):


    ruta_archivo = './data/' + nombre_archivo + '.csv'
    archivo_guardar.to_csv(ruta_archivo, index=False)

#extraemos processed
csv("processed", df_processed)
