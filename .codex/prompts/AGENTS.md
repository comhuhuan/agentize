All Codex commands are transplanted from Claude Code.

# Below are copied from Codex official documentation for custom prompts creation.

Several key differences between Codex and Claude Code:

1. Claude Code has per-repo customized prompts located in .claude/commands, while Codex uses a global ~/.codex/prompts/ directory.
2. Claude Code `argument-hint` are just argument hints, while Codex strictly parses them to extract named arguments.
3. Claude Code has native support for sub-agent invocation, while Codex does not support it yet.
   - A workaround is to create a skill that invokes a `codex exec` command in command line.

## Creating custom prompts

Custom prompts turn Markdown files into reusable slash commands that you trigger with /prompts:<name>. Custom prompts require explicit invocation. You can’t share them in repositories. If you want to share a prompt or want Codex to implicitly invoke it, check out skills.

Ensure your Codex home exists:

mkdir -p ~/.codex/prompts

Create ~/.codex/prompts/draftpr.md with reusable guidance:

---
description: Prep a branch, commit, and open a draft PR
argument-hint: [FILES=<paths>] [PR_TITLE="<title>"]
---

Create a branch named `dev/<feature_name>` for this work.
If files are specified, stage them first: $FILES.
Commit the staged changes with a clear message.
Open a draft PR on the same branch. Use $PR_TITLE when supplied; otherwise write a concise summary yourself.

Restart Codex (or start a new session) so it loads the new prompt.

Expected: Typing /prompts:draftpr in the slash popup shows your custom command with the description from the front matter and hints that files and a PR title are optional.

Add metadata and arguments

Codex reads prompt metadata and resolves placeholders the next time the session starts.

Description: Shown under the command name in the popup. Set it in YAML front matter as description:.
Argument hint: Document expected parameters with argument-hint: KEY=<value>.
Positional placeholders: $1 through $9 expand from space-separated arguments you provide after the command. $ARGUMENTS includes them all.
Named placeholders: Use uppercase names like $FILE or $TICKET_ID and supply values as KEY=value. Quote values with spaces (for example, FOCUS="loading state").
Literal dollar signs: Write $$ to emit a single $ in the expanded prompt.
After editing prompt files, restart Codex or open a new chat so the updates load. Codex ignores non-Markdown files in the prompts directory.

Invoke and manage custom commands

Launch Codex and type / to open the popup.

Enter prompts: or the prompt name, for example /prompts:draftpr.

Supply required arguments:

/prompts:draftpr FILES="src/pages/index.astro src/lib/api.ts" PR_TITLE="Add hero animation"

Press Enter to send the expanded instructions (skip either argument when you don’t need it).

Expected: Codex pastes the content of draftpr.md, replacing placeholders with the arguments you supplied. Run /status or /diff afterward to confirm the prompt triggered the intended workflow.

Manage prompts by editing or deleting files under ~/.codex/prompts/. Codex scans only the top-level Markdown files in that folder, so place each custom prompt directly under ~/.codex/prompts/ rather than in subdirectories.


