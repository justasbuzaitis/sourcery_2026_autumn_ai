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

## 3. Add the weather MCP server

Add the server to `.kit.yml`:

```yaml
mcpServers:
  weather:
    type: local
    command: ["docker", "compose", "run", "--build", "--rm", "-T", "weather"]
    allowedTools: ["get_weather"]
```

- `--build` rebuilds the image before starting the server.
- `--rm` removes the stopped server container.
- `-T` disables the terminal interface because MCP communicates through standard input and output.

Exit and restart Kit:

```sh
kit --model custom/qwen-local
```

## 4. Ask again

Ask the same question:

```text
What is the current weather in Kaunas? Use an available tool and do not guess.
```
