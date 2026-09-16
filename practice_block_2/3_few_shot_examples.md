# Few-shot examples

Add two or three example questions and desired answers before the original question.

## Rewritten prompt

```text
Use these examples to review the final PostgreSQL code.

Example 1
Code: const query = `SELECT * FROM users WHERE id = ${id}`;
Answer: High: SQL injection. Use db.query("SELECT * FROM users WHERE id = $1", [id]).

Example 2
Code: console.log("User loaded:", user);
Answer: Medium: user data may be sensitive. Remove the log or log only a safe identifier.

Review in the same concise style:

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

High: SQL injection. Use `db.query("SELECT * FROM users WHERE id = $1", [userId])`.

Medium: sensitive data may be exposed. Remove the log or log only a safe identifier.
