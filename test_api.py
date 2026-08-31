"""
=============================================================================
Título: Script de Pruebas Automatizadas para la API de Detección de Intrusiones
Proyecto: MLOps Pipeline - KDD Cup 1999
Descripción: Conjunto de pruebas unitarias y de integración utilizando TestClient
             para validar el funcionamiento de los endpoints, esquemas de datos,
             inferencias del modelo y manejo de errores de la API en FastAPI.
=============================================================================
"""

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_main():
    """Valida que el endpoint raíz responda correctamente y la API esté activa."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Activa"}

def test_predict_valid():
    """Valida que un request con características válidas retorne código 200
    y la estructura de predicción y probabilidad esperada por la rúbrica."""
    # Lista de características simulada ajustada al formato de entrada
    payload = {"features": [0.0] * 41} 
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "probability" in data

def test_predict_invalid_schema():
    """Valida el comportamiento ante un input inválido (tipo de dato incorrecto),
    esperando un código de error de validación 422 de Pydantic."""
    payload = {"features": "esto_debe_ser_una_lista"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  # Error de validación de esquema