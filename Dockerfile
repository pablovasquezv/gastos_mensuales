FROM python:3.11-slim

# Evita que Python genere archivos .pyc y permite ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalamos dependencias del sistema para que psycopg2 (el driver de Postgres) funcione
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instalamos librerías de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Puerto por defecto de Django
EXPOSE 8000

# Comando para arrancar (ajusta 'tu_proyecto' al nombre de tu carpeta principal)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
