# settings.py

# 1. Seguridad
import os
from pathlib import Path

# **¡IMPORTANTE!** No subir la clave secreta a GitHub.
# Usa variables de entorno (Render te permite definirlas).
SECRET_KEY = os.environ.get('SECRET_KEY', 'una-clave-super-secreta-de-desarrollo')

# 2. Host Permitidos
# Necesario para que Render pueda servir la aplicación.
ALLOWED_HOSTS = ['*'] # Se recomienda poner el nombre de dominio de Render.

# 3. Base de Datos (Usando Variables de Entorno)
# Esto te permite cambiar la DB sin tocar el código.
import dj_database_url
# Si usas Supabase o Render, tendrás una URL de conexión única.
DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600)
}

# 4. CORS
CORS_ALLOW_ALL_ORIGINS = True # Para pruebas rápidas con Postman/Swagger
# O si quieres mayor seguridad:
# CORS_ALLOWED_ORIGINS = [
#     "https://tu-frontend-url.com",
# ]

# 5. Static Files (Necesario para el Admin de Django)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'