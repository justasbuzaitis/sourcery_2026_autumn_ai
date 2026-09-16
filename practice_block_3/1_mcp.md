# Test a weather MCP server

## 1. Start Kit

From this directory, run:

```sh
kit --model custom/qwen-local
```

If the `kit` command is unavailable, run:

```sh
npx @mark3labs/kit --model custom/qwen-local
```

## 2. Ask about the weather

Ask Kit:

```text
What is the current weather in Kaunas? Use an available tool and do not guess.
```

Kit cannot answer because it does not have a weather tool.

Result:

```text
I don't have access to real-time weather data or external APIs.
```

## 3. Add weather data

In `weather_app.py`, add Kaunas to the `weather` dictionary:

```python
weather = {
    "Kaunas": "Sunny",
}
```

## 4. Add the weather MCP server

Add the server to `.kit.yml`:

```yaml
mcpServers:
  weather:
    type: remote
    url: http://localhost:8000/mcp
    noOAuth: true
    allowedTools: ["get_weather"]
```

Build and start the server:

```sh
docker compose up --build -d weather
```

Exit and restart Kit:

```sh
kit --model custom/qwen-local
```

## 5. Ask again

Ask the same question:

```text
What is the current weather in Kaunas? Use an available tool and do not guess.
```

Result:

```text
The current weather in Kaunas is Sunny.
```
