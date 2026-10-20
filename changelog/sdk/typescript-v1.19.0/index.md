# SDK TypeScript v1.19.0

Released 2026-09-22
Release: https://github.com/strands-agents/harness-sdk/releases/tag/typescript/v1.19.0 · Package: https://www.npmjs.com/package/@strands-agents/sdk/v/1.19.0

## Features
- non-clobbering seam for Anthropic-direct server-side tools (web search) [devx, model] (https://github.com/strands-agents/harness-sdk/pull/3568)
- port handoff\_to\_user tool to TypeScript [hil, tool] (https://github.com/strands-agents/harness-sdk/pull/4382)
- requestTimeout option on BedrockModel [devx, model] (https://github.com/strands-agents/harness-sdk/pull/4408)
- launch the redesigned Strands website (https://github.com/strands-agents/harness-sdk/pull/4446)

## Fixes
- deliver background results through the registered management tool [async, tool] (https://github.com/strands-agents/harness-sdk/pull/4347)
- reject unrecognized limits keys instead of silently applying no cap [devx, agent] (https://github.com/strands-agents/harness-sdk/pull/4356)
- interrupt retry backoff on cancellation [model, agent] (https://github.com/strands-agents/harness-sdk/pull/4291)
- propagate handler-raised interrupts regardless of onError [hil, interventions] (https://github.com/strands-agents/harness-sdk/pull/4373)
- pin the strands command to the commit it was issued against (https://github.com/strands-agents/harness-sdk/pull/4393)
- keep only text when re-roling a summary as a user message [context] (https://github.com/strands-agents/harness-sdk/pull/4421)
- accept a ContextManager instance in Agent contextManager [context, devx] (https://github.com/strands-agents/harness-sdk/pull/4459)
- preserve UTF-8 across stream chunk boundaries [server] (https://github.com/strands-agents/harness-sdk/pull/4157)

## Other
- Rename file number appropriately for design doc 0018-shared-agent-model-types.md (https://github.com/strands-agents/harness-sdk/pull/4376)
- remove duplicate docs-strands-command workflow (https://github.com/strands-agents/harness-sdk/pull/4380)
- add @strands-agents/harness (harness-ts) npm release pipeline (https://github.com/strands-agents/harness-sdk/pull/4455)
- remove stale test issue references (https://github.com/strands-agents/harness-sdk/pull/4467)
- use Strands wordmarks in package READMEs (https://github.com/strands-agents/harness-sdk/pull/4475)
- bump fast-uri from 3.1.5 to 3.1.8 (https://github.com/strands-agents/harness-sdk/pull/4385)
- bump hono from 4.13.0 to 4.13.8 (https://github.com/strands-agents/harness-sdk/pull/4386)
- bump the production-minor group across 1 directory with 3 updates (https://github.com/strands-agents/harness-sdk/pull/4344)
