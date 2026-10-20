# SDK TypeScript v1.21.0

Released 2026-10-14
Release: https://github.com/strands-agents/harness-sdk/releases/tag/typescript/v1.21.0 · Package: https://www.npmjs.com/package/@strands-agents/sdk/v/1.21.0

## Features
- share the stash across agents through a caller-scoped… [context, sessions] (https://github.com/strands-agents/harness-sdk/pull/5075)
- port vended subagent tool to TypeScript [multiagent, language] (https://github.com/strands-agents/harness-sdk/pull/4971)
- add auxModel for auxiliary model calls (TS port of #4658) [model, agent] (https://github.com/strands-agents/harness-sdk/pull/4783)
- support strict tool use via strictTools config [model, tool] (https://github.com/strands-agents/harness-sdk/pull/4181)
- add SEP-2663 task execution on mcp/ext-tasks [mcp] (https://github.com/strands-agents/harness-sdk/pull/4977)
- add python\_repl vended tool to TS [language, tool] (https://github.com/strands-agents/harness-sdk/pull/5041)
- accept a config object in LocalFileStorage and InMemoryStorage [devx, persistence] (https://github.com/strands-agents/harness-sdk/pull/5090)
- added mcp v2 prompts, resources methods with paginationToken [mcp] (https://github.com/strands-agents/harness-sdk/pull/4296)
- add progress callbacks for tool calls [mcp] (https://github.com/strands-agents/harness-sdk/pull/4302)
- add DecisionModel primitive and LLMDecisionModel [model, structured-output] (https://github.com/strands-agents/harness-sdk/pull/4942)
- package Strands for Claude, Codex, and Cursor [devx] (https://github.com/strands-agents/harness-sdk/pull/5123)

## Fixes
- reject non-finite web fetch size limits [tool] (https://github.com/strands-agents/harness-sdk/pull/4718)
- add context window limit for Haiku 5.5 (py + ts) [context, model] (https://github.com/strands-agents/harness-sdk/pull/4998)
- read chat usage reported on the finish\_reason chunk [model] (https://github.com/strands-agents/harness-sdk/pull/4851)
- rebuild transport and client when reconnecting url-configured clients [mcp] (https://github.com/strands-agents/harness-sdk/pull/4378)
- forward the call signal to connect and fetch task metadata for unlisted tools [mcp] (https://github.com/strands-agents/harness-sdk/pull/5043)
- reject host-filesystem search strategies with a sandbox [persistence] (https://github.com/strands-agents/harness-sdk/pull/5093)
- set include\_server\_side\_tool\_invocations when mixing function declarations with built-in tools [model] (https://github.com/strands-agents/harness-sdk/pull/4754)
- preserve shared connection when creator aborts [mcp] (https://github.com/strands-agents/harness-sdk/pull/5065)

## Other
- decision model primitive (TS-first rework of 0020) (https://github.com/strands-agents/harness-sdk/pull/4891)
- bump source-map-js from 1.2.1 to 1.2.2 (https://github.com/strands-agents/harness-sdk/pull/4928)
- bump @modelcontextprotocol/client from 2.0.0 to 2.3.1 (https://github.com/strands-agents/harness-sdk/pull/4931)
- bump codecov/codecov-action from 7.0.0 to 7.1.1 (https://github.com/strands-agents/harness-sdk/pull/4430)
- cover the legacy fallback through the 2.0 client transports [mcp] (https://github.com/strands-agents/harness-sdk/pull/4278)
