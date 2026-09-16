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

## Practice blocks

Each practice block is available on its own branch:

1. [Run an LLM locally](https://github.com/justasbuzaitis/sourcery_2026_autumn_ai/tree/practice-1/practice_block_1)
2. [Prompting techniques](https://github.com/justasbuzaitis/sourcery_2026_autumn_ai/tree/practice-2/practice_block_2)
3. [Test MCP](https://github.com/justasbuzaitis/sourcery_2026_autumn_ai/tree/practice-3/practice_block_3)
4. [Experiment with skills](https://github.com/justasbuzaitis/sourcery_2026_autumn_ai/tree/practice-4/practice_block_4)

To open a practice block, replace `1` with its number:

```sh
git fetch origin
git switch --track origin/practice-1
```
