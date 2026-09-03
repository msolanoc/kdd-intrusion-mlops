# 🛡️ MLOps Pipeline: KDD Cup 1999 Intrusion Detection System

Sistema de detección de intrusiones en redes basado en el conjunto de datos KDD Cup 1999, diseñado bajo un enfoque integral de ingeniería MLOps de grado industrial para garantizar reproducibilidad, trazabilidad, despliegue continuo y monitoreo automatizado del ciclo de vida del modelo.

---

## 🚀 Enlaces de Producción (Live Demos)

- **Frontend Interactivo (Streamlit Cloud):** [https://kdd-intrusion-mlops.streamlit.app](https://kdd-intrusion-mlops.streamlit.app)
- **Backend API (FastAPI Docs / Swagger UI en Render):** [https://kdd-intrusion-mlops.onrender.com/docs](https://kdd-intrusion-mlops.onrender.com/docs)
- **Endpoint de Inferencia Directa:** `POST https://kdd-intrusion-mlops.onrender.com/predict`

---

## 1. Problema de Negocio y Criterio de Decisión

En entornos de ciberseguridad corporativa, la identificación temprana de tráfico malicioso es crítica. El costo operativo de un **Falso Negativo (FN)** —permitir que un ataque real pase desapercibido como tráfico normal— es potencialmente catastrófico para la infraestructura.

Por este motivo, la optimización algorítmica priorizó maximizar el **Recall** (~99.8%) sin sacrificar la estabilidad general del sistema (F1-Score y Precision).

- **Modelo Seleccionado:** **Random Forest Classifier** (Scikit-Learn).
- **Justificación:** Capacidad superior para modelar correlaciones e interacciones no lineales complejas en más de 40 características de red, manteniendo alta resiliencia frente al sobreajuste (*overfitting*).

---

## 2. Dataset

- **Origen:** KDD Cup 1999 Dataset (The Third International Knowledge Discovery and Data Mining Tools Competition).
- **Descripción:** Registros estructurados de conexiones de red simuladas en un entorno de red militar (USAF LAN), catalogadas como tráfico normal o vectores de ataque (DoS, R2L, U2R, Probe).

---

## 3. Arquitectura y Ciclo de Vida MLOps

El pipeline implementa un diseño modular y desacoplado:

1. **Ingesta, Validación y EDA:** Análisis exploratorio y control de calidad de datos (`kddcup1999.ipynb`, `quality_check.py`) con validación de esquemas y nulos.
2. **Entrenamiento y Tracking (MLflow):** Registro de experimentos, comparación de métricas (Precision, Recall, F1) y versionado de hiperparámetros y artefactos (`model.pkl`).
3. **Servicio en Producción (FastAPI):** API REST (`app.py`) conteinerizada para servir inferencias de baja latencia.
4. **Monitoreo y Simulación de Data Drift:** Detección de cambios de distribución en producción (`simulate_drift.py`) y protocolo automatizado de reentrenamiento basado en métricas estadísticas como el Population Stability Index (PSI) (`retrain_strategy.py`).
5. **Interfaz de Usuario (Streamlit):** Panel interactivo (`streamlit_app.py`) para pruebas y auditoría manual de tráfico en vivo.
6. **Contenedorización (Docker):** Empaquetado estandarizado con dependencias fijadas (`requirements.txt`) para asegurar portabilidad entre entornos.

---

## 4. Estructura del Repositorio

```text
kdd-intrusion-mlops/
├── kddcup1999.ipynb          # Notebook con EDA, preprocesamiento y experimentación
├── app.py                    # Servidor API REST con FastAPI (Backend)
├── streamlit_app.py          # Dashboard interactivo para operadores (Frontend)
├── test_api.py               # Pruebas unitarias automatizadas (pytest)
├── simulate_drift.py         # Módulo de simulación de Data Drift en producción
├── retrain_strategy.py       # Estrategia y umbrales de reentrenamiento (PSI)
├── quality_check.py          # Script de validación de calidad e integridad de datos
├── model.pkl                 # Modelo serializado final (Random Forest)
├── Dockerfile                # Definición de la imagen Docker para producción
├── requirements.txt          # Dependencias y versiones fijadas
├── confusion_matrix_*.png    # Evidencias visuales de evaluación y matrices de confusión
└── README.md                 # Documentación técnica maestra