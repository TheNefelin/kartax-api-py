# Usa una imagen de Python como base
FROM python:3.11

# Crea el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copia los archivos necesarios de tu proyecto al contenedor
COPY requirements.txt .
COPY . .

# Configura las variables de entorno para Python (Opcional)
#ENV PYTHONUNBUFFERED=1
#ENV PYTHONDONTWRITEBYTECODE=1

# Crea un entorno virtual para el proyecto
RUN python -m venv env

# Activa el entorno virtual (para Windows)
RUN . env/Scripts/activate

# Instala las dependencias de tu proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Define el comando para ejecutar tu aplicación
CMD ["python", "src/main.py"]