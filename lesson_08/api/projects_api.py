import os
import requests

BASE_URL = "https://yougile.com/api-v2" 
TOKEN = os.environ.get("YOUGILE_TOKEN", "ВАШ_ТОКЕН")
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

class ProjectsAPI:
    def create_project(self, data):
        return requests.post(f"{BASE_URL}/projects", json=data, headers=HEADERS)

    def update_project(self, project_id, data):
        return requests.put(f"{BASE_URL}/projects/{project_id}", json=data, headers=HEADERS)

    def get_project(self, project_id):
        return requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
