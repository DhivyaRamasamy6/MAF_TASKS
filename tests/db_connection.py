from src.tools.hrms_mcp.database import engine

try:
    with engine.connect() as connection:
        print("Database Connected")
    
except Exception as e:
    print("error:",e)
    