from fastmcp import FastMCP

mcp = FastMCP("Weather MCP")

@mcp.tool()
def get_weather(city: str) -> str:
    weather = {
        "Kaunas": "Sunny",
    }
    return weather.get(city, "Unknown city")


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
