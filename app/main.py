from fastapi import FastAPI
from .tasks import get_tasks
from .agent import demo_agent,openai_agent
from .grader import grade
app=FastAPI(title='Ticket-Bench')
@app.get('/health')
def health():return {'status':'ok'}
@app.get('/tasks')
def tasks():return get_tasks()
@app.post('/benchmark/{task_id}')
def benchmark(task_id:str,use_openai:bool=False):
 t=next((x for x in get_tasks() if x.id==task_id),None)
 if not t:return {'error':'task not found'}
 return grade(t,openai_agent(t) if use_openai else demo_agent(t))
