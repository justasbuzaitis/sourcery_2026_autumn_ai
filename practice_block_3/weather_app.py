from fastmcp import FastMCP

mcp = FastMCP("Weather MCP")

@mcp.tool()
def get_weather(city: str) -> str:
    weather = {
        "Kaunas": "15°C and cloudy",
    }
    return weather.get(city, "Unknown city")


if __name__ == "__main__":
    mcp.run()
