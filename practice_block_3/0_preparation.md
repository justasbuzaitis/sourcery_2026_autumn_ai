# Preparation

1. Open Docker Desktop.
2. In **Docker Desktop → Settings → AI**, enable **Docker Model Runner** and ensure the TCP port is set to `12434`.
3. Start the Qwen model from this directory:

```sh
docker compose up -d qwen
```

4. Install Kit:

```sh
npm install -g @mark3labs/kit
kit --help
```

If `kit` is not recognized, restart the terminal. You can also run it with:

```sh
npx @mark3labs/kit --help
```

The `.kit.yml` file connects Kit to the local Qwen 1.7B chat model.
