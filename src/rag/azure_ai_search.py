import os
from agent_framework import Agent
from src.config.settings import foundry_client
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from dotenv import load_dotenv
load_dotenv()

search_endpoint = os.getenv('SEARCH_SERVICE_ENDPOINT')
search_key = os.getenv('SEARCH_SERVICE_QUERY_KEY')
search_index = os.getenv('SEARCH_INDEX_NAME')

#requesting search index
def search_query(query):
    crdential=AzureKeyCredential(search_key)
    search_client=SearchIndexClient(search_endpoint,search_index,crdential)
    results=search_client.search(
        query,
        top=5,
        query_type="",
        select=[]
    )
    return list(results)

# then configure the search result with maf agent
def generate_answer(query,search_result):
    context=""
    for r in search_result:
        context+=r["chunk"]+"\n"
        
    prompt =  f"""...Context: {context}...Question: {query}..."""
   
    
    agent=foundry_client.as_agent(
        name="HRpolicy Agent",
        instructions="""You are a helpful assistant.

        Answer the question ONLY using the context below.
        If the answer is not present, say "I don't know based on the provided data.""",
    )
    result=agent.run(prompt)
    print(result.text)
    
    
    
#in agent_framework
from agent_framework import Agent
from agent_framework.azure import AzureAISearchContextProvider
from src.config.settings import foundry_client

search_provider=AzureAISearchContextProvider(
    endpoint=search_endpoint,
    index_name=search_index,
    api_key=search_key,
    mode="semantic",
    top_k=3,
    semantic_configuration_name="",
)
agent=Agent(
        client=foundry_client,
        context_providers=[search_provider],
        instructions="""
        You are an HR policy assistant. Answer ONLY using retrieved context.
        If the answer isn't found, say I don't know based on the provided data. """,
)
