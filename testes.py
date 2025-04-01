import pytest
import requests

#CRUD
BASE_URL = "http://127.0.0.1:5000"
tasks = []
#@pytest.skip("CREATE OK")
def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da Nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

def test_get_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    response_json = response.json()
    
    assert response.status_code == 200
    assert 'tasks' in response_json
    assert 'total_tasks' in response_json

def test_get_task_by_id():
    if tasks:
        tasks_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{tasks_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert tasks_id == response_json['id'] 

def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            'completed': False,
            'description': 'Nova Descrição',
            'title': 'Titulo atualizado'
        }
    response = requests.put(f'{BASE_URL}/tasks/{task_id}', json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert 'message' in response_json
    #assert task_id == response_json['id']

    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['title'] == payload['title']
    assert response_json['completed'] == payload['completed']
    assert response_json['completed'] == payload['completed']

def teste_delete_task():
    if tasks:
        tasks_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{tasks_id}")
        assert response.status_code == 200

        response = requests.get(f"{BASE_URL}/tasks/{tasks_id}")
        assert response.status_code == 404
