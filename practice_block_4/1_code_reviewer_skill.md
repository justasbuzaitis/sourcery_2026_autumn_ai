# Code reviewer skill

## 1. Create the skill

Create this directory:

```text
.agents/skills/code-reviewer
```

Inside it, create `SKILL.md` manually in your code editor. Do not use Kit to create or edit the skill. Paste this minimal skill:

```md
---
name: code-reviewer
description: Review code for bugs, security issues, and maintainability problems.
---

# Code reviewer

Review the provided code and report only concrete issues.

Output:
- **High** — serious security/correctness issue
- **Medium** — meaningful reliability/maintainability issue
- **Low** — minor quality/style issue

For each issue:
**[Severity] Title** — short explanation + suggested fix.

Rules:
- Review only. Do not edit files or use tools.
- Explain the impact, not just the rule being violated.
- Avoid praise, summaries, and generic advice.
- Be concise. Keep each finding to 1–2 sentences.
- Suggest the smallest practical fix.
```

## 2. Validate the skill

```sh
kit skill validate .agents/skills/code-reviewer
kit skill list
```

Both commands must show `code-reviewer` without warnings.

## 3. Review without the skill

Use this question for both reviews:

```text
Review the following Node.js function.

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

```sh
kit --model custom/qwen-local --no-skills
```

Ask the question and save the answer. Exit Kit.

## 4. Review with the skill

```sh
kit --model custom/qwen-local
```

Activate the skill:

```text
/code-reviewer CODE_HERE
```

Ask the same question and save the answer.

## 5. Compare results

Result without skill:

```text
1. SQL injection: `userId` is inserted directly into SQL. Use a parameterized query.
2. Sensitive logging: the complete user row may be written to production logs.
3. Error handling: database query failures are not handled.
```

---

Result with skill:

```text
The function is vulnerable to SQL injection because `userId` is inserted directly into the query. Use a parameterized query.
```

The skill response was shorter, but the model ignored the requested severity format and suggested `?` as the placeholder. PostgreSQL uses `$1`.
