# Imagen base ligera
FROM python:3.11-slim

# Variables útiles
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Crear carpeta de trabajo
WORKDIR /app

# Instalar dependencias del sistema (si hiciera falta, descomenta)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     curl && rm -rf /var/lib/apt/lists/*

# Primero requirements (mejor cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer puerto de Flask
EXPOSE 5000

# Arranque (gunicorn, 2 workers, 1 hilo c/u)
CMD ["gunicorn", "-w", "2", "-k", "gthread", "--threads", "1", "-b", "0.0.0.0:5000", "wsgi:app"]
