# 📝 Todo List API

Esta es una API REST para la gestión de tareas, construida con **Django Rest Framework (DRF)** y **PostgreSQL**, completamente dockerizada para facilitar su despliegue.  

🚀 Puedes probar la API de dos maneras:
1. **Clonando el repositorio y ejecutándola en local con Docker** 🐳  
2. **Consumiéndola directamente desde nuestro servidor en línea** (recomendado) 🌍  

---

## 🛠 **Tecnologías Utilizadas**
- **Python 3.12** 🐍
- **Django 5.6.1 + Django Rest Framework (DRF)** 🛠
- **PostgreSQL 15.12** como base de datos 🗄
- **Docker + Docker Compose** para despliegue 🚢
- **pytest** para pruebas automatizadas ✅
- **logging** para registro de eventos 📜
- **django-filter** para filtrado de tareas 🔍
- **Token Authentication** para seguridad 🔑

---

## 📌 **1. Probar la API en Nuestro Servidor**
Puedes realizar consultas a la API en nuestro servidor en línea:  
🌍 **Base URL:** `http://201.251.222.200:25080/`

🔐 **Token de acceso:** `90200710a15526cf84d00dd42247b464deba4eb5`

### 🔹 **📌 Probar desde CMD en Windows** (recomendado)
Puedes usar `curl` en **CMD o PowerShell** para interactuar con la API.  

#### **1️⃣ Listar todas las tareas**
Desde **CMD** en Windows:
```cmd
curl -X GET "http://201.251.222.200:25080/api/tareas/" -H "Authorization: Token 90200710a15526cf84d00dd42247b464deba4eb5"
```

Desde **PowerShell**, usa comillas simples en la cabecera:
```powershell
curl -X GET "http://201.251.222.200:25080/api/tareas/" -H 'Authorization: Token 90200710a15526cf84d00dd42247b464deba4eb5'
```

#### **2️⃣ Crear una nueva tarea**
```cmd
curl -X POST "http://201.251.222.200:25080/api/tareas/" -H "Authorization: Token 90200710a15526cf84d00dd42247b464deba4eb5" -H "Content-Type: application/json" -d "{"titulo": "Nueva tarea", "descripcion": "Descripción de prueba", "completada": false}"
```

#### **3️⃣ Actualizar una tarea (marcar como completada)**
```cmd
curl -X PATCH "http://201.251.222.200:25080/api/tareas/1/" -H "Authorization: Token 90200710a15526cf84d00dd42247b464deba4eb5" -H "Content-Type: application/json" -d "{"completada": true}"
```

#### **4️⃣ Eliminar una tarea**
```cmd
curl -X DELETE "http://201.251.222.200:25080/api/tareas/1/" -H "Authorization: Token 90200710a15526cf84d00dd42247b464deba4eb5"
```

---

## 📌 **2. Clonar y Ejecutar en Local con Docker**
### 🔹 **Requisitos**
- Tener **Docker y Docker Compose** instalados en tu máquina.

### 🔹 **Pasos de instalación**
1️⃣ **Clonar el repositorio**  
```sh
git clone https://github.com/matiasoviedo28/todo-challenge.git
cd todo-challenge
```

2️⃣ **Levantar los contenedores con Docker**  
```sh
docker compose up -d
```

3️⃣ **Crear las migraciones y superusuario**  
```sh
docker compose run --rm web python manage.py migrate
docker compose run --rm web python manage.py createsuperuser
```

4️⃣ **Probar la API en local**  
Si ejecutaste todo correctamente, la API estará disponible en:  
🌍 `http://localhost:25080/api/tareas/`

Puedes probar los mismos comandos `curl`, pero apuntando a `localhost` en lugar de `201.251.222.200`.

---

## 🛠 **3. Pruebas Automáticas**
Hemos implementado **tests automatizados con `pytest`** para verificar el correcto funcionamiento de la API.  
Para ejecutar las pruebas:
```sh
docker compose run --rm web pytest
```

---

## ✅ **4. Validaciones Implementadas**
- **Para garantizar que la API sea segura y a prueba de errores, se han implementado las siguientes validaciones:**  

### 1️⃣ Evitar Tareas Duplicadas
- No se permite crear dos tareas con **el mismo título, descripción y estado (`completada`)**.
- Si se intenta crear una tarea idéntica, la API devuelve:
  ```json
  { "detail": "Ya existe una tarea con estos mismos datos." }
  ```

### 2️⃣ Campos Obligatorios
- El titulo y descripcion son obligatorios y no pueden estar vacíos.
- Si un campo está vacío, la API devuelve:
  ```json
  { "titulo": ["El título no puede estar vacío."] }
  ```

### 3️⃣ Validación del Campo completada
- Solo acepta true o false
- Si se envía otro valor (ej. "si", 1, "false"), la API devuelve:
  ```json
  { "completada": ["El campo 'completada' debe ser True o False."] }
  ```
### 4️⃣ Errores Claros y Personalizados
- Todos los errores devuelven mensajes explicativos para que el usuario entienda qué está mal en la petición.


---

## 🔐 **5. Seguridad y Consideraciones**
- **El token de autenticación proporcionado es solo para pruebas.**  
  Si deseas regenerar un token para otro usuario, ejecuta:  
  ```sh
  docker compose run --rm web python manage.py drf_create_token <nombre_de_usuario>
  ```

---

---
## 📂 **Documentación de Archivos**
📄 **[Files.md](./files.md)** → Explicación detallada de cada archivo en el proyecto.

---

## 📩 **Contacto**
Si tienes dudas o quieres colaborar, no dudes en contactarme. 🚀  

**[Matías Oviedo](https://www.linkedin.com/in/matias-alberto-oviedo-gonzalez/)**
