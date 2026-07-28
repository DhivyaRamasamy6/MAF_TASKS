from agent_framework import tool
@tool(name="Weather")
async def get_weather(city:str)->str:
    """
    Returns the current weather for a given city.

    Use this tool ONLY when the user asks about:
    - weather
    - temperature
    - forecast
    - rain
    - humidity
    - climate
    """
    
    raise Exception("Weather API is unavailable")