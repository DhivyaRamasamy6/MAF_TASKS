from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from src.models.model import ChatRequest,ChatResponse
from src.agents.simple_agent import agent
from src.agents.order_status import assistant
from src.agents.customer_support_agent import customer_support_agent
from src.agents.hrms_agent import hrms_agent
router=APIRouter(tags=["Maf"])

#Agent non-stream
@router.post("/chat/Agent-Response",response_model=ChatResponse)
async def non_stream(request:ChatRequest):
    result=await agent.run(
        request.message
    )
    return ChatResponse(
        message=str(result)
    )
    
#Agent with streaming 
@router.post("/chat/Agent-Streaming")
async def streaming(request:ChatRequest):
    async def agent_stream():
        async for chunk in agent.run(request.message,stream=True):
            yield chunk.text
    return StreamingResponse(
        agent_stream(),
        media_type="text/plain"
    )
#agent -> order_agent
@router.post("/chat/Order_status",response_model=ChatResponse)
async def order(request:ChatRequest):
    result=await assistant.run(
        request.message
    )
    return ChatResponse(
        message=str(result)
    )
     
#agent-customer_support_agent
@router.post("/chat/Customer-Suport-Agent",response_model=ChatResponse)
async def customer_support(request:ChatRequest):
    result=await customer_support_agent.run(
        request.message
    )
    return ChatResponse(
        message=str(result)
    )
    
@router.post("/chat/HRMS-employee lookup",response_model=ChatResponse)
async def hrms(request:ChatRequest):
    result=await hrms_agent.run(
        request.message
    )
    return ChatResponse(
        message=str(result) 
    )