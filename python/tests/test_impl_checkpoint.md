# test_impl_checkpoint.py

Unit tests for checkpoint serialization and resumption state contracts in the
`impl` workflow.

## Purpose

This module validates that workflow state can be persisted and restored
deterministically across interruptions, including stage values used by the
explicit FSM loop.

## Coverage

- `ImplState` dictionary serialization and deserialization
- checkpoint write/read behavior and version validation
- checkpoint existence probing for valid and invalid files
- initial state construction defaults
- stage round-trip behavior including `rebase` stage values

## Design Rationale

Checkpoint tests prioritize hard guarantees around data contract stability and
resumption safety. They intentionally avoid testing model-facing behavior and
focus on deterministic persistence boundaries.
