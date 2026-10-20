# SDK Python v1.57.1

Released 2026-09-25
Release: https://github.com/strands-agents/harness-sdk/releases/tag/python/v1.57.1 · Package: https://pypi.org/project/strands-agents/1.57.1/

## Features
- add Agent.shutdown() for scope-based cleanup [devx, agent] (https://github.com/strands-agents/harness-sdk/pull/4519)
- require explicit model IDs for providers [model, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4525)
- add a2a\_client vended tool [tool, a2a] (https://github.com/strands-agents/harness-sdk/pull/4304)
- add snapshot capture and restore [bidirectional-streaming, persistence] (https://github.com/strands-agents/harness-sdk/pull/4584)

## Fixes
- reject non-boolean classifier decisions [hil] (https://github.com/strands-agents/harness-sdk/pull/4538)
- simplify and clarify CLI UX; fix bugs [context, devx] (https://github.com/strands-agents/harness-sdk/pull/4548)
- extract content from task.status.message when artifacts are absent [a2a] (https://github.com/strands-agents/harness-sdk/pull/4511)
- cap sqlalchemy\<2.1.0 to avoid RecursionError in Hatch dependency check (https://github.com/strands-agents/harness-sdk/pull/4583)
- finalize invocation before yielding the result [multiagent, hooks] (https://github.com/strands-agents/harness-sdk/pull/4580)
- align response boundaries and transcript history [hooks, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4560)
- record tool dispatch in conversation history [tool, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4605)
- rewrite all stored copies of a message when guardrail redacts it [persistence, interventions] (https://github.com/strands-agents/harness-sdk/pull/4606)
- update model id in cancellation integ tests [model] (https://github.com/strands-agents/harness-sdk/pull/4611)

## Other
- enforce formatting checks (https://github.com/strands-agents/harness-sdk/pull/4526)
- add Python lint/format gate to pre-commit hook [devx] (https://github.com/strands-agents/harness-sdk/pull/4528)
- use barge-in terminology [hooks, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4566)
- remove response stop reasons [hooks, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4604)
