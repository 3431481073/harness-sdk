# SDK Python v1.57.2

Released 2026-10-01
Release: https://github.com/strands-agents/harness-sdk/releases/tag/python/v1.57.2 · Package: https://pypi.org/project/strands-agents/1.57.2/

## Features
- support grouped content messages [bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4609)
- add strands update and polish compact, skills, rename, and setup flows [context, devx] (https://github.com/strands-agents/harness-sdk/pull/4612)
- add agent-level storage to BidiAgent [bidirectional-streaming, persistence] (https://github.com/strands-agents/harness-sdk/pull/4616)
- bring LocalAgent to parity with the TypeScript interface [devx, agent] (https://github.com/strands-agents/harness-sdk/pull/4639)
- add text and reasoning stream events [bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4624)
- support typing and speech in a shared console [devx, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4640)
- preserve grouped tool calls through execution and delivery [tool, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4687)
- support cancellation from custom tools [tool, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4664)
- display tool calls in console I/O [devx, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4703)
- port a2a\_client tool to TypeScript [tool, a2a] (https://github.com/strands-agents/harness-sdk/pull/4575)
- graduate bidirectional streaming API [devx, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4707)

## Fixes
- include cache tokens in totalTokens [context, model] (https://github.com/strands-agents/harness-sdk/pull/4219)
- map cache\_write\_tokens to cacheWriteInputTokens [model] (https://github.com/strands-agents/harness-sdk/pull/4193)
- defer OpenAI responses during user speech [model, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4642)
- return portable filename from FileStorage.store instead of host path [persistence] (https://github.com/strands-agents/harness-sdk/pull/4568)
- deliver tool results that finish after a connection restart [tool, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4677)
- normalize tool inputs before replay [model, tool] (https://github.com/strands-agents/harness-sdk/pull/4625)
- add context window limits for Sonnet 5.5, Opus 5.5, Fable 5.1 (py + ts) [context, model] (https://github.com/strands-agents/harness-sdk/pull/4694)
- skip location-source documents in OpenAIResponsesModel message formatting [model] (https://github.com/strands-agents/harness-sdk/pull/4706)
- keep stashed originals when backfilling after session resume [context, sessions] (https://github.com/strands-agents/harness-sdk/pull/4699)

## Other
- bump cedar-policy-mcp-schema-generator from 0.6.0 to 0.6.1 in /strands-py (https://github.com/strands-agents/harness-sdk/pull/4650)
- remove session manager configuration [bidirectional-streaming, sessions] (https://github.com/strands-agents/harness-sdk/pull/4698)
- add Human Overview sections to templates per AI usage reflection (https://github.com/strands-agents/harness-sdk/pull/4696)
- make tool execution internals private [devx, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4708)
- use restart consistently for connection restarts [bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4734)
- correct docstrings and drop unused barge-in and connection stop reasons [bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4728)
