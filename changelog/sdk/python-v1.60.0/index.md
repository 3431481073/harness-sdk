# SDK Python v1.60.0

Released 2026-10-12
Release: https://github.com/strands-agents/harness-sdk/releases/tag/python/v1.60.0 · Package: https://pypi.org/project/strands-agents/1.60.0/

## Features
- share the stash across agents through a caller-scoped storage view [context, multiagent] (https://github.com/strands-agents/harness-sdk/pull/4389)
- port vended subagent tool to TypeScript [multiagent, language] (https://github.com/strands-agents/harness-sdk/pull/4971)
- add python\_repl vended tool [tool, server] (https://github.com/strands-agents/harness-sdk/pull/4384)
- propagate OTel baggage context in Python [otel, sessions] (https://github.com/strands-agents/harness-sdk/pull/4840)

## Fixes
- format video content blocks as inline data [model] (https://github.com/strands-agents/harness-sdk/pull/4910)
- add context window limit for Haiku 5.5 (py + ts) [context, model] (https://github.com/strands-agents/harness-sdk/pull/4998)
- warn about reasoningContent once per request [model] (https://github.com/strands-agents/harness-sdk/pull/5016)
- deduplicate usage nudges via stdlib warnings module [devx] (https://github.com/strands-agents/harness-sdk/pull/4983)
