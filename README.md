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

---

## O. Monitoreo del Sistema, Datos y Modelo (MLOps)

Para garantizar la estabilidad, confiabilidad y el rendimiento óptimo del pipeline de Machine Learning en un entorno de producción, he estructurado el sistema de monitoreo en tres dimensiones clave:

### O1. System Monitoring (Monitoreo de Infraestructura y API)
A nivel de sistema y asegurando la alta disponibilidad del servicio expuesto mediante **FastAPI** y **Docker**, realizo el control de las siguientes métricas operativas:
- **Latencia:** Control del tiempo de respuesta (en milisegundos) que toma el contenedor al procesar el endpoint `POST /predict`.
- **Throughput:** Medición del volumen de peticiones por minuto que la API es capaz de atender concurrentemente.
- **Error Rate:** Monitoreo estricto de las respuestas HTTP, diferenciando peticiones exitosas (código 200) de errores controlados por esquemas de entrada inválidos (código 422) o fallos de ejecución (código 500).
- **Availability:** Verificación continua del estado del contenedor y su tiempo de actividad (*uptime*), asegurando que el servicio responda correctamente en el endpoint raíz `/`.

### O2. Data Monitoring (Monitoreo de Deriva de Datos - Data Drift)
Para asegurar que las características de entrada del tráfico de red en producción ($P_{production}(X)$) no se desvíen significativamente respecto a la distribución de los datos históricos de entrenamiento y validación ($P_{reference}(X)$), establezco el uso conceptual y técnico de las siguientes técnicas de detección:
- **Kolmogorov-Smirnov (KS Test):** Utilizado para comparar las funciones de distribución acumulada de las variables numéricas continuas y detectar cambios estadísticos relevantes.
- **PSI (Population Stability Index):** Empleado para cuantificar el grado de desplazamiento poblacional entre las variables de referencia y las de producción a lo largo del tiempo.
- **Validación Estructural Automática:** Mediante validación de esquemas con Pydantic y un mecanismo defensivo de dimensiones en la API que previene desajustes de tipos o faltas de variables (*missing values*).

### O3. Model Monitoring (Monitoreo de Desempeño del Modelo)
Dado que mi proyecto corresponde a un problema de **Clasificación binaria** (Detección de intrusiones en redes - KDD Cup 1999), el monitoreo continuo de la calidad predictiva se evalúa mediante las siguientes métricas clave obtenidas y validadas en el ciclo de ML:
- **Precision (Precisión):** Para minimizar los falsos positivos y asegurar que las alertas de ataques sean confiables.
- **Recall (Exhaustividad):** Para garantizar que la gran mayoría de las intrusiones reales sean detectadas correctamente y no pasen desapercibidas.
- **F1-Score:** Como métrica armónica de balance entre precisión y recall.
- **AUC (Área Bajo la Curva ROC):** Para medir la capacidad discriminativa global del modelo entre tráfico normal y malicioso.