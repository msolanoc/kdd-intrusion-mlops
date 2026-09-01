# MLOps Pipeline: KDD Cup 1999 Intrusion Detection System

Sistema de detección de intrusiones en redes basado en el dataset KDD Cup 1999, diseñado bajo un enfoque de ingeniería MLOps de grado industrial, garantizando reproducibilidad, trazabilidad y control automatizado del ciclo de vida del modelo.

---

## 1. Business Problem
En el entorno de ciberseguridad actual, la identificación temprana y precisa de tráfico malicioso en redes corporativas es crítica para mitigar brechas de seguridad. Este proyecto resuelve la detección automatizada de ataques informáticos mediante modelos de Machine Learning integrados en un pipeline de producción escalable, incorporando control de calidad de datos, tracking de experimentos y estrategias automatizadas de reentrenamiento ante la presencia de Data Drift.

## 2. Dataset
* **Origen:** KDD Cup 1999 Dataset (The Third International Knowledge Discovery and Data Mining Tools Competition).
* **Descripción:** Contiene registros de conexiones de red simuladas en un entorno de red militar de la Fuerza Aérea de EE. UU. (USAF LAN), clasificados en tráfico normal o tipos específicos de ataques (DoS, R2L, U2R, Probe).

## 3. Architecture & MLOps Lifecycle
El pipeline sigue una arquitectura modular, desacoplada y orientada a producción:

1. **Ingestión y Validación:** Carga de datos y validación automatizada de esquemas y nulos mediante scripts dedicados de control de calidad (`quality_check.py`).
2. **Entrenamiento y Registro (MLflow):** Modelado automatizado y tracking de hiperparámetros, métricas de rendimiento y artefactos del modelo almacenados localmente en `mlruns/`.
3. **Servicio (Serving - FastAPI):** API REST ligera construida en `app.py` para procesar peticiones de inferencia en tiempo real sobre nuevas conexiones de red.
4. **Monitoreo y Simulación (PSI & Drifts):** Evaluación continua de la estabilidad de las variables mediante el Índice de Estabilidad de Población (PSI) en `retrain_strategy.py` para detectar degradación o cambios en la distribución de los datos.
5. **Contenedorización (Docker):** Empaquetado universal del entorno y las dependencias para garantizar una ejecución idéntica en cualquier infraestructura.

---

## 4. Repository Structure

```text
kdd-intrusion-mlops/
├── venv/                      # Entorno virtual de desarrollo
├── src/                       # Código fuente modular (ingesta, entrenamiento, etc.)
├── mlruns/                    # Almacenamiento local de experimentos MLflow
├── app.py                     # API REST para inferencia en producción
├── retrain_strategy.py        # Lógica de decisión de reentrenamiento y PSI
├── Dockerfile                 # Configuración de contenedorización universal
├── requirements.txt           # Dependencias y librerías del proyecto
└── README.md                  # Documentación maestra del proyecto

## 5. Instrucciones de Despliegue

```bash
docker build -t kddcup-mlops-api:latest .
```

Para verificar que los endpoints responden de forma óptima y validar que el modelo predice con éxito bajo demanda, ejecuto el script de pruebas automatizadas:

```bash
python test_api.py
```