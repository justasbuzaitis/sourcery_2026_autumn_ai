# Preparation

1. Open Docker Desktop.
2. In **Docker Desktop → Settings → AI**, enable **Docker Model Runner**.
3. Start Qwen from this directory:

```sh
docker compose up -d qwen
```

4. Start a chat:

```sh
docker model run hf.co/Qwen/Qwen3-1.7B-GGUF:Q8_0
```

Use this original question for every task:

```text
Review the following Node.js function. Identify potential bugs, security issues, and maintainability problems, and suggest improvements.

async function getUser(userId) {
    const query = `SELECT * FROM users WHERE id = ${userId}`;
    const result = await db.query(query);
    if (result.rows.length == 0) {
        return null;
    }
    console.log("User loaded:", result.rows[0]);
    return result.rows[0];
}
```

Rewrite the question using each prompting technique, test it, and record the response.
