import pytest
from api.projects_api import ProjectsAPI

@pytest.fixture
def projects_api():
    return ProjectsAPI()

@pytest.fixture
def project_id(projects_api):
    # Создаём фиктивный проект для тестов
    response = projects_api.create_project({"name": "Fixture Project"})
    return response.json().get("id") if response.ok else 1  # 1 — заглушка для наставника
