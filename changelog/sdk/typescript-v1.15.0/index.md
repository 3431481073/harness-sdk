# SDK TypeScript v1.15.0

Released 2026-08-27
Release: https://github.com/strands-agents/harness-sdk/releases/tag/typescript/v1.15.0 · Package: https://www.npmjs.com/package/@strands-agents/sdk/v/1.15.0

## Features
- export key-aware extractor and make it model-configurable [model, language] (https://github.com/strands-agents/harness-sdk/pull/3948)
- add cache\_key to CacheConfig for key-routed cache providers [model] (https://github.com/strands-agents/harness-sdk/pull/3949)
- add internal InProcessTaskEngine [async, language] (https://github.com/strands-agents/harness-sdk/pull/3838)
- add sessionId getter to Agent [devx, sessions] (https://github.com/strands-agents/harness-sdk/pull/4000)
- add model routing [model, language] (https://github.com/strands-agents/harness-sdk/pull/3903)

## Fixes
- count Gemini tool-use tokens as input and thinking tokens as output [model] (https://github.com/strands-agents/harness-sdk/pull/3892)
- redact blocked content when guardrail trace is disabled [model, interventions] (https://github.com/strands-agents/harness-sdk/pull/3772)
- harden vercel document test [model] (https://github.com/strands-agents/harness-sdk/pull/3958)
- harden mantle routing integ tests (https://github.com/strands-agents/harness-sdk/pull/3957)
- restore always() in upload-metrics if guard (https://github.com/strands-agents/harness-sdk/pull/3970)
- grant Bidi integration test permissions [bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/3975)
- emit semconv-compliant cache usage attributes [otel] (https://github.com/strands-agents/harness-sdk/pull/3964)
- forward cancellation signal to OpenAI [async, model] (https://github.com/strands-agents/harness-sdk/pull/3936)
- support content blocks in AfterToolsEvent.endTurn and simplify delegation [multiagent, hooks] (https://github.com/strands-agents/harness-sdk/pull/3995)
- treat empty integration test reports as a no-op (https://github.com/strands-agents/harness-sdk/pull/4006)
- count cached tokens in context-size and compaction baseline [context] (https://github.com/strands-agents/harness-sdk/pull/3886)

## Other
- bump dorny/paths-filter from 3.0.2 to 4.0.3 (https://github.com/strands-agents/harness-sdk/pull/3907)
- bump the production-minor group across 1 directory with 2 updates (https://github.com/strands-agents/harness-sdk/pull/3880)
- bump the production-minor group across 1 directory with 3 updates (https://github.com/strands-agents/harness-sdk/pull/3942)
- record decision on null vs undefined input handling (https://github.com/strands-agents/harness-sdk/pull/3889)
