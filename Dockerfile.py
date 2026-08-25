FROM python:3.13-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar paquete Python
COPY transformapi-1.0.0-py3-none-any.whl .

# Instalar nuestra aplicación
RUN pip install --no-cache-dir transformapi-1.0.0-py3-none-any.whl

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
