# MLOps Pipeline: Detección de Intrusiones en Redes (KDD Cup 1999)

## 📌 Descripción del Proyecto
Este proyecto implementa un pipeline completo de MLOps para la detección de intrusiones en redes informáticas utilizando el histórico conjunto de datos **KDD Cup 1999**. El sistema abarca todo el ciclo de vida del desarrollo: desde el análisis exploratorio de datos (EDA), preprocesamiento, entrenamiento y evaluación de modelos predictivos de Machine Learning, hasta su despliegue en una API de alto rendimiento con **FastAPI** y su posterior contenedorización mediante **Docker** para garantizar una reproducibilidad total en cualquier entorno.

---

## 🛠️ Estructura del Repositorio
- `kddcup1999.ipynb`: Notebook principal con el preprocesamiento de datos, entrenamiento de modelos, evaluación y generación de métricas.
- `app.py`: Código fuente de la API construida con FastAPI que expone endpoints para realizar inferencias y predicciones en tiempo real.
- `model.pkl`: Archivo binario con el modelo de Machine Learning entrenado y serializado.
- `Dockerfile`: Configuración oficial para empaquetar la aplicación y sus dependencias en un contenedor aislado.
- `requirements.txt`: Listado detallado de las librerías de Python necesarias para la ejecución del proyecto.
- `cm_*.png` / `confusion_matrix_*.png`: Gráficos de matrices de confusión generados durante la fase de evaluación de los modelos.

---

## 🚀 Ejecución y Despliegue Local mediante Docker

Para ejecutar el proyecto de forma aislada y reproducible, utiliza los siguientes comandos en tu terminal:

1. **Construir la imagen de Docker:**
   ```bash
   docker build -t kdd-intrusion-api .
