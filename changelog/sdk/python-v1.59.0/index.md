# SDK Python v1.59.0

Released 2026-10-08
Release: https://github.com/strands-agents/harness-sdk/releases/tag/python/v1.59.0 · Package: https://pypi.org/project/strands-agents/1.59.0/

## Features
- add vended subagent tool [multiagent, tool] (https://github.com/strands-agents/harness-sdk/pull/4841)

## Fixes
- map RECITATION finish reason to content\_filtered (https://github.com/strands-agents/harness-sdk/pull/4898)
- resume nested agent-as-tool interrupts across rehydration [multiagent, hil] (https://github.com/strands-agents/harness-sdk/pull/3675)
- classify every 429 as throttling regardless of body format [model] (https://github.com/strands-agents/harness-sdk/pull/4524)
- drop the leading blank line on tool-result turns (py) [model, interventions] (https://github.com/strands-agents/harness-sdk/pull/4828)
- support Anthropic cache writes on older LiteLLM [model] (https://github.com/strands-agents/harness-sdk/pull/4979)

## Other
- decision model primitive (TS-first rework of 0020) (https://github.com/strands-agents/harness-sdk/pull/4891)
