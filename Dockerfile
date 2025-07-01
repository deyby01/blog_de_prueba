# Usar una imagen oficial de Python como bas
FROM python:3.11-slim

# 2. Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Copiar el archivo de requerimentos e instalar dependencias 
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar todo el codigo del proyecto al contenedor
COPY . /app/

# 6. Exponer el puerto que usara Django
EXPOSE 8000

# 7. El comando para correr la aplicacion
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]