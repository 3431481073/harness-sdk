# Harness TypeScript v0.3.1

Released 2026-10-21
Release: https://github.com/strands-agents/harness-sdk/releases/tag/harness-typescript/v0.3.1 · Package: https://www.npmjs.com/package/@strands-agents/harness/v/0.3.1

## Features
- add harness, CLI, and box release streams (https://github.com/strands-agents/harness-sdk/pull/5192)
- add docs-verifier skill (https://github.com/strands-agents/harness-sdk/pull/5268)

## Fixes
- send adaptive thinking to Claude Haiku 5.5 [model] (https://github.com/strands-agents/harness-sdk/pull/5159)
- surface the child's stop reason instead of masking blocked runs as success [multiagent, interventions] (https://github.com/strands-agents/harness-sdk/pull/5165)
- make the file tools work on Windows and run Windows CI for harness-ts, harness-py and strands-cli [tool] (https://github.com/strands-agents/harness-sdk/pull/4978)
- enable Bedrock Mantle web search for GPT-6.1 Sol [model] (https://github.com/strands-agents/harness-sdk/pull/5188)
- inject memory on user turns only, matching the SDK default [context] (https://github.com/strands-agents/harness-sdk/pull/5298)
- sniff image bytes in read so a non-image or mislabeled file is not sent as an image [model, tool] (https://github.com/strands-agents/harness-sdk/pull/5311)

## Other
- redraw docs diagrams as theme-aware SVGs (https://github.com/strands-agents/harness-sdk/pull/5135)
- backfill harness, CLI, and box releases (https://github.com/strands-agents/harness-sdk/pull/5193)
- add 0021 cache-friendly tool management [tool] (https://github.com/strands-agents/harness-sdk/pull/5161)
