import json
from ollama import AsyncClient
import os
from dotenv import load_dotenv
load_dotenv()
# import asyncio
from src.models.model import RequestClassification
ollama = AsyncClient(host="http://localhost:11434")


async def classify_request(user_query:str):
    prompt = f"""
    You are a request classifier.

    Return ONLY valid JSON in this format:

    {{
    "role": "",
    "category": "",
    }}

    Rules:
    - Extract department, role, and access_level from the user message.
    - Classify the request as exactly one of:
    - Finance
    - HR
    - Sales
    - General
    - Finance includes: salary, payroll, budget, invoice, tax, revenue, profit, expense.
    - Return only JSON. No explanation. No markdown.

    User Message:
    {user_query}
    """

    response = await ollama.chat(
        model=os.getenv("OLLAMA_MODEL"),
        format="json",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )
    content = response["message"]["content"]
    content = content.replace("```json", "").replace("```", "").strip()

    result = RequestClassification.model_validate_json(content)

    return result
