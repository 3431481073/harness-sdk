# SDK Python v1.58.0

Released 2026-10-05
Release: https://github.com/strands-agents/harness-sdk/releases/tag/python/v1.58.0 · Package: https://pypi.org/project/strands-agents/1.58.0/

## Features
- support BidiAgent in SnapshotSessionManager [bidirectional-streaming, persistence] (https://github.com/strands-agents/harness-sdk/pull/4603)
- add aux\_model for auxiliary model calls [context, agent] (https://github.com/strands-agents/harness-sdk/pull/4658)
- add Strands coding-agent skill [agent] (https://github.com/strands-agents/harness-sdk/pull/4739)
- use agent.cancel() to stop the event loop [tool, agent] (https://github.com/strands-agents/harness-sdk/pull/3506)
- migrate agent axis policies to SDKs [multiagent, config] (https://github.com/strands-agents/harness-sdk/pull/4714)
- normalize token usage events [model, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4886)

## Fixes
- skip guardContent wrap for blank text [model, interventions] (https://github.com/strands-agents/harness-sdk/pull/4693)
- tolerate missing usage metadata on final response [model] (https://github.com/strands-agents/harness-sdk/pull/4724)
- retry failed multi-agent restore [multiagent, sessions] (https://github.com/strands-agents/harness-sdk/pull/4663)
- preserve anyOf for nullable enums and respect model\_json\_schema overrides [model, structured-output] (https://github.com/strands-agents/harness-sdk/pull/4610)
- confirm OpenAI interruptions and fix console rendering [bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4792)
- prevent hang when server connection drops during in-flight tool call [async, mcp] (https://github.com/strands-agents/harness-sdk/pull/4499)
- save sessions before restart and document checkpoints [bidirectional-streaming, persistence] (https://github.com/strands-agents/harness-sdk/pull/4813)
- forward numeric keep\_alive values such as 0 [model] (https://github.com/strands-agents/harness-sdk/pull/4725)
- remove sqlalchemy\<2.1.0 cap, fixed upstream in 2.1.1 (https://github.com/strands-agents/harness-sdk/pull/4674)
- emit OpenAI usage before response stop [model, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4889)
- broaden Mantle gpt-6 prefix to cover dot-separated model ids [model] (https://github.com/strands-agents/harness-sdk/pull/4882)

## Other
- remove directory tool watching [devx, bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4746)
- add note on invocation state [agent] (https://github.com/strands-agents/harness-sdk/pull/4744)
- add Observability catalog type [otel] (https://github.com/strands-agents/harness-sdk/pull/4772)
- rename the Realtime section to Voice and move its pages to /sdk/bidi/ (https://github.com/strands-agents/harness-sdk/pull/4793)
- update mistralai requirement from \<3.0.0,\>=2.0.0 to \>=2.0.0,\<4.0.0 in /strands-py (https://github.com/strands-agents/harness-sdk/pull/4809)
- document input content [bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4824)
- rewrite I/O streams guide [bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4858)
- update python readme information for bidi [bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4866)
- rename auto\_reconnect to auto\_restart [bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4740)
- add tools guide and clean up failed context entry [bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4836)
- bump browserslist from 4.28.2 to 4.28.8 in /test-infra in the npm\_and\_yarn group across 1 directory (https://github.com/strands-agents/harness-sdk/pull/4110)
- correct connection and audio docstrings [bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4884)
- blog: announce Bidi Agents general availability [bidirectional-streaming] (https://github.com/strands-agents/harness-sdk/pull/4899)
