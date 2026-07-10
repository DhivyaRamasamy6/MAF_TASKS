from agent_framework import tool
from src.common.logger import get_logger
logger=get_logger(__name__)
@tool(name="Customer_details",description="Retrieve customer information using the customer ID.")
def get_customer(customer_id:str) ->dict:
    """ Returns the customer information."""
    logger.info("Tool:get_customer invoked")
    customers={
        "c101":{
            "customer_id":"101",
            "name":"kirthika",
            "email":"Kirthika@gmail.com",
            "membership":"Gold"
        },
        "c102":{
            "customer_id":"102",
            "name":"Pragadheeswaran",
            "email":"Pragadheeswaran@gmail.com",
            "membership":"Gold"
        },
        "c103":{
            "customer_id":"103",
            "name":"Gokul",
            "email":"Gokul@gmail.com",
            "membership":"Silver"
        },
        "c104":{
            "customer_id":"104",
            "name":"Dhivya",
            "email":"Dhivya@gmail.com",
            "membership":"Silver"
        }
        }
    return customers.get(customer_id,{"error":"customer not found"})
