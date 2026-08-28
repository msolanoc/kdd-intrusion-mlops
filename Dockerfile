# Usamos una imagen oficial de Python ligera como base
FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalamos dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiamos primero el archivo de requerimientos para aprovechar la caché
COPY requirements.txt .

# Instalamos las librerías de Python necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código y archivos del proyecto al contenedor
COPY . .

# Exponemos el puerto por defecto
EXPOSE 8501

# Comando por defecto para ejecutar el proyecto
CMD ["python", "kddcup1999.py"]