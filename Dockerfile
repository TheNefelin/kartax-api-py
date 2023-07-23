# Usa una imagen de Windows como base
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Crea el directorio de trabajo dentro del contenedor
WORKDIR C:\app

# Copia los archivos necesarios de tu proyecto al contenedor
COPY requirements.txt .
COPY vercel.json .
COPY . .
COPY sql\sql_server.py .\sql\

# Crea un entorno virtual para el proyecto con virtualenv
RUN pip install virtualenv
RUN virtualenv env

# Activa el entorno virtual
RUN .\env\Scripts\activate

# Instala las dependencias de tu proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Desactiva el entorno virtual
RUN deactivate

# Define el comando para ejecutar tu aplicación
CMD ["python", "src/main.py"]