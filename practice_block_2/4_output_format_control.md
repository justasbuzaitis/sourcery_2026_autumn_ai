# Output format control

Specify the required response structure, such as JSON, a table, bullets, or a word limit.

## Rewritten prompt

```text
Review this PostgreSQL Node.js function. Return only a Markdown table with columns
Severity, Issue, and Fix. Use at most three rows.

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

| Severity | Issue | Fix |
| --- | --- | --- |
| High | SQL injection | Use `db.query("SELECT * FROM users WHERE id = $1", [userId])`. |
| Medium | Input is not validated | Validate the type and range of `userId`. |
| Low | Log message is vague | Use a more descriptive log message. |
