# Role and persona

Give the model a relevant role, audience, and level of expertise.

## Rewritten prompt

```text
You are a senior Node.js security reviewer. Review this function for a junior developer.
Identify concrete bugs, security issues, and maintainability problems. Give at most four
bullets, ordered by severity, and include a fix for each.

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

- **High:** SQL injection is possible. Use `db.query("SELECT * FROM users WHERE id = $1", [userId])`.
- **Medium:** Database errors are not handled. Catch them at the service boundary.
- **Medium:** Logging the complete user row may expose sensitive data. Remove it or log only a safe identifier.
