# SDK Python v1.61.0

Released 2026-10-14
Release: https://github.com/strands-agents/harness-sdk/releases/tag/python/v1.61.0 · Package: https://pypi.org/project/strands-agents/1.61.0/

## Features
- support client-level request metadata (\_meta) on tool calls [mcp] (https://github.com/strands-agents/harness-sdk/pull/4660)
- package Strands for Claude, Codex, and Cursor [devx] (https://github.com/strands-agents/harness-sdk/pull/5123)

## Fixes
- map content\_filter finish reason to content\_filtered [model, interventions] (https://github.com/strands-agents/harness-sdk/pull/5072)
- map a content-filtered Responses API run to content\_filtered [model] (https://github.com/strands-agents/harness-sdk/pull/5074)
- serialize multi-agent snapshot saves [multiagent, persistence] (https://github.com/strands-agents/harness-sdk/pull/4673)
- map cancelled agent results to FAILED and stop downstream routing [multiagent] (https://github.com/strands-agents/harness-sdk/pull/4753)
- set include\_server\_side\_tool\_invocations when mixing function declarations with built-in tools [model] (https://github.com/strands-agents/harness-sdk/pull/4754)

## Other
- update ruff requirement from \<0.17.0,\>=0.16.0 to \>=0.16.0,\<0.18.0 in /strands-py (https://github.com/strands-agents/harness-sdk/pull/5100)
- bump codecov/codecov-action from 7.0.0 to 7.1.1 (https://github.com/strands-agents/harness-sdk/pull/4430)
