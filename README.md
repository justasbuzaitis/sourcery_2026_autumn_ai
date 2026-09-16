# Sourcery 2026 Autumn AI

## Setup before the lecture

1. Install [Docker Desktop](https://docs.docker.com/get-started/get-docker/) **4.42 or newer**.
2. Open **Docker Desktop → Settings → AI**, enable **Docker Model Runner**, and ensure the TCP port is set to `12434`.
3. Verify the installation:

   ```sh
   docker model version
   docker compose version
   ```

   Docker Compose must be version **2.36 or newer**.

4. **Choose and download a model.** The exercises use **Qwen 1.7B** by default. These are suggested total laptop RAM amounts:

   | Laptop RAM | Chat model |
   | --- | --- |
   | Less than 8 GB | `hf.co/Qwen/Qwen3-0.6B-GGUF:Q8_0` |
   | 8 GB | `hf.co/Qwen/Qwen3-1.7B-GGUF:Q8_0` (default) |
   | 16 GB | `hf.co/Qwen/Qwen3-4B-GGUF:Q4_K_M` |
   | 32 GB or more | `hf.co/Qwen/Qwen3-8B-GGUF:Q4_K_M` |

   Download the default model:

   ```sh
   docker model pull hf.co/Qwen/Qwen3-1.7B-GGUF:Q8_0
   ```

5. Install the [Node.js LTS version](https://nodejs.org/en/download). npm is included. Verify with:

   ```sh
   node --version
   npm --version
   ```

## Branch commands

Push practice branches one by one:

```sh
git push --set-upstream origin practice-1
git push --set-upstream origin practice-2
git push --set-upstream origin practice-3
git push --set-upstream origin practice-4
```

Update downstream branches after changing an earlier branch:

```sh
git rebase main practice-1
git rebase practice-1 practice-2
git rebase practice-2 practice-3
git rebase practice-3 practice-4
```
