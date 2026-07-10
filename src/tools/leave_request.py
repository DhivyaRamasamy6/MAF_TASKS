from agent_framework import tool
from src.models.model import LeaveRequest

LEAVE_DB={}
next_id=1
@tool(approval_mode="always_require",description="""
    Submit a leave request.
    Arguments:
    - request.employee_name: Full name of the employee.
    - request.leave_type: Must be exactly one of:
    - casual
    - sick
    - vacation
    - request.start_date: ISO date (YYYY-MM-DD)
    - request.end_date: ISO date (YYYY-MM-DD)
    - request.reason: Reason for leave.
    Do not use values like 'Casual Leave'.
    Use only: casual, sick or vacation.
    """)
def submit_leave_request(
    request:dict,request_id:str
    )->dict:
    
    global next_id
    request=LeaveRequest.model_validate(request)
    request_id=f"LR-{next_id:04d}"
    next_id+=1
    LEAVE_DB[request_id] = request.model_dump()

    return {
        "request_id": request_id,
        "employee_name": request.employee_name,
        "status": request.status,
        "message": "Leave request submitted successfully."
    }