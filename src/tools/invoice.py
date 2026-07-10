from agent_framework import tool
from src.common.logger import get_logger
logger=get_logger(__name__)
@tool(name="Invoice_details",description="Retrieve invoice details using the invoice ID.")
def get_invoice(invoice_id:str)->dict:
    """Retrieve invoice information."""
    logger.info("invoice tool invoked")
    invoices={
        "INV101":{
            "invoice_id":"INV101",
            "amount":"50,000",
            "status":"Paid"
        },
        "INV102":{
            "invoice_id":"INV102",
            "amount":"1,00,000",
            "status":"Pending"
        },
        
    }
    return invoices.get(invoice_id,{"error":"Invoice processing failed"})