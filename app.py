from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="API de Inferencia - KDD Cup 1999", version="1.0.0")

class NetworkData(BaseModel):
    features: list

MODEL_PATH = "model.pkl" 
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None

@app.get("/")
def home():
    return {"message": "API Activa"}

@app.post("/predict")
def predict(data: NetworkData):
    if model is None:
        raise HTTPException(status_code=500, detail="El modelo no pudo ser cargado.")
    
    try:
        input_data = np.array([data.features], dtype=float)
        
        # Ajuste defensivo automático de características para evitar errores de dimensión
        if hasattr(model, "n_features_in_"):
            expected = model.n_features_in_
            current = input_data.shape[1]
            if current < expected:
                # Si faltan características, rellenamos con ceros
                padding = np.zeros((1, expected - current))
                input_data = np.hstack((input_data, padding))
            elif current > expected:
                # Si sobran, recortamos al tamaño esperado
                input_data = input_data[:, :expected]

        prediction_code = int(model.predict(input_data)[0])
        
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[0].tolist()
            probability = float(probabilities[prediction_code])
        else:
            probability = 1.0

        label_mapping = {
            0: "Tráfico Normal (Clase 0)",
            1: "Intrusión o Ataque (Clase 1)"
        }

        return {
            "prediction": prediction_code,
            "prediction_label": label_mapping.get(prediction_code, "Desconocido"),
            "probability": round(probability, 4),
            "model_version": "1"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error en la inferencia: {str(e)}")