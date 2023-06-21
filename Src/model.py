import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split


#cargamos archivo

df = pd.read_csv("./data/train.csv")


#creacion x-y and train-test split

X = df.drop(columns=["salario_eur"], axis=1)
y = df["salario_eur"]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=42)


#baselinemodel

from sklearn.linear_model import LinearRegression

baseline_model = LinearRegression()
baseline_model.fit(X_train, y_train)

import pickle

with open('./models/trained_model.pkl', 'wb') as archivo_salida:
    pickle.dump(baseline_model, archivo_salida)

