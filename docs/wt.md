# `wt`: Git worktree helper

## Getting Started

This is a part of `source setup.sh`.
After that, you can use the `wt` command in your terminal.

## Commands and Subcommands

- `wt init`: Initialize the `trees` directory to hold git worktrees, as well as set up the main branch
   in `$PROJECT_ROOT/trees/main`.
   - NOTE: No matter the default branch is `main` or `master`, it will always be in `trees/main`.
   - NOTE: This is a git constraint: if you create  `trees/main`, your $PROJECT_ROOT` will:
     - still be valid as a git repository,
     - but you cannot checkout `main` branch in `$PROJECT_ROOT` anymore.
- `wt main`: Goes to the directory of `$PROJECT_ROOT/trees/main`.
- `wt spawn <issue-no>`: Create a new worktree for the given issue number from the main branch.
  - NOTE: The main branch is in `$PROJECT_ROOT/trees/main`, not the `$PROJECT_ROOT` itself.
- `wt remove <issue-no>`: It removes the worktree in `trees` directory for the given issue number,
   as well as deletes the corresponding branch.
- `wt list`: List all existing worktrees in the `trees` directory.
- `wt prune`: Remove all worktrees that have been deleted from the remote repository.
- `wt help`: Display help information about the `wt` command and its subcommands.
