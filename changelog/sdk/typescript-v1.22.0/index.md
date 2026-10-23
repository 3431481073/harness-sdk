# SDK TypeScript v1.22.0

Released 2026-10-21
Release: https://github.com/strands-agents/harness-sdk/releases/tag/typescript/v1.22.0 · Package: https://www.npmjs.com/package/@strands-agents/sdk/v/1.22.0

## Features
- add swarm tool in TypeScript [multiagent, tool] (https://github.com/strands-agents/harness-sdk/pull/5204)
- port baggage propagation to TypeScript [otel, language] (https://github.com/strands-agents/harness-sdk/pull/5073)
- make the Python middleware system public [devx, hooks] (https://github.com/strands-agents/harness-sdk/pull/4976)
- use agent.cancel() to stop the event loop (Python) [hil, agent] (https://github.com/strands-agents/harness-sdk/pull/4833)
- add harness, CLI, and box release streams (https://github.com/strands-agents/harness-sdk/pull/5192)
- enforce invoke limits and usage accounting across the whole agent tree [multiagent, agent] (https://github.com/strands-agents/harness-sdk/pull/4667)
- add docs-verifier skill (https://github.com/strands-agents/harness-sdk/pull/5268)
- add decision usage to the request's invocation context [context, model] (https://github.com/strands-agents/harness-sdk/pull/5304)

## Fixes
- return portable filename from TS FileStorage.store [persistence] (https://github.com/strands-agents/harness-sdk/pull/4668)
- keep removal markers and summaries out of message 0 [context] (https://github.com/strands-agents/harness-sdk/pull/5121)
- add context window limits for GPT-6 Sol, Luna and 6.1 Sol (py + ts) [context, model] (https://github.com/strands-agents/harness-sdk/pull/5147)
- report correct paths for values after nested objects in deepCopyWithValidation [devx] (https://github.com/strands-agents/harness-sdk/pull/4981)
- retry with drop\_block when a history edit invalidates replayed thinking [context, model] (https://github.com/strands-agents/harness-sdk/pull/5171)
- delegate FileMemoryStore search, scope storage namespaces [persistence] (https://github.com/strands-agents/harness-sdk/pull/5117)
- replace retired Claude Sonnet 4 model IDs with Sonnet 4.6 [model] (https://github.com/strands-agents/harness-sdk/pull/5241)
- drop reasoning blocks the target model rejects (TypeScript) [model] (https://github.com/strands-agents/harness-sdk/pull/5246)
- omit empty citation source when replaying citations [model] (https://github.com/strands-agents/harness-sdk/pull/5266)
- run the default local environment's commands on Windows [server] (https://github.com/strands-agents/harness-sdk/pull/5244)
- inherit the parent's interventions in the default subagent builder [multiagent, interventions] (https://github.com/strands-agents/harness-sdk/pull/5200)
- add context window limits for GLM-5, 5.3 and 4.7 Flash (py + ts) [context, model] (https://github.com/strands-agents/harness-sdk/pull/5301)
- always append the JSON output format to ModelExtractor prompts [tool, agent] (https://github.com/strands-agents/harness-sdk/pull/5269)
- render tool calls as text in summarizer input [context] (https://github.com/strands-agents/harness-sdk/pull/5292)
- prevent text duplication across streamed content blocks [model, agent] (https://github.com/strands-agents/harness-sdk/pull/5308)

## Other
- redraw docs diagrams as theme-aware SVGs (https://github.com/strands-agents/harness-sdk/pull/5135)
- backfill harness, CLI, and box releases (https://github.com/strands-agents/harness-sdk/pull/5193)
- add 0021 cache-friendly tool management [tool] (https://github.com/strands-agents/harness-sdk/pull/5161)
- skip audio integ tests when Bedrock rejects audio input [model] (https://github.com/strands-agents/harness-sdk/pull/5310)
