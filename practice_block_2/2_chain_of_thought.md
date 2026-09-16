# Chain of thought

Ask the model to solve the question in clear steps and provide a concise final answer.

## Rewritten prompt

```text
Analyze this PostgreSQL Node.js function in three clear steps: security, correctness,
and maintainability. End with a concise list of fixes.

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

## Response

1. **Security:** String interpolation allows SQL injection. Use `$1` and pass `[userId]`.
2. **Correctness:** Multiple rows would be reduced to the first result. Enforce a unique ID or add `LIMIT 1`.
3. **Maintainability:** Move query execution into a small helper.
