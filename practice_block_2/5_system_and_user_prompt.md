# System and user prompts

Put behavior and constraints in the system prompt. Put the question in the user prompt.

## Rewritten prompt

```text
System: You are a concise application-security reviewer. Report only concrete issues.
For each issue, give severity, impact, and the smallest fix.

User: Review this Node.js function.

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

Severity: High  
Impact: SQL injection vulnerability allows attackers to execute arbitrary SQL code.  
Fix: Use parameterized queries instead of string interpolation.  
Example: `db.query('SELECT * FROM users WHERE id = $1', [userId]);`
