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

- **SQL Injection Vulnerability**  
  The query is directly interpolated with `userId` in the string, allowing attackers to inject malicious SQL code (e.g., `userId = '1; DROP TABLE users;'`). This is a **critical security risk** that can lead to data corruption or unauthorized access.  

  **Fix**: Use parameterized queries with `db.query('SELECT * FROM users WHERE id = ?', [userId])` to prevent SQL injection.  

- **Maintainability Issues**  
  The query is built using string concatenation, making the code hard to read and maintain. This increases the risk of errors and reduces collaboration efficiency.  

  **Fix**: Refactor the query to use a database client library (e.g., `pg` for PostgreSQL) that supports parameterized queries, or use a ORM (e.g., Sequelize) to abstract SQL logic.  

- **Parameterized Query Not Used**  
  The function does not use prepared statements, leaving the query vulnerable to SQL injection even if the input is sanitized. This is a **moderate security issue**.  

  **Fix**: Replace direct string interpolation with parameterized queries to ensure the input is properly escaped and validated.  

- **Data Integrity Risk**  
  The function returns the first row in `result.rows[0]` even if there are multiple rows or none. This could lead to incorrect data retrieval or errors in downstream logic.  

  **Fix**: Validate the number of rows returned and handle edge cases (e.g., `result.rows.length > 0` or `result.rows.length == 0`) to ensure correctness.  

---

**Summary**:  
1. **Critical**: SQL injection via direct string interpolation.  
2. **Moderate**: Maintainability and parameterized query absence.  
3. **Moderate**: Data integrity risk from improper row handling.  
4. **Maintainability**: Hard-to-read query structure.
