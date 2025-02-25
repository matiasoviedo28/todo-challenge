# 📂 Files.md - Estructura del Proyecto

Este documento explica la estructura de archivos y carpetas dentro del proyecto.

---

## 📂 **Raíz del Proyecto (`/`)**

| Archivo / Carpeta        | Descripción |
|--------------------------|-------------|
| `README.md`             | Documentación principal del proyecto. |
| `files.md`              | Este archivo, con la descripción de la estructura del proyecto. |
| `docker-compose.yml`    | Orquestación de los contenedores con Docker Compose. |
| `requirements.txt`      | Lista de dependencias del proyecto. |

---

## 📂 **Backend (`backend/`)**

| Archivo / Carpeta        | Descripción |
|--------------------------|-------------|
| `manage.py`             | Script principal para ejecutar comandos en Django. |
| `Dockerfile`            | Define cómo construir la imagen de Docker para el backend. |
| `pytest.ini`            | Configuración para `pytest`. |

---

## 📂 **Aplicación Principal (`backend/todo/`)**

| Archivo / Carpeta        | Descripción |
|--------------------------|-------------|
| `__init__.py`           | Indica que esta carpeta es un módulo de Python. |
| `settings.py`           | Configuración global de Django. |
| `urls.py`               | Rutas de la API. |
| `wsgi.py`               | Configuración del servidor WSGI para producción. |

---

## 📂 **Módulo de Tareas (`backend/tasks/`)**

| Archivo / Carpeta        | Descripción |
|--------------------------|-------------|
| `models.py`             | Define el modelo de datos de Tareas. |
| `views.py`              | Lógica de los endpoints de la API. |
| `serializers.py`        | Convierte los modelos en JSON. |
| `admin.py`              | Configura la administración de Django. |
| `migrations/`           | Contiene los archivos de migración de la base de datos. |
| `test_tasks.py`         | Pruebas unitarias con `pytest`. |

---

## 📂 **Logs y Configuración**

| Archivo / Carpeta        | Descripción |
|--------------------------|-------------|
| `logs/`                 | Carpeta donde se guardan los logs de ejecución. |
| `.env.example`          | Archivo de ejemplo para definir variables de entorno. |

---

## 📩 **Contacto**
**[Matías Oviedo](https://www.linkedin.com/in/matias-alberto-oviedo-gonzalez/)**
