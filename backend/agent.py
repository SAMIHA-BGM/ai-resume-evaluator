# import os
# from dotenv import load_dotenv
# from pydantic_ai import Agent

# load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# MODEL_NAME = os.getenv("MODEL_NAME", "llama3-70b-8192")

# if not GROQ_API_KEY:
#     raise RuntimeError("GROQ_API_KEY not found. Check your .env file.")

# system_prompt = """
# You are a professional placement resume evaluator.

# Given a job description and a candidate resume, you must:
# 1. Give a match score from 0 to 100.
# 2. List strengths.
# 3. List skill gaps.
# 4. Give improvement suggestions.
# 5. Give a final hiring recommendation.
# """

# agent = Agent(
#     model=f"groq:{MODEL_NAME}",
#     system_prompt=system_prompt,
# )

#2

# import os
# from dotenv import load_dotenv
# from pydantic_ai import Agent

# load_dotenv()
# agent = Agent('groq:llama3-70b-8192')

#3

# from dotenv import load_dotenv
# from pydantic_ai import Agent
# from main import EvalResponse   # import schema

# load_dotenv()

# agent = Agent(
#     'groq:llama3-70b-8192',
#     result_type=EvalResponse
# )

#4

# from dotenv import load_dotenv
# from pydantic_ai import Agent
# from schemas import EvalResponse

# load_dotenv()

# agent = Agent(
#     'groq:llama3-70b-8192',
#     output_type=EvalResponse   
# )

#5

# from dotenv import load_dotenv
# import os
# from pydantic_ai import Agent
# from schemas import EvalResponse

# load_dotenv()
# print("GROQ_API_KEY loaded:", bool(os.getenv('GROQ_API_KEY')))  # Debug

# agent = Agent(
#     'groq:llama3-70b-8192',
#     output_type=EvalResponse
# )

from dotenv import load_dotenv
import os
from pydantic_ai import Agent
from schemas import EvalResponse

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
print(f"DEBUG: API Key exists: {bool(api_key)}")
print(f"DEBUG: Key preview: {api_key[:10] if api_key else 'NONE'}...")  # First 10 chars
if not api_key:
    raise ValueError("GROQ_API_KEY missing from .env!")

agent = Agent(
    'groq:llama-3.1-8b-instant',  # Fast 8B, recommended for testing
    # OR 'groq:llama3-70b-8192'  # Original Llama3 70B (if supported)
    # OR 'groq:llama-3.3-70b-versatile'  # Newer 70B
    output_type=EvalResponse
)



