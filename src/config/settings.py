#maf client
import os
from dotenv import load_dotenv
from agent_framework.foundry import FoundryChatClient
from agent_framework.openai import OpenAIChatClient
from azure.identity import DefaultAzureCredential

load_dotenv()

# credential=DefaultAzureCredential()

# client=FoundryChatClient(
#     project_endpoint=os.getenv("FOUNDRY_PROJECT_ENDPOINT"),
#     model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
#     credential=DefaultAzureCredential(),
    
# )


client = OpenAIChatClient(
    base_url=os.getenv("AZURE_AI_ENDPOINT"),
    api_key=os.getenv("AZURE_AI_KEY"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
)






