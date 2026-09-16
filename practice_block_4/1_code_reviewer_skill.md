# Code reviewer skill

## 1. Create the skill

Create this directory:

```text
.agents/skills/code-reviewer
```

Inside it, create `SKILL.md` manually in your code editor. Do not use Kit to create or edit the skill. Paste this minimal template:

```md
---
name: code-reviewer
description: Review code for bugs, security issues, and maintainability problems.
---

# Code reviewer

[Write your review instructions here.]
```

Replace the placeholder with instructions that define:

- what the reviewer must check;
- how findings should be prioritized;
- what output format it should use.

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

```
RESULT WITHOUT SKILL
```

---

Result with skill:

```
RESULT WITH SKILL
```
