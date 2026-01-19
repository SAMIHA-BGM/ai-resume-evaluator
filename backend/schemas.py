from pydantic import BaseModel
from typing import List

class EvalRequest(BaseModel):
    job_description: str
    resume: str

class EvalResponse(BaseModel):
    score: int
    strengths: List[str]
    improvements: List[str]
