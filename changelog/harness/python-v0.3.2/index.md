# Harness Python v0.3.2

Released 2026-10-22
Release: https://github.com/strands-agents/harness-sdk/releases/tag/harness-python/v0.3.2 · Package: https://pypi.org/project/strands-harness/0.3.2/

## Features
- add harness, CLI, and box release streams (https://github.com/strands-agents/harness-sdk/pull/5192)
- add docs-verifier skill (https://github.com/strands-agents/harness-sdk/pull/5268)

## Fixes
- make the file tools work on Windows and run Windows CI for harness-ts, harness-py and strands-cli [tool] (https://github.com/strands-agents/harness-sdk/pull/4978)
- enable Bedrock Mantle web search for GPT-6.1 Sol [model] (https://github.com/strands-agents/harness-sdk/pull/5188)
- inject memory on user turns only, matching the SDK default [context] (https://github.com/strands-agents/harness-sdk/pull/5298)
- sniff image bytes in read so a non-image or mislabeled file is not sent as an image [model, tool] (https://github.com/strands-agents/harness-sdk/pull/5311)
- run web\_fetch's curl through PowerShell when the sandbox speaks it [tool, server] (https://github.com/strands-agents/harness-sdk/pull/5328)

## Other
- backfill harness, CLI, and box releases (https://github.com/strands-agents/harness-sdk/pull/5193)
- add 0021 cache-friendly tool management [tool] (https://github.com/strands-agents/harness-sdk/pull/5161)
- bump re-actors/alls-green from 1.2.2 to 1.3.0 (https://github.com/strands-agents/harness-sdk/pull/3963)
- apply area-catalog label to PRs touching catalog entries (https://github.com/strands-agents/harness-sdk/pull/5334)
- bump actions/upload-artifact from 7.0.1 to 7.0.2 (https://github.com/strands-agents/harness-sdk/pull/5099)
- bump actions/download-artifact from 8.0.1 to 8.0.2 (https://github.com/strands-agents/harness-sdk/pull/5097)
- bump astral-sh/setup-uv from 10.0.1 to 10.3.0 (https://github.com/strands-agents/harness-sdk/pull/5098)
