from agent_framework import tool
from src.rag.retrieval import retrieve_hr_policy
from src.common.logger import get_logger
logger=get_logger(__name__)
@tool(name="HRpolicy_tool",description='Retrieve HR policy documents.')
async def search_hr_policy(query:str)->str:
    """Retrieve HR Policy documents."""
    logger.info("HRpolicy tool invoked")
    chunks=await retrieve_hr_policy(query,backend="chroma",top=5,)
    if not chunks:
        return "No relevant chunks found."
    response=[]
    
    for chunk in chunks:
        response.append(
            f"""
            Section:{chunk.section_title}
            Page:{chunk.source_page}
            Document:{chunk.document_name}
            
            {chunk.content}
            """
        )
    return "\n".join(response)