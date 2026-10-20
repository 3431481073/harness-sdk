# SDK TypeScript v1.20.0

Released 2026-10-08
Release: https://github.com/strands-agents/harness-sdk/releases/tag/typescript/v1.20.0 · Package: https://www.npmjs.com/package/@strands-agents/sdk/v/1.20.0

## Features
- swap to @modelcontextprotocol/client 2.0 [mcp] (https://github.com/strands-agents/harness-sdk/pull/4093)
- add Agent.shutdown() for scope-based cleanup [devx, agent] (https://github.com/strands-agents/harness-sdk/pull/4519)
- add strands update and polish compact, skills, rename, and setup flows [context, devx] (https://github.com/strands-agents/harness-sdk/pull/4612)
- export InterruptError from the TypeScript SDK [devx, hil] (https://github.com/strands-agents/harness-sdk/pull/4541)
- port a2a\_client tool to TypeScript [tool, a2a] (https://github.com/strands-agents/harness-sdk/pull/4575)
- add Strands coding-agent skill [agent] (https://github.com/strands-agents/harness-sdk/pull/4739)
- use agent.cancel() to stop the event loop [tool, agent] (https://github.com/strands-agents/harness-sdk/pull/3506)
- migrate agent axis policies to SDKs [multiagent, config] (https://github.com/strands-agents/harness-sdk/pull/4714)
- port mcp\_router vended tool to TypeScript [mcp, tool] (https://github.com/strands-agents/harness-sdk/pull/4448)
- restore legacy task execution on the SDK 2.x client [mcp] (https://github.com/strands-agents/harness-sdk/pull/4711)
- expose tool client accessor [devx, mcp] (https://github.com/strands-agents/harness-sdk/pull/4863)

## Fixes
- simplify and clarify CLI UX; fix bugs [context, devx] (https://github.com/strands-agents/harness-sdk/pull/4548)
- include cache tokens in totalTokens [context, model] (https://github.com/strands-agents/harness-sdk/pull/4219)
- surface prompt-cache write tokens on TS OpenAI and Bedrock paths [model] (https://github.com/strands-agents/harness-sdk/pull/4617)
- format model-facing numbers independently of the host locale [context, language] (https://github.com/strands-agents/harness-sdk/pull/4682)
- add context window limits for Sonnet 5.5, Opus 5.5, Fable 5.1 (py + ts) [context, model] (https://github.com/strands-agents/harness-sdk/pull/4694)
- retry failed multi-agent restore [multiagent, sessions] (https://github.com/strands-agents/harness-sdk/pull/4663)
- store redacted thinking as bytes and re-encode on send [model, sessions] (https://github.com/strands-agents/harness-sdk/pull/4593)
- skip overlong prefixed tools when continuing on error [mcp] (https://github.com/strands-agents/harness-sdk/pull/4569)
- include traceAttributes on chat, execute\_tool, and cycle spans [otel] (https://github.com/strands-agents/harness-sdk/pull/4669)
- broaden Mantle gpt-6 prefix to cover dot-separated model ids [model] (https://github.com/strands-agents/harness-sdk/pull/4882)
- propagate and resume nested agent-as-tool interrupts [multiagent, hil] (https://github.com/strands-agents/harness-sdk/pull/4782)

## Other
- bump ip-address from 10.4.0 to 10.7.2 (https://github.com/strands-agents/harness-sdk/pull/4690)
- add Human Overview sections to templates per AI usage reflection (https://github.com/strands-agents/harness-sdk/pull/4696)
- add note on invocation state [agent] (https://github.com/strands-agents/harness-sdk/pull/4744)
- add Observability catalog type [otel] (https://github.com/strands-agents/harness-sdk/pull/4772)
- bump brace-expansion from 5.0.7 to 5.0.12 (https://github.com/strands-agents/harness-sdk/pull/4730)
- bump vitest from 4.1.10 to 4.1.11 (https://github.com/strands-agents/harness-sdk/pull/4387)
- bump browserslist from 4.28.2 to 4.28.8 in /test-infra in the npm\_and\_yarn group across 1 directory (https://github.com/strands-agents/harness-sdk/pull/4110)
- bump proxy-addr from 2.0.7 to 2.0.8 (https://github.com/strands-agents/harness-sdk/pull/4929)
