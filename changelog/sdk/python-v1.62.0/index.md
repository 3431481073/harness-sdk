# SDK Python v1.62.0

Released 2026-10-21
Release: https://github.com/strands-agents/harness-sdk/releases/tag/python/v1.62.0 · Package: https://pypi.org/project/strands-agents/1.62.0/

## Features
- add swarm tool in TypeScript [multiagent, tool] (https://github.com/strands-agents/harness-sdk/pull/5204)
- make the Python middleware system public [devx, hooks] (https://github.com/strands-agents/harness-sdk/pull/4976)
- add swarm tool in Python [multiagent, tool] (https://github.com/strands-agents/harness-sdk/pull/4922)
- use agent.cancel() to stop the event loop (Python) [hil, agent] (https://github.com/strands-agents/harness-sdk/pull/4833)
- add harness, CLI, and box release streams (https://github.com/strands-agents/harness-sdk/pull/5192)
- add docs-verifier skill (https://github.com/strands-agents/harness-sdk/pull/5268)
- add experimental OpenAI Live provider [model, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/5286)

## Fixes
- add context window limits for GPT-6 Sol, Luna and 6.1 Sol (py + ts) [context, model] (https://github.com/strands-agents/harness-sdk/pull/5147)
- invoke endpoints off the event loop [async, model] (https://github.com/strands-agents/harness-sdk/pull/5034)
- keep assistant text that sits beside tool calls [model] (https://github.com/strands-agents/harness-sdk/pull/4919)
- retry with drop\_block when a history edit invalidates replayed thinking [context, model] (https://github.com/strands-agents/harness-sdk/pull/5171)
- delegate FileMemoryStore search, scope storage namespaces [persistence] (https://github.com/strands-agents/harness-sdk/pull/5117)
- replace retired Claude Sonnet 4 model IDs with Sonnet 4.6 [model] (https://github.com/strands-agents/harness-sdk/pull/5241)
- preserve tool result adjacency in mistral, writer and llamacpp [model] (https://github.com/strands-agents/harness-sdk/pull/5248)
- run the default local environment's commands on Windows [server] (https://github.com/strands-agents/harness-sdk/pull/5244)
- add DISPATCHED status to prevent fan-in double-execution on resume (#3633) [async, multiagent] (https://github.com/strands-agents/harness-sdk/pull/3724)
- let providers enforce structured output when a model cannot be forced [model, structured-output] (https://github.com/strands-agents/harness-sdk/pull/5190)
- inherit the parent's interventions in the default subagent builder [multiagent, interventions] (https://github.com/strands-agents/harness-sdk/pull/5200)
- drop unsigned reasoning instead of raising KeyError [model] (https://github.com/strands-agents/harness-sdk/pull/5247)
- fix test flakiness caused by set\_tracer\_provider pollution [otel] (https://github.com/strands-agents/harness-sdk/pull/5270)
- add context window limits for GLM-5, 5.3 and 4.7 Flash (py + ts) [context, model] (https://github.com/strands-agents/harness-sdk/pull/5301)
- always append the JSON output format to ModelExtractor prompts [tool, agent] (https://github.com/strands-agents/harness-sdk/pull/5269)
- cap litellm below 1.107.0 [model] (https://github.com/strands-agents/harness-sdk/pull/5307)
- run Bedrock knowledge base calls off the event loop [async, persistence] (https://github.com/strands-agents/harness-sdk/pull/5053)
- render tool calls as text in summarizer input [context, model] (https://github.com/strands-agents/harness-sdk/pull/5293)

## Other
- fix typos in comments and docstrings (https://github.com/strands-agents/harness-sdk/pull/4997)
- backfill harness, CLI, and box releases (https://github.com/strands-agents/harness-sdk/pull/5193)
- add 0021 cache-friendly tool management [tool] (https://github.com/strands-agents/harness-sdk/pull/5161)
- skip audio integ tests when Bedrock rejects audio input [model] (https://github.com/strands-agents/harness-sdk/pull/5310)
- skip flaky multi-turn cache read test [model] (https://github.com/strands-agents/harness-sdk/pull/5314)
