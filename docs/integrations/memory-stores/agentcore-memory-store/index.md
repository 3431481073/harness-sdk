The AgentCore Memory Store, available in Python and TypeScript, implements the Strands [`MemoryStore`](/docs/user-guide/sdk/memory/managing-memory/index.md#custom-stores) interface on top of Amazon Bedrock AgentCore Memory. Search maps to AgentCore’s `RetrieveMemoryRecords`, and conversation turns are ingested for server-side memory extraction into long-term records. Attach it to an agent through a [`MemoryManager`](/docs/user-guide/sdk/memory/overview/index.md) like any other store. See the [Getting Started](/docs/user-guide/sdk/memory/overview/index.md) section for more information.

Use this integration for long-term memory through a memory manager. To persist and restore conversation history, use `SnapshotSessionManager``SessionManager` as described in the [single-agent session guide](/docs/user-guide/sdk/agents/session-management/index.md#single-agent-sessions).

## Requirements

Use an existing [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) resource with extraction strategies and AWS credentials to access it. Match the examples’ namespaces to those configured on your strategies. The store does not create the resource.

(( tab "Python" ))
-   `bedrock-agentcore >= 1.21.0`
-   `strands-agents >= 1.56.0`
(( /tab "Python" ))

(( tab "TypeScript" ))
-   `bedrock-agentcore >= 0.4.1`
-   `@strands-agents/sdk >= 1.5.0`
(( /tab "TypeScript" ))

## Installation

(( tab "Python" ))
```bash
pip install "bedrock-agentcore[strands-agents]>=1.21.0"
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```bash
npm install bedrock-agentcore @strands-agents/sdk
```
(( /tab "TypeScript" ))

## Usage

To recall from multiple namespaces, use `create_agentcore_memory_stores``createAgentCoreMemoryStores`. It builds one store per namespace over a shared client. Attach the stores to an agent through a `MemoryManager` and enable extraction on one writer to capture conversation turns. Writes go to the shared conversation stream; the memory resource’s strategies decide which namespaces receive extracted records.

(( tab "Python" ))
Set `AGENTCORE_MEMORY_ID` to your memory resource ID.

```python
import os

from strands import Agent
from strands.memory import MemoryManager
from bedrock_agentcore.memory.integrations.strands.memorystore import (
    create_agentcore_memory_stores,
)

stores = create_agentcore_memory_stores(
    memory_id=os.environ["AGENTCORE_MEMORY_ID"],
    actor_id="user-123",
    session_id="session-1",
    namespaces=[
        {"namespace": "/facts/{actorId}", "writable": True},
        {"namespace": "/preferences/{actorId}", "min_score": 0.5},
    ],
    extraction=True,
    region_name="us-east-1",
)

manager = MemoryManager(stores=stores)
agent = Agent(memory_manager=manager)
```

The import package is `memorystore`, without an underscore. With extraction enabled, the factory selects the first namespace not explicitly marked `writable=False` when no writer is specified. Set `writable=True` on one namespace to choose the writer explicitly, as above. Omit `extraction` and writer flags for recall-only stores.
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent, MemoryManager, BedrockModel } from '@strands-agents/sdk'
import { createAgentCoreMemoryStores } from 'bedrock-agentcore/memory/strands'

const stores = createAgentCoreMemoryStores({
  memoryId: 'mem-abc',
  actorId: 'user-123',
  sessionId: 'session-1',
  namespaces: [
    { namespace: '/facts/{actorId}', writable: true },
    { namespace: '/preferences/{actorId}', minScore: 0.5 },
  ],
  extraction: true,
})

const agent = new Agent({
  model: new BedrockModel(),
  memoryManager: new MemoryManager({ stores }),
})
```
(( /tab "TypeScript" ))

A single `AgentCoreMemoryStore` can also be constructed directly when you only need one namespace:

(( tab "Python" ))
```python
import os

from strands import Agent
from strands.memory import MemoryManager
from bedrock_agentcore.memory.integrations.strands.memorystore import (
    AgentCoreMemoryStore,
)

store = AgentCoreMemoryStore(
    memory_id=os.environ["AGENTCORE_MEMORY_ID"],
    actor_id="user-123",
    session_id="session-1",
    namespace="/facts/{actorId}",
    writable=True,
    extraction=True,
    region_name="us-east-1",
)
manager = MemoryManager(stores=[store])
agent = Agent(memory_manager=manager)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { AgentCoreMemoryStore } from 'bedrock-agentcore/memory/strands'

const store = new AgentCoreMemoryStore({
  memoryId: 'mem-abc',
  actorId: 'user-123',
  sessionId: 'session-1',
  namespace: '/facts/{actorId}',
  writable: true,
  extraction: true,
})
```
(( /tab "TypeScript" ))

## Configuration

Set namespace-specific options on each factory entry, and identity and extraction options at the top level. The direct `AgentCoreMemoryStore` constructor takes all options in one flat config.

| Option | Type | Description |
| --- | --- | --- |
| `memory_id``memoryId` | string | Memory resource ID. |
| `actor_id``actorId` | string | Replaces `{actorId}`. |
| `session_id``sessionId` | string | Replaces `{sessionId}`. |
| `namespace` | string | Exact namespace prefix for recall. |
| `namespace_path``namespacePath` | string | Subtree query; direct constructor only, instead of `namespace`. |
| `writable` | boolean | Enables conversation writes; false by default on a direct store. |
| `extraction` | boolean or config | Enables automatic dispatch, with cadence and filtering. |
| `min_score``minScore` | number | Minimum relevance score for recall. |

(( tab "Python" ))
For custom extraction cadence, pass an `extraction` dictionary with `cadence` and `filter` to the factory. For example, use `IntervalTrigger(turns=10)` from `strands.memory` as the cadence. The direct constructor uses the Strands `ExtractionConfig`, whose cadence key is `trigger`.

See the [package README](https://github.com/aws/bedrock-agentcore-sdk-python/tree/main/src/bedrock_agentcore/memory/integrations/strands/memorystore) for batching, score filtering, metadata, and the full namespace contract.
(( /tab "Python" ))

(( tab "TypeScript" ))
See the [package README](https://github.com/aws/bedrock-agentcore-sdk-typescript/tree/main/src/memory/integrations/strands) for the full option reference, including subtree reads and over-fetch tuning.
(( /tab "TypeScript" ))

## Writes and shutdown

Conversation writes use `CreateEvent` for server-side extraction, preserving user and assistant roles. Flush pending writes at a shutdown boundary after asynchronous invocation or streaming.

(( tab "Python" ))
Synchronous `agent(...)` calls flush automatically. After `agent.invoke_async(...)` or `agent.stream_async(...)`, call `await manager.flush()` before closing the event loop. Reuse the manager while the same actor and session remain active to retain buffered turns and cadence state.

Strands logs extraction write failures and retains failed batches for retry. A completed `flush()` alone is not proof that events were persisted.

The store implements `add_messages()`, not the flat-string `add()` interface, so it does not enable the manager’s `add_memory` tool. Enable extraction to send conversation turns instead.
(( /tab "Python" ))

(( tab "TypeScript" ))
Await `agent.memoryManager?.flush()` at shutdown to settle pending writes.
(( /tab "TypeScript" ))

A completed flush does not confirm that server-side extraction has finished. Monitor write failures in logs; newly extracted records may not be immediately searchable.

## Notes

-   **One writable store per session.** Mark at most one store `writable` for a given memory resource, actor, and session: multiple writers would emit duplicate events to the same stream. The factory rejects configurations with more than one writer.
-   **Placeholders resolve at construction.** Only `{actorId}` and `{sessionId}` are substituted client-side, into the namespace used for recall. Any other placeholder in a namespace causes construction to throw. Provision strategies with `{actorId}`/`{sessionId}`\-only templates to match.
-   **Cross-session recall.** A namespace containing `{sessionId}` scopes recall to that session. Use an actor-only namespace to recall memories across sessions.

## References

-   [Python integration source and README](https://github.com/aws/bedrock-agentcore-sdk-python/tree/main/src/bedrock_agentcore/memory/integrations/strands/memorystore)
-   [`bedrock-agentcore` on PyPI](https://pypi.org/project/bedrock-agentcore/)
-   [TypeScript integration source and README](https://github.com/aws/bedrock-agentcore-sdk-typescript/tree/main/src/memory/integrations/strands)
-   [`bedrock-agentcore` on npm](https://www.npmjs.com/package/bedrock-agentcore)
-   [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
-   [Report a Python issue](https://github.com/aws/bedrock-agentcore-sdk-python/issues/new/choose)
-   [Report a TypeScript issue](https://github.com/aws/bedrock-agentcore-sdk-typescript/issues/new/choose)