import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from data_processing import csv
from sklearn.linear_model import LinearRegression
import pickle

#cargamos archivo

df_processed = pd.read_csv("./data/processed.csv")

#creamos csv train y test 
from sklearn.model_selection import train_test_split

train_df, test_df = train_test_split(df_processed, test_size=0.2, random_state=42)

csv("test", test_df)
csv("train", train_df)

#creacion x-y and train-test split

X = train_df.drop(columns=["salario_eur"], axis=1)
y = train_df["salario_eur"]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=42)


#baselinemodel



baseline_model = LinearRegression()
baseline_model.fit(X_train, y_train)



with open('./models/trained_model.pkl', 'wb') as archivo_salida:
    pickle.dump(baseline_model, archivo_salida)

