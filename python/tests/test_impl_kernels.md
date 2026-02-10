# test_impl_kernels.py

Unit tests for helper and stage-kernel behaviors in the `impl` workflow.

## Purpose

This module validates deterministic contracts for utility helpers and
stage-facing kernel functions that interact with git and PR/rebase flows.

## Coverage

- score extraction and completion marker parsing helpers
- shell command construction and optional file-read helpers
- remote/base-branch/current-branch detection helpers
- PR stage event routing (`pr_pass` / `pr_fail_fixable` / `pr_fail_need_rebase`)
- rebase stage event routing (`rebase_ok` / `rebase_conflict`)
- structured artifact creation for PR and rebase stage diagnostics

## Design Rationale

These tests emphasize objective stage contracts and event determinism instead
of subjective model output quality. This keeps flow-control semantics stable
while implementation prompts and provider behavior evolve.
