from pydantic import BaseModel
from enum import Enum
from datetime import date
class ChatRequest(BaseModel):
    message:str

class ChatResponse(BaseModel):
    message:str
    


class LeaveType(str,Enum):
    CASUAL="casual"
    SICK="sick"
    VACATION="vacation"
class LeaveStatus(str,Enum):
    SUBMITTED="submitted"
    APPROVED="approved"
    REJECTED="rejected"
    
class LeaveRequest(BaseModel):
    employee_name:str
    leave_type:LeaveType
    start_date:date
    end_date:date
    reason:str
    status:LeaveStatus=LeaveStatus.SUBMITTED