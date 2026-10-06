from pydantic import BaseModel
from typing import Literal
class TicketTask(BaseModel):
 id:str; category:Literal['password_reset','vpn_fault','access_request']; title:str; description:str; required_actions:list[str]; expected_outcome:str; difficulty:str='medium'
class EpisodeResult(BaseModel):
 task_id:str; passed:bool; score:float; actions:list[str]; feedback:list[str]
