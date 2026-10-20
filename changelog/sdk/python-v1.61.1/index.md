# SDK Python v1.61.1

Released 2026-10-15
Release: https://github.com/strands-agents/harness-sdk/releases/tag/python/v1.61.1 · Package: https://pypi.org/project/strands-agents/1.61.1/

## Fixes
- text content block is silently dropped when a toolUse is pending in the same content block stop (#4004) [model] (https://github.com/strands-agents/harness-sdk/pull/4067)
- preserve tool result adjacency with injected context [context, model] (https://github.com/strands-agents/harness-sdk/pull/5158)
- keep removal markers and summaries out of message 0 [context] (https://github.com/strands-agents/harness-sdk/pull/5121)
- drop reasoning blocks the target model rejects when history crosses model families [context, model] (https://github.com/strands-agents/harness-sdk/pull/5166)

## Other
- redraw docs diagrams as theme-aware SVGs (https://github.com/strands-agents/harness-sdk/pull/5135)
