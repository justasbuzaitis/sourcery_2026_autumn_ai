# Run the model

This task runs [`Qwen/Qwen3-1.7B-GGUF`](https://huggingface.co/Qwen/Qwen3-1.7B-GGUF) locally with Docker Model Runner.

## Task

Start the model:

```sh
docker compose up -d qwen
```

Chat with the model:

```sh
docker model run hf.co/Qwen/Qwen3-1.7B-GGUF:Q8_0
```
