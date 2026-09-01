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

```mermaid
graph TD
    %% Estilo y colores profesionales
    classDef source fill:#f9f,stroke:#333,stroke-width:2px;
    classDef process fill:#bbf,stroke:#333,stroke-width:2px;
    classDef storage fill:#fbf,stroke:#333,stroke-width:2px;
    classDef deploy fill:#bfb,stroke:#333,stroke-width:2px;

    %% Flujo del Pipeline MLOps
    A[KDD Cup 1999 Raw Data] -->|src/ingestion/ingest.py| B(Data Ingestion & Validation)
    B -->|Cleaned Data| C(Feature & Model Training)
    C -->|src/training/train.py| D[MLflow Tracking Server]
    
    subgraph Model Registry & Artifacts
        D -->|Metrics & Params| E[(mlruns/ Local Store)]
        D -->|Serialized Model| F(Best Candidate Model .pkl)
    end

    F -->|Containerization| G(Dockerfile)
    G -->|Build Image| H[kdd-intrusion-api Image]
    
    H -->|Docker Run / Local Serving| I(app.py - FastAPI / REST API)
    
    I -->|Inference Production| J(Real-time Intrusion Detection)
    
    %% Monitoreo y Estrategia Avanzada
    J --> K(retrain_strategy.py)
    
    subgraph Monitoring & Audit
        K --> L1[Data Drift Analysis - PSI]
        K --> L2[Model Performance Metrics]
        K --> L3[System Resource Metrics]
    end

    L1 --> M{Threshold Exceeded?}
    L2 --> M
    L3 --> M
    
    M -->|Yes - Trigger Alert & Retrain| C
    M -->|No - Stable Production| J

    class A source;
    class B,C,I,K process;
    class D,E,F storage;
    class G,H deploy;

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

## Arquitectura del Sistema

```mermaid
graph TD
    A[Dataset KDD Cup 1999] --> B[Pipeline de Datos & EDA]
    B --> C[Control de Calidad: quality_check.py]
    C --> D[Entrenamiento & Registro: MLflow]
    D --> E[Contenedorización: Docker & FastAPI]
    E --> F[Monitoreo & Simulación: Drift & Retrain]
```

## 5. Instrucciones de Despliegue (Reproducción)

Para garantizar la compatibilidad de entornos y evitar conflictos de versiones con scikit-learn, el modelo se genera de forma nativa directamente dentro del contenedor. Ejecutar los siguientes comandos en orden:

1. **Construir la imagen:**
   ```bash
   docker build -t kddcup-mlops-api:latest .