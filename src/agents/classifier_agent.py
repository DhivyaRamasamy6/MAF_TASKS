from agent_framework import Agent
from src.config.settings import foundry_client
import asyncio
classifier=Agent(
    name="Classifier Agent",
    client=foundry_client,
    instructions="""
    You are a routing agent.

    Your job is ONLY to classify the user's request.

    Choose exactly ONE category.

    Possible categories:
    - HR
    - Finance
    - Data

    Rules:
    - Return only the category name.
    - Do not explain.
    - Do not answer the user's question.
    - Never return anything except:
    
    HR
    Finance
    Data
    output:hr,finance,data
    """   
)

# async def main():
#     response=await classifier.run(
#         "what is leave policy?"
#     )
#     print(response.text)
# asyncio.run(main())