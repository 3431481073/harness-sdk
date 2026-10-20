# Harness Python v0.2.0

Released 2026-10-08
Release: https://github.com/strands-agents/harness-sdk/releases/tag/harness-python/v0.2.0 · Package: https://pypi.org/project/strands-harness/0.2.0/

## Features
- add Agent.shutdown() for scope-based cleanup [devx, agent] (https://github.com/strands-agents/harness-sdk/pull/4519)
- add Strands coding-agent skill [agent] (https://github.com/strands-agents/harness-sdk/pull/4739)
- use agent.cancel() to stop the event loop [tool, agent] (https://github.com/strands-agents/harness-sdk/pull/3506)

## Fixes
- reject caching values other than 'auto', a bool, or None [devx, model] (https://github.com/strands-agents/harness-sdk/pull/4631)
- remove context offloader plugin from harness in favor of context manager's stash (https://github.com/strands-agents/harness-sdk/pull/4701)
- log at info when the default web\_search is unavailable [devx, server] (https://github.com/strands-agents/harness-sdk/pull/4786)
- require SDK 1.57.2 for session restore [persistence, sessions] (https://github.com/strands-agents/harness-sdk/pull/4974)

## Other
- add versioning policy for Strands harness and the CLI (https://github.com/strands-agents/harness-sdk/pull/4535)
- add Python lint/format gate to pre-commit hook [devx] (https://github.com/strands-agents/harness-sdk/pull/4528)
- update default model (https://github.com/strands-agents/harness-sdk/pull/4661)
- add Human Overview sections to templates per AI usage reflection (https://github.com/strands-agents/harness-sdk/pull/4696)
- add Observability catalog type [otel] (https://github.com/strands-agents/harness-sdk/pull/4772)
- bump browserslist from 4.28.2 to 4.28.8 in /test-infra in the npm\_and\_yarn group across 1 directory (https://github.com/strands-agents/harness-sdk/pull/4110)
