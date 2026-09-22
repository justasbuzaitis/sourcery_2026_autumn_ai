# Few-shot examples

Add two or three example questions and desired answers before the original question.

## Rewritten prompt

```text
The examples only demonstrate the answer style and severity levels. Identify the final code's issues independently.

Example 1
Code: const apiKey = "production-secret";
Answer: High: a secret is stored in source code. Read it from an environment variable.

Example 2
Code: const config = JSON.parse(input);
Answer: Medium: malformed input can crash the request. Validate the input and handle the parsing error.

Review the code in the same concise style. Report every concrete issue you find:

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

High: user ID is not validated, leading to potential SQL injection. The query uses a string interpolation with `${userId}` without checking if the input is a valid integer, which could allow malicious input to be executed as SQL code.
