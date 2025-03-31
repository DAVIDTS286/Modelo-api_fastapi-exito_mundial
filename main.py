from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Cargar modelo y columnas
modelo = joblib.load("modelo_vgsales.pkl")
columnas = joblib.load("columnas_vgsales.pkl")

# Definir esquema de entrada
class Juego(BaseModel):
    Year: int
    Genre: str
    Platform: str
    NA_Sales: float
    EU_Sales: float
    JP_Sales: float
    Other_Sales: float

@app.post("/predict")
def predict(juego: Juego):
    try:
        df = pd.DataFrame([juego.dict()])
        df = pd.get_dummies(df)

        # Añadir columnas faltantes
        for col in columnas:
            if col not in df.columns:
                df[col] = 0
        df = df[columnas]

        pred = modelo.predict(df)[0]
        return {"exito_global": bool(pred)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
