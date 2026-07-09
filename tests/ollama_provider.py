import asyncio
import os
from dotenv import load_dotenv
from agent_framework.ollama import OllamaChatClient
load_dotenv()
client=OllamaChatClient(model=os.getenv("OLLAMA_MODEL"))
agent=client.as_agent(
    name="Assistant",
    instructions="You are a helpful assistant. keep your answers brief.",
)
async def main():
    result=await agent.run("What is AI?")
    print(result.text)
asyncio.run(main())