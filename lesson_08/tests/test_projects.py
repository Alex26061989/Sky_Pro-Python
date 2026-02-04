import pytest
from api.projects_api import ProjectsAPI

    # Создаём объект API для работы с проектами
@pytest.fixture
def projects_api():
    return ProjectsAPI()

    # Создаём тестовый проект и возвращаем его ID
@pytest.fixture
def project_id(projects_api):
    response = projects_api.create_project({"title": "Fixture Project"})
    project_id = response.json().get("id")
    yield project_id

def test_create_project_positive(projects_api):
    response = projects_api.create_project({"title": "Positive Project"})  # исправлено на title
    assert response.status_code in (200, 201)

    # пустой словарь, ожидаем ошибку 400
def test_create_project_negative(projects_api):
    response = projects_api.create_project({}) 
    assert response.status_code == 400  

    # Передаём id проекта через фикстуру
def test_get_project_positive(projects_api, project_id):
    response = projects_api.get_project(project_id)
    assert response.status_code == 200

def test_get_project_negative(projects_api):
    response = projects_api.get_project(999999)  # несуществующий проект
    assert response.status_code == 404

def test_update_project_positive(projects_api, project_id):
    response = projects_api.update_project(project_id, {"title": "Updated Project"})  # исправлено на title
    assert response.status_code == 200

def test_update_project_negative(projects_api):
    response = projects_api.update_project(999999, {"title": "Updated Project"})
    assert response.status_code == 400  # исправлено на 400
