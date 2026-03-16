"""
Weather Tool
=============
Provides weather data for the agent using the free wttr.in API.
No API key required — great for learning!
"""

import requests
from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city.

    Args:
        city: Name of the city (e.g., "London", "Tokyo")

    Returns:
        Current weather conditions as a formatted string
    """
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=j1",
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        current = data["current_condition"][0]
        return (
            f"Weather in {city}: "
            f"{current['temp_C']}°C ({current['temp_F']}°F), "
            f"{current['weatherDesc'][0]['value']}, "
            f"Humidity: {current['humidity']}%, "
            f"Wind: {current['windspeedKmph']} km/h"
        )
    except Exception as e:
        return f"Error fetching weather for {city}: {e}"
