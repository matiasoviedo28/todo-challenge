import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from tasks.models import Tarea

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="testpass")

@pytest.fixture
def auth_client(api_client, user):
    response = api_client.post("/api/token/", {"username": "testuser", "password": "testpass"})
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {response.data['token']}")
    return api_client

@pytest.fixture
def tarea(db):
    return Tarea.objects.create(titulo="Tarea de prueba", descripcion="Esto es un test", completada=False)

def test_crear_tarea(auth_client):
    response = auth_client.post("/api/tareas/", {"titulo": "Nueva tarea", "descripcion": "Descripción", "completada": False})
    assert response.status_code == 201
    assert response.data["titulo"] == "Nueva tarea"

def test_listar_tareas(auth_client, tarea):
    response = auth_client.get("/api/tareas/")
    assert response.status_code == 200
    assert len(response.data) > 0

def test_crear_tarea_sin_titulo(auth_client):
    response = auth_client.post("/api/tareas/", {"titulo": "", "descripcion": "Descripción válida", "completada": False})
    assert response.status_code == 400
    assert "titulo" in response.data

def test_crear_tarea_sin_descripcion(auth_client):
    response = auth_client.post("/api/tareas/", {"titulo": "Tarea válida", "descripcion": "", "completada": False})
    assert response.status_code == 400
    assert "descripcion" in response.data
