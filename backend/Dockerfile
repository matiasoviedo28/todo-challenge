# Imagen base
FROM python:3.11

# Definir directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el codigo fuente
COPY . .

# Comando de inicio
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "todo.wsgi:application"]
