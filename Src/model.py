import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from data_processing import csv
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


#cargamos archivo

df_processed = pd.read_csv("./data/processed.csv")

#creamos csv train y test 

train_df, test_df = train_test_split(df_processed, test_size=0.2, random_state=42)

csv("test", test_df)
csv("train", train_df)

#creacion x-y and train-test split

X = train_df.drop(columns=["salario_eur"], axis=1)
y = train_df["salario_eur"]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=42)


#model
# Definir los pasos del pipeline
steps = [
    ('scaler', StandardScaler()),  # Escalado de datos
    ('model', None)  # Modelo a evaluar (se especificará posteriormente)
]

# Crear el pipeline
pipeline = Pipeline(steps)

# Definir los hiperparámetros a ajustar para cada modelo
parameters = [
    {
        'model': [LinearRegression()]  # Regresión lineal
    },
    {
        'model': [RandomForestRegressor()],  # RandomForestRegressor
        'model__n_estimators': [10, 50, 100],  # Número de árboles en el bosque
        'model__max_depth': [None, 5, 10],  # Profundidad máxima de los árboles
    },
    {
        'model': [XGBRegressor()],  # XGBRegressor
        'model__n_estimators': [10, 50, 100],  # Número de estimadores (árboles)
        'model__max_depth': [3, 6, 9],  # Profundidad máxima de los árboles
        'model__learning_rate': [0.1, 0.01, 0.001],  # Tasa de aprendizaje
    }
]

# Realizar la búsqueda de hiperparámetros y seleccionar el mejor modelo
grid_search = GridSearchCV(pipeline, parameters, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)  # X_train y y_train son tus datos de entrenamiento

# Obtener el mejor modelo y sus hiperparámetros
best_model = grid_search.best_estimator_

import pickle

with open('./models/train_model.pkl', 'wb') as archivo_salida:
    pickle.dump(best_model, archivo_salida)

