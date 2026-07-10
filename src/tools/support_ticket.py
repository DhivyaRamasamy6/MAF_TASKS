from agent_framework import tool
from src.common.logger import get_logger
logger=get_logger(__name__)
@tool(name="support_ticket",description="Create a customer support ticket.")
def create_ticket(issue:str)->str:
    """Creates support ticket."""
    logger.info("support_ticket tool invoked ")
    return{
        "ticket_id":"t1001",
        "status":"created",
        "issue":issue
    }
    