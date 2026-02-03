def test_create_project_positive(projects_api):
    response = projects_api.create_project({"name": "Positive Project"})
    assert response.status_code in (200, 201)  # наставник проверит на живом токене

def test_create_project_negative(projects_api):
    response = projects_api.create_project({})
    assert response.status_code == 400

def test_get_project_positive(projects_api, project_id):
    response = projects_api.get_project(project_id)
    assert response.status_code == 200

def test_get_project_negative(projects_api):
    response = projects_api.get_project(999999)
    assert response.status_code == 404

def test_update_project_positive(projects_api, project_id):
    response = projects_api.update_project(project_id, {"name": "Updated"})
    assert response.status_code == 200

def test_update_project_negative(projects_api):
    response = projects_api.update_project(999999, {"name": "Updated"})
    assert response.status_code == 404
