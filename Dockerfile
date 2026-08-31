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

# Copiamos el resto del código del proyecto al contenedor
COPY . .

# Exponemos el puerto 8000 que utiliza FastAPI por defecto
EXPOSE 8000

# Comando para ejecutar la API con Uvicorn de forma accesible desde cualquier IP externa del contenedor
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]