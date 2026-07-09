from agent_framework import tool
@tool(name="order_status",description="Returns the status of an order.")
def get_order_status(order_id:str)->str:
    
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