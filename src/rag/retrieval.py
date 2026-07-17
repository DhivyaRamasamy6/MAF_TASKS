from src.rag.ingestion import get_collection
from src.rag.model import HRPolicyChunk

async def retrieve_hr_policy(query:str,backend:str="in_memory",top:int=5,)->list[HRPolicyChunk]:
    """Retrieve the most relevant HR policy chunks."""
    collection=get_collection(backend)
    chunks:list[HRPolicyChunk]=[]
    async with collection:
        results=await collection.search(query,top=top)
        async for result in results.results:
            chunks.append(result.record)
    return chunks
