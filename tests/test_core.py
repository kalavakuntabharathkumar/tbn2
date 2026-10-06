from fastapi.testclient import TestClient
from app.main import app
from app.tasks import get_tasks
from app.grader import grade
c=TestClient(app)
def test_health(): assert c.get('/health').json()['status']=='ok'
def test_tasks(): assert len(c.get('/tasks').json())>=3
def test_grade():
 t=get_tasks()[0]; assert grade(t,t.required_actions).passed; assert not grade(t,t.required_actions[:-1]).passed
def test_api(): assert c.post('/benchmark/PWD-001').json()['passed'] is True
