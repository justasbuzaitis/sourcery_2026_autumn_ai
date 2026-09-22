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

**Security:**  
- Use parameterized queries to prevent SQL injection. Replace `id = ${userId}` with `id = $1` and pass `userId` as a parameter.  
- Example: `db.query('SELECT * FROM users WHERE id = $1', [userId])`.

**Correctness:**  
- Ensure the query fetches the correct user (e.g., use `WHERE id = $1` for unique IDs).  
- Validate that the query returns exactly one row (e.g., use `LIMIT 1` if multiple rows might exist).  
- Handle edge cases like duplicate IDs or non-existent users gracefully.

**Maintainability:**  
- Refactor the query to use a more readable structure (e.g., `SELECT * FROM users WHERE id = $1`).  
- Avoid inline string interpolation and use a library like `pg` for prepared statements.  
- Add comments or documentation for clarity.

**Fixes:**  
1. Replace inline SQL with parameterized query (`id = $1`).  
2. Use `LIMIT 1` to ensure single result (if needed).  
3. Refactor code to use a library like `pg` for prepared statements.
