# MLOps Pipeline: KDD Cup 1999 Intrusion Detection System

Sistema de detección de intrusiones en redes basado en el dataset KDD Cup 1999, diseñado bajo un enfoque de ingeniería MLOps de grado industrial, garantizando reproducibilidad, trazabilidad y control automatizado del ciclo de vida del modelo.

---

## 1. Business Problem
En el entorno de ciberseguridad actual, la identificación temprana y precisa de tráfico malicioso en redes corporativas es crítica para mitigar brechas de seguridad. Este proyecto resuelve la detección automatizada de ataques informáticos mediante modelos de Machine Learning integrados en un pipeline de producción escalable.

## 2. Dataset
* **Origen:** KDD Cup 1999 Dataset (The Third International Knowledge Discovery and Data Mining Tools Competition).
* **Descripción:** Contiene registros de conexiones de red simuladas en un entorno de red militar de la Fuerza Aérea de EE. UU. (USAF LAN), clasificados en tráfico normal o tipos específicos de ataques (DoS, R2L, U2R, Probe).

## 3. Architecture
El pipeline de MLOps sigue una arquitectura modular y desacoplada:
1. **Ingestión y Validación:** Limpieza de datos y validación de esquemas.
2. **Entrenamiento y Registro:** Modelado estadístico y tracking de experimentos con MLflow.
3. **Servicio (Serving):** API REST ligera construida para inferencia en tiempo real.
4. **Monitoreo y Estrategia:** Detección de Data Drift (PSI) y lógica de reentrenamiento combinada con degradación de rendimiento.
5. **Contenedorización:** Empaquetado universal mediante Docker.
El siguiente diagrama técnico detalla el flujo integral de MLOps implementado en el repositorio, donde cada componente corresponde exactamente con los scripts y archivos desarrollados:





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
```

| Fase / Etapa | Componente / Archivo | Descripción del Proceso |
| :--- | :--- | :--- |
| **1. Ingesta y EDA** | Dataset KDD Cup 1999 | Carga y análisis exploratorio de datos de intrusión en red. |
| **2. Control de Calidad** | `quality_check.py` | Validación automatizada de esquemas y nulos antes del entrenamiento. |
| **3. Entrenamiento y Registro** | MLflow (`mlruns/`) | Registro de hiperparámetros, métricas y artefactos del modelo. |
| **4. Contenedorización** | Docker & FastAPI (`app.py`) | Empaquetado universal y API REST para inferencia en producción. |
| **5. Monitoreo y Simulación** | Drifts & Retrain | Evaluación de estabilidad (PSI) y lógica de reentrenamiento. |

## 5. Instrucciones de Despliegue (Reproducción)

Para garantizar la compatibilidad de entornos y evitar conflictos de versiones con scikit-learn, el modelo se genera de forma nativa directamente dentro del contenedor. Ejecutar los siguientes comandos en orden:

1. **Construir la imagen:**
   ```bash
   docker build -t kddcup-mlops-api:latest .