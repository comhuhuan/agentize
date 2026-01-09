# Telegram Approval

Manual approval workflow via Telegram for hands-off automation.

## Overview

When rule-based permissions return `ask` (or when Haiku LLM evaluation is uncertain), the permission system can escalate to Telegram for manual approval. This enables secure hands-off operation by letting you approve/deny tool calls from your phone.

## Configuration

Enable Telegram approval with these environment variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `AGENTIZE_USE_TG` | Yes | Set to `1`, `true`, or `on` to enable |
| `TG_API_TOKEN` | Yes | Telegram Bot API token |
| `TG_CHAT_ID` | Yes | Chat ID to send approval requests to |
| `TG_APPROVAL_TIMEOUT_SEC` | No | Timeout in seconds (default: 60) |
| `TG_POLL_INTERVAL_SEC` | No | Poll interval in seconds (default: 5) |
| `TG_ALLOWED_USER_IDS` | No | Comma-separated list of allowed user IDs |

## Approval Flow

1. Server sends a message to your Telegram chat with tool details:
   - Tool name
   - Target (command/file path)
   - Session ID (truncated)

2. You respond using inline buttons or text commands:
   - **Buttons**: Tap "Allow" or "Deny"
   - **Commands**: Send `/allow` or `/deny`

3. The original message is updated to show the decision result

4. If no response within timeout, returns `ask` (falls back to Claude Code's default behavior)
