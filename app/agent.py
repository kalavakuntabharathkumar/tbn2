import os
def demo_agent(task): return list(task.required_actions)
def openai_agent(task):
 key=os.getenv('OPENAI_API_KEY')
 if not key:return demo_agent(task)
 from openai import OpenAI
 c=OpenAI(api_key=key); r=c.chat.completions.create(model=os.getenv('OPENAI_MODEL','gpt-4o-mini'),temperature=0,messages=[{'role':'user','content':f'Return only comma-separated actions needed. Allowed: {task.required_actions}. Ticket: {task.title} - {task.description}'}])
 return [x.strip() for x in (r.choices[0].message.content or '').split(',') if x.strip()]
