import os
from src.config.settings import foundry_client
from agent_framework import Agent
from dotenv import load_dotenv
import asyncio
from src.common.logger import get_logger
logger=get_logger(__name__)
gihub_pat=os.getenv("GITHUB_ACCESS_TOKEN")
auth_header={"Authorization":f"Bearer {gihub_pat}",}

def github_mcp()->None:
    """
    The tool connects to the GitHub MCP server using a GitHub Personal
    Access Token (PAT) for authentication.
    """
    if not gihub_pat:
        raise ValueError ("GITHUB PAT TOKEN must be set")
    logger.info("Github mcp tool is invoked")
    return foundry_client.get_mcp_tool(
        name="GitHub",
        url="https://api.githubcopilot.com/mcp/",
        headers=auth_header,
        approval_mode="never_require",
    )
    
   

