---
name: plan-to-issue
description: Create GitHub [plan] issues from user-provided existing implementation plan from plan mode or etc.
argument-hint: [your plan description or file path]
---

# Plan to Issue Command

This command faithfully converts the user given implementation plan into our
plan guidelines and creates a well-structured GitHub [plan] issue.

Look at the provided $ARGUMENTS.
If it is a file path, read the file content.
If it is direct description text, use it as is.
Based on our `\plan-guidelines` and `\open-issue` skills, create a well-structured GitHub [plan] issue.
Ensure the issue includes all the sections described as the prompt template in `\external-consensus` skill.

Remember, after creating the issue, add a `agentize:pr` label to it for further processing.
