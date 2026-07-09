from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from src.models.model import ChatRequest,ChatResponse
from src.agents.simple_agent import agent
from src.agents.assistant import assistant
router=APIRouter(tags=["Maf"])

#Agent non-stream
@router.post("/chat/Agent-Response",response_model=ChatResponse)
async def chat(request:ChatRequest):
    result=await agent.run(
        request.message
    )
    return ChatResponse(
        message=str(result)
    )
    
#Agent with streaming 
@router.post("/chat/Agent-Streaming")
async def agent_stream(request:ChatRequest):
    async def agent_stream():
        async for chunk in agent.run(request.message,stream=True):
            yield chunk.text
    return StreamingResponse(
        agent_stream(),
        media_type="text/plain"
    )
#agent -order_agent
@router.post("/chat/Assistant",response_model=ChatResponse)
async def chat(request:ChatRequest):
    result=await assistant.run(
        request.message
    )
    return ChatResponse(
        message=str(result)
    )
     