from agent_framework import workflow,step
from src.agents.HR_assistant import HR_Assistant
from src.agents.finance_assistant import finance_agent
from src.agents.data_engineering import data_engineering_assistant
from src.agents.classifier_agent import classifier

import asyncio


@step
async def hr_step(query:str):
    return await HR_Assistant.run(query)

@step
async def finance_step(query:str):
    return await finance_agent.run(query)

@step
async def data_step(query:str):
    return await data_engineering_assistant.run(query)





@workflow
async def route_request(query: str):
    
    classification = await classifier.run(query)
    department = classification.text.strip().lower()
    print(department)
    if department == "hr":
        return await hr_step(query)

    elif department == "finance":
        return await finance_step(query)

    elif department == "data":
        return await data_step(query)

    else:
        return "Unknown Department"
    
async def main():
     
    result = await route_request.run(
        "what is pf"
    )

    outputs = result.get_outputs()[0]

    print(outputs.text)

    

asyncio.run(main())