FROM python:3.12-slim
WORKDIR /app

COPY requeriments.txt .
RUN pip install --no-cache-dir -r requeriments.txt
COPY . .
CMD ["uvicorn",
     "app.src.controller.ActividadController:app", 
     "--host", "0.0.0.0", 
     "--port","8000"]