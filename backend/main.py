# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from agent import agent

# app = FastAPI(title="AI Resume Evaluator")

# # Allow frontend origin during dev
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# class EvaluateRequest(BaseModel):
#     job_description: str
#     resume_text: str


# class EvaluateResponse(BaseModel):
#     score: int
#     strengths: list[str]
#     improvements: list[str]


# @app.get("/")
# async def root():
#     return {"message": "AI Resume Evaluator API is running"}


# # @app.post("/evaluate", response_model=EvaluateResponse)
# # async def evaluate(req: EvaluateRequest):
# #     prompt = f"""
# # Job description:
# # {req.job_description}

# # Resume:
# # {req.resume_text}
# # """
    
# #     # Call the PydanticAI agent
# #     result = await agent.run(prompt)
    
# #     # PydanticAI gives validated JSON data
# #     data = result.data
    
# #     return EvaluateResponse(
# #         score=int(data["score"]),
# #         strengths=data["strengths"],
# #         improvements=data["improvements"],
# #     )

# @app.post("/evaluate", response_model=EvaluateResponse)
# async def evaluate(req: EvaluateRequest):
#     prompt = f"""
# Job description:
# {req.job_description}

# Resume:
# {req.resume_text}
#     """

#     result = await agent.run(prompt)
    
#     # Handle agent output safely - extract what matches your prompt
#     data = result.data if result.data else {}
    
#     return EvaluateResponse(
#         score=int(data.get("score", 0)),  # Default 0 if missing
#         strengths=data.get("strengths", []),
#         improvements=data.get("improvements", []) + data.get("skill_gaps", [])  # Merge gaps into improvements
#     )

#2:(crying in pain)


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from agent import agent
# from typing import Any, Dict

# app = FastAPI(title="AI Resume Evaluator")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class EvaluateRequest(BaseModel):
#     job_description: str
#     resume_text: str

# class EvaluateResponse(BaseModel):
#     score: int
#     strengths: list[str]
#     improvements: list[str]

# @app.get("/")
# async def root():
#     return {"message": "AI Resume Evaluator API is running"}

# @app.post("/evaluate")
# async def evaluate(req: EvaluateRequest) -> EvaluateResponse:
#     prompt = f"""
# Job description:
# {req.job_description}

# Resume:
# {req.resume_text}
#     """

#     try:
#         result = await agent.run(prompt)
#         data: Dict[str, Any] = getattr(result, 'data', {})
        
#         # Force-fit to model - safe defaults
#         score = int(data.get('score', 0) or 0)
#         strengths = [str(s) for s in (data.get('strengths', []) or [])]
#         improvements = [str(i) for i in (data.get('improvements', []) + data.get('skill_gaps', []) or [])]
        
#         return EvaluateResponse(score=score, strengths=strengths, improvements=improvements)
#     except Exception as e:
#         # Fallback on error
#         return EvaluateResponse(score=0, strengths=[], improvements=["Agent error - check logs"])

#3

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from agent import agent
# from typing import Any, Dict

# app = FastAPI(title="AI Resume Evaluator")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class EvaluateRequest(BaseModel):
#     job_description: str
#     resume_text: str

# @app.get("/")
# async def root():
#     return {"message": "AI Resume Evaluator API is running"}

# @app.post("/evaluate")
# async def evaluate(req: EvaluateRequest) -> Dict[str, Any]:
#     prompt = f"""
# Job description:
# {req.job_description}

# Resume:
# {req.resume_text}
#     """

#     try:
#         result = await agent.run(prompt)
#         data: Dict[str, Any] = getattr(result, 'data', {})
        
#         score = int(data.get('score', 0) or 0)
#         strengths = [str(s) for s in (data.get('strengths', []) or [])]
#         improvements = [str(i) for i in (data.get('improvements', []) + data.get('skill_gaps', []) or [])]
        
#         return {
#             "score": score,
#             "strengths": strengths,
#             "improvements": improvements
#         }
#     except Exception as e:
#         return {"score": 0, "strengths": [], "improvements": [f"Error: {str(e)}"]}
# app.openapi_schema = None  # Clear cache

# from typing import List, Any, Dict
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from agent import agent

# app = FastAPI(title="AI Resume Evaluator")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class EvaluateRequest(BaseModel):
#     job_description: str
#     resume_text: str

# class EvaluateResponse(BaseModel):
#     score: int
#     strengths: List[str]
#     improvements: List[str]

# @app.get("/")
# async def root():
#     return {"message": "AI Resume Evaluator API is running"}

# @app.post("/evaluate", response_model=EvaluateResponse)
# async def evaluate(req: EvaluateRequest):
#     prompt = f"""
# Job description:
# {req.job_description}

# Resume:
# {req.resume_text}
#     """

#     try:
#         result = await agent.run(prompt)
#         data: Dict[str, Any] = getattr(result, 'data', {})
        
#         score = int(data.get('score', 0) or 0)
#         strengths = [str(s) for s in (data.get('strengths', []) or [])]
#         improvements = [str(i) for i in (data.get('improvements', []) + data.get('skill_gaps', []) or [])]
        
#         return {
#             "score": score,
#             "strengths": strengths,
#             "improvements": improvements
#         }
#     except Exception as e:
#         return {
#             "score": 0,
#             "strengths": [],
#             "improvements": [f"Error: {str(e)}"]
#         }

# 4

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import List
# from agent import agent

# app = FastAPI(title="AI Resume Evaluator")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # For local + deploy
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class EvalRequest(BaseModel):
#     job_description: str
#     resume: str

# class EvalResponse(BaseModel):
#     score: int
#     strengths: List[str]
#     improvements: List[str]

# # @app.post("/evaluate", response_model=EvalResponse)
# # async def evaluate_resume(request: EvalRequest):
# #     try:
# #         prompt = f"""Score this resume 0-100 against the job. Return ONLY valid JSON:
# # {{
# #     "score": 85,
# #     "strengths": ["Matches FastAPI exp", "LLM knowledge"],
# #     "improvements": ["Add 3+ yrs exp"]
# # }}
# # Job: {request.job_description}
# # Resume: {request.resume}"""
# #         result = agent.chat(prompt)
# #         # Simple parse (adjust if agent returns str)
# #         import json
# #         parsed = json.loads(result) if isinstance(result, str) else result
# #         return EvalResponse(**parsed)
# #     except Exception as e:
# #         return EvalResponse(score=0, strengths=[], improvements=[f"Error: {str(e)}"])

# # app.openapi_schema = None  # Clear cache

# @app.post("/evaluate", response_model=EvalResponse)
# async def evaluate_resume(request: EvalRequest):
#     try:
#         prompt = f"""You are resume evaluator. ANALYZE STRICTLY and respond ONLY with this JSON, NO OTHER TEXT:

# {{
#   "score": 92,
#   "strengths": [
#     "Strong FastAPI match",
#     "LLM/ML experience aligns"
#   ],
#   "improvements": [
#     "Quantify years of exp",
#     "Add deployment examples"
#   ]
# }}

# Job Description: {request.job_description}

# Candidate Resume: {request.resume}

# JSON ONLY - no explanations!"""
#         result = agent.run(prompt)
#         import json
#         parsed = json.loads(str(result).strip())  # Force parse
#         return EvalResponse(**parsed)
#     except Exception as e:
#         return EvalResponse(score=0, strengths=[], improvements=[str(e)])

#5

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import List
# from agent import agent
# import json

# app = FastAPI(title="AI Resume Evaluator")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class EvalRequest(BaseModel):
#     job_description: str
#     resume: str

# class EvalResponse(BaseModel):
#     score: int
#     strengths: List[str]
#     improvements: List[str]

# @app.post("/evaluate", response_model=EvalResponse)
# async def evaluate_resume(request: EvalRequest):
#     try:
#         prompt = f"""Resume evaluator: Return ONLY JSON, no text!

# {{
#   "score": 92,
#   "strengths": ["FastAPI match", "LLM exp"],
#   "improvements": ["Add years exp", "Deploy examples"]
# }}

# Job: {request.job_description}
# Resume: {request.resume}

# JSON ONLY!"""
#         result = agent.run(prompt)
#         parsed = json.loads(str(result).strip())
#         return EvalResponse(**parsed)
#     except Exception as e:
#         return EvalResponse(score=0, strengths=[], improvements=[str(e)])

# app.openapi_schema = None

# @app.post("/evaluate", response_model=EvalResponse)
# async def evaluate_resume(request: EvalRequest):
#     prompt = f"""
# You are an expert AI resume evaluator.

# Evaluate the resume strictly against the job description.

# Return a structured result.

# Job Description:
# {request.job_description}

# Resume:
# {request.resume}
# """

#     result = await agent.run(prompt)
#     return result.data

#6
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from agent import agent
import json  # Fallback

app = FastAPI(title="AI Resume Evaluator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EvalRequest(BaseModel):
    job_description: str
    resume: str

class EvalResponse(BaseModel):
    score: int
    strengths: List[str]
    improvements: List[str]

@app.get("/")
async def root():
    return {"status": "Backend running"}

@app.post("/evaluate", response_model=EvalResponse)
async def evaluate_resume(request: EvalRequest):
    prompt = f"""Expert resume evaluator. Output ONLY JSON:

{{"score": 85, "strengths": ["Matches Python skills"], "improvements": ["Add exp years"]}}

Job: {request.job_description}
Resume: {request.resume}

JSON ONLY!"""
    try:
        result = await agent.run(prompt)
        # Safe access - works for pydantic_ai
        if hasattr(result, 'output') and result.output:
            data = result.output.dict()
        else:
            data = json.loads(str(result))
        return EvalResponse(**data)
    except Exception as e:
        return EvalResponse(score=0, strengths=[], improvements=[f"Error: {str(e)}"])
