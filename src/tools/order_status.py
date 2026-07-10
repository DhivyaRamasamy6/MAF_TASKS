from agent_framework import tool
from src.common.logger import get_logger
logger=get_logger(__name__)
#poor tool schema 
# @tool(name="status_tool",description="Returns something")
@tool(name="get_order_status",description="Retrieves the current status of a customer's order using the provided order ID. Use this tool whenever a user asks about tracking an order, delivery status, shipment progress, or order state.")
def get_order_status(order_id:str)->str:
    """
    Retrieves the status of an order based on the order ID.
    """
    logger.info("Order_status tool invoked")
    orders ={
        "101":{
            "order_id":"101",
            "status":"Delivered",
            "expected_delivery":"08/07/2026"
            },
        "102":{
            "order_id":"102",
            "status":"Processing",
            "expected_delivery":"11/07/2026"
            },
        "103":{
            "order_id":"103",
            "status":"Shipped",
            "expected_delivery":"09/07/2026"
            },
        "104":{
            "order_id":"104",
            "status":"Cancelled",
            "expected_delivery":None
            },
    }
    return orders.get(order_id,{
            "order_id":order_id,
            "status":"not found",
            "expected_delivery":None
            })
