# pipeline.sh

Multi-agent planning pipeline orchestration for the CLI planner. This module is sourced by
`src/cli/planner.sh` and exposes pipeline entry points plus shared rendering helpers.

## External Interface

### _planner_run_pipeline "<feature-description>" [issue-mode] [verbose] [refine-issue-number]
Runs the full multi-stage planning pipeline (understander -> bold-proposer -> critique/reducer in parallel -> external consensus).

**Parameters**:
- `feature-description`: Request text or issue body used to build the prompts.
- `issue-mode`: `"true"` to create/publish to a GitHub issue when possible; `"false"` for timestamp-only artifacts.
- `verbose`: `"true"` to print detailed progress messages to stderr.
- `refine-issue-number`: Optional issue number to refine an existing plan; fetches the issue body and appends refinement focus.

**Behavior**:
- Creates stage artifacts under `.tmp/` using an issue-based or timestamp prefix.
- Loads planner backends from `.agentize.local.yaml` (planner.* keys) when present.
- Runs agent stages via `acw`, then synthesizes a consensus plan via the external-consensus skill.
- Publishes the plan to the issue when `issue-mode` is true and an issue number is available.

**Output**:
- Prints stage progress and summary to stderr.
- Prints the consensus plan path via `term_label` to stdout.

**Exit codes**:
- `0`: Success.
- `1`: Configuration or setup failure (repo root/backends).
- `2`: Pipeline stage failure (prompt render, agent run, or consensus synthesis).

### _planner_render_prompt <output-file> <agent-md-path> <include-plan-guideline> <feature-desc> [context-file]
Builds a prompt file by concatenating the agent base prompt, optional plan-guideline, the feature request,
and optional context from a previous stage.

**Parameters**:
- `output-file`: Path to write the rendered prompt.
- `agent-md-path`: Repo-relative path to the agent prompt markdown.
- `include-plan-guideline`: `"true"` to append the plan-guideline skill content.
- `feature-desc`: Feature request text inserted into the prompt.
- `context-file`: Optional path to append prior stage output.

**Exit codes**:
- `0`: Success.
- `1`: Missing repo root or agent prompt file.

## Internal Helpers

### _planner_color_enabled / _planner_anim_enabled
Checks whether colored output or animation is enabled on stderr based on environment flags and TTY state.

### _planner_print_feature
Prints a styled "Feature:" label and description using `term_label`.

### _planner_timer_start / _planner_timer_log
Tracks stage timings using epoch seconds and logs elapsed durations.

### _planner_anim_start / _planner_anim_stop
Manages a simple dot animation on stderr to show stage progress.

### _planner_print_issue_created
Prints a styled "issue created" message using `term_label`.

### _planner_validate_backend
Validates backend specs in `provider:model` format; emits errors for invalid inputs.

### _planner_load_backend_config
Loads `planner.*` backend overrides from `.agentize.local.yaml` via helper module
`lib/local_config_io` with a Python fallback parser.

### _planner_acw_run
Runs `acw` with provider/model and optional Claude-only flags (tools/permission mode).

### _planner_log / _planner_stage
Logging helpers for verbose and stage-specific stderr output.
