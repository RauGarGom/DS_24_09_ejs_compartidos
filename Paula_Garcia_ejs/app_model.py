from fastapi import FastAPI, HTTPException
import os
import pickle
import uvicorn
from pydantic import BaseModel
from typing import List
# ---------------------------------------------------------------------------------

app = FastAPI()

@app.get('/')
async def home():
    return "Bienvenido a la API de Paula"

# ---------------------------------------------------------------------------------

# CSV to DB

import pandas as pd
import sqlite3

df_advertising = pd.read_csv('./data/Advertising.csv')

conn = sqlite3.connect('./data/advertising.db')
cursor = conn.cursor()

# to SQL
df_advertising.to_sql('advertising', conn, if_exists='replace', index=False)
# CIERRO, PERO RECUERD LUEGO VOLVER A LLAMAR A LA CONEXION CUNADO LO NECESITES
# conn.close()

# ---------------------------------------------------------------------------------

# 1. Endpoint de predicción

# ---------------------------------------------------------------------------------

# Cargo el modelo al iniciar la aplicación
model_path = "./data/advertising_model.pkl"

with open(model_path, 'rb') as file:
        model = pickle.load(file)



# MI CLASS PARA LA PREDICCION

class PredictData(BaseModel):
    data: List[List[float]]

@app.get('/predict')
async def predict(predict_data: PredictData):
    try:
        features = predict_data.data
        if not all(len(feature) == 3 for feature in features):
            raise HTTPException(status_code=422, detail="Cada entrada debe tener exactamente 3 valores: tv, radio, newpaper")
        predictions = model.predict(features)
        return {"prediction": predictions.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error durante la predicción: {str(e)}")



# class Gastos(BaseModel):
#     TV: float
#     radio: float
#     newpaper: float



# @app.post('/predict')
# async def predict(gastos: Gastos):
#     """
#     REALIZA UNA PREDICCION DE GASTOS :)
#     """

#     # Realizar la predicción
#     try:
#         features = [[gastos.TV, gastos.radio, gastos.newpaper]]
#         prediction = model.predict(features)
#         return {"predicted_sales": prediction[0]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail= str(e))



# ---------------------------------------------------------------------------------

# 2. Endpoint de ingesta de datos

# ---------------------------------------------------------------------------------

from typing import List

class RegistroMultiple(BaseModel):
    data: List[List[float]]

@app.post('/ingest')
async def ingest_data(registros: RegistroMultiple):
    """
    REALIZA UNA INGESTA DE MÚLTIPLES REGISTROS
    """
    try:
    
        for registro in registros.data:
            if len(registro) != 4:
                raise HTTPException(
                    status_code=400,
                    detail="Cada registro debe contener exactamente 4 valores: TV, radio, newpaper, sales."
                )
        

        with sqlite3.connect('./data/advertising.db') as conn:
            cursor = conn.cursor()
    
            for registro in registros.data:
                query = """
                    INSERT INTO advertising (TV, radio, newpaper, sales)
                    VALUES (?, ?, ?, ?)
                """
                cursor.execute(query, tuple(registro))
            conn.commit()
        
        return {'message': 'Datos ingresados correctamente'}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# class NuevoRegistro(BaseModel):
#     TV: float
#     radio: float
#     newpaper: float
#     sales: float


# @app.post('/ingest')
# async def ingest_data(nuevo_registro: NuevoRegistro):
#     """
#     REALIZA UNA INGESTA DE GASTOS :)
#     """
#     try:
#         query = """
#             INSERT INTO advertising (TV, radio, newpaper, sales)
#             VALUES (?, ?, ?, ?)
#         """ 
#         cursor.execute(query, (nuevo_registro.TV, nuevo_registro.radio, nuevo_registro.newpaper, nuevo_registro.sales))
#         conn.commit()  
        
#         return {'message': 'Datos ingresados correctamente'}
    
#     except Exception as e:
#         raise HTTPException(status_code=500, detail= str(e))
  
#   # NO NECESITO PONER QU SE ACTUALICE, NO VAYA A CAUSAR ERRORES SINTETICOS EN EL MODELO




# ---------------------------------------------------------------------------------

# 3. Endpoint de reentramiento del modelo

# ---------------------------------------------------------------------------------

@app.post('/retrain')
async def retrain_model():
    try:
        data = pd.read_sql_query("SELECT * FROM advertising", conn)
        X = data[["TV", "radio", "newpaper"]]
        y = data["sales"]
        model.fit(X, y)
        model_path = "data/advertising_model.pkl"
        with open(model_path, "wb") as file:
            pickle.dump(model, file)
        return {'message': 'Modelo reentrenado correctamente.'}
    except Exception as e:
        raise HTTPException(status_code=500, detail= str(e))






# ---------------------------------------------------------------------------------

# Ejecutar la aplicación

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)






# ---------------------------------------------------------------------------------

# python app_model.py

# ---------------------------------------------------------------------------------


