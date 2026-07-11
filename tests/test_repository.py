from src.hrms_mcp.database import *
from src.hrms_mcp.repository import EmployeeRepository

db=SessionLocal()

try:
    employee=EmployeeRepository.get_employee_by_id(
        db,"EMP104"
    )
    
    if employee:
        print("Employee Found")
        print(employee.employee_name)
        print(employee.department)
        print(employee.email)
    else:
        print("Employee not found")

finally:
    db.close()