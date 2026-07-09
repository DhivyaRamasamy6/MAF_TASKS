#maf client
import os
from dotenv import load_dotenv
from agent_framework.foundry import FoundryChatClient
from agent_framework.openai import OpenAIChatClient
from agent_framework.ollama import OllamaChatClient
from azure.identity import ClientSecretCredential
load_dotenv()


credential = ClientSecretCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    client_secret=os.environ["AZURE_CLIENT_SECRET"],
)

#Foundry
foundry_client=FoundryChatClient(
    project_endpoint=os.getenv("FOUNDRY_PROJECT_ENDPOINT"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    credential=credential,
)

#openai
openai_client = OpenAIChatClient(
    base_url=os.getenv("AZURE_AI_ENDPOINT"),
    api_key=os.getenv("AZURE_AI_KEY"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
)

#ollama
ollama_client=OllamaChatClient(
    model=os.getenv("OLLAMA_MODEL")
)






