# Preparation

1. Open Docker Desktop.
2. In **Docker Desktop → Settings → AI**, enable **Docker Model Runner** and ensure the TCP port is set to `12434`.
3. Start the Qwen model:

```sh
docker compose up -d qwen
```

4. Install Kit and verify it:

```sh
npm install -g @mark3labs/kit
kit --help
```

If `kit` is not recognized, restart the terminal or use:

```sh
npx @mark3labs/kit --help
```
