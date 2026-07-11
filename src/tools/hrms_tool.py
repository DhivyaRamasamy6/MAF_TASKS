from agent_framework import MCPStdioTool
from src.common.logger import get_logger
logger=get_logger(__name__)
def hrms():
    logger.info("hrms tool is invoked")
    return MCPStdioTool(
        name="HRMS tool",
        command="python",
        args=[r"C:\Users\Dhivya\OneDrive - CONVERSE Data Solutions\Microsoft_Agent_Framework\src\hrms_mcp\app.py"],
    )
hrms_tool=hrms()