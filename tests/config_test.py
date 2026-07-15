from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("AZURE_AI_KEY"),
    base_url=os.getenv("AZURE_AI_ENDPOINT"),   )
response = client.embeddings.create(
    model=os.getenv("EMBEDDING_MODEL"),    
    input="Hello World"
)

embedding = response.data[0].embedding
print(len(embedding))