from agent_framework import tool
from src.common.logger import get_logger
logger = get_logger(__name__)


@tool
def calculator(expression: str) -> str:
    """
    Use this tool for ALL arithmetic calculations.

    Examples:
    - 25*67
    - 100/5
    - (12*17)/0
    - 2**10

    Never calculate manually.
    Always use this tool.
    """

    logger.info(
        f"Calculating expression: {expression}"
    )

    print(
        f"[Calculator Tool] Executing: {expression}"
    )

    return str(eval(expression))