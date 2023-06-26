#mapeo paises segun orden de salario medio

def apply_rank_encoding(df, column_name):
    mean_encoding = df.groupby(column_name)['salario_eur'].mean().round()
    mean_encoding_sorted = mean_encoding.sort_values(ascending=False)
    ranked_values = mean_encoding_sorted.rank(method='first').astype(int)
    
    mapping = {value: rank for rank, value in enumerate(ranked_values, start=1)}
    mapped_values = ranked_values.map(mapping)
    
    mapping_dict = dict(zip(mean_encoding_sorted.index, mapped_values))
    df[column_name] = df[column_name].replace(mapping_dict)
    
    return df


#evauacion modelos
def valoracion_modelos(tipo, modelo, Xtest, ytest):

    y_pred = modelo.predict(Xtest)
    print("RF_scoore", r2_score(ytest , y_pred))
    print("MAE", tipo, mean_absolute_error(ytest, y_pred))
    print("MSE",tipo, mean_squared_error(ytest, y_pred))