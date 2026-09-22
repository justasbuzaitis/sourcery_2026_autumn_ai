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

If you still see that package was not found, it could be `0.109.0` version bug that could be resolved like this:

```sh
ln -sf "$(npm root -g)/@mark3labs/kit/bin/kit-bin" \
  "$(npm config get prefix)/bin/kit"

rehash
kit --help
```

The `.kit.yml` file connects Kit to the local Qwen 1.7B chat model.
