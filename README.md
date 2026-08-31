# MLOps Pipeline: Detección de Intrusiones (KDD Cup 1999)

## 📌 Descripción del Proyecto
Este proyecto implementa un pipeline completo de MLOps para la detección de intrusiones en redes utilizando el conjunto de datos KDD Cup 1999.

## 🛠️ Estructura
- app.py: Código de la API
- model.pkl: Modelo entrenado
- Dockerfile: Contenedor
- requirements.txt: Dependencias
## 🐳 Ejecución con Docker
1. Construir la imagen:
   ```bash
   docker build -t kdd-intrusion-api .