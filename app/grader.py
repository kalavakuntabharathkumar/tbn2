from .models import TicketTask,EpisodeResult
def grade(task:TicketTask,actions:list[str]):
 req=set(task.required_actions); got=set(actions); score=len(req&got)/len(req)
 missing=req-got; feedback=[]
 if missing: feedback.append('Missing: '+', '.join(sorted(missing)))
 if score==1: feedback.append('All required actions completed.')
 return EpisodeResult(task_id=task.id,passed=score==1,score=round(score,3),actions=actions,feedback=feedback)
