By default a Strands agent starts every conversation from zero: it cannot recall a user’s preferences, past decisions, or anything it learned in an earlier session. The `MemoryManager` gives an agent long-term memory that persists across sessions.

Memory works through **memory stores**, the backends that hold what the agent remembers. A store can be the built-in zero-setup [test store](/docs/user-guide/sdk/memory/test-memory-store/index.md), a managed service like [Amazon Bedrock Knowledge Bases](/docs/user-guide/sdk/memory/bedrock-knowledge-base/index.md), or [your own implementation](/docs/user-guide/sdk/memory/managing-memory/index.md#custom-stores). Across the stores you attach, the manager does three jobs:

1.  **Recall** - the agent searches stored knowledge on demand through a tool.
2.  **Injection** - the manager folds relevant knowledge into the prompt automatically, before the model runs.
3.  **Extraction** - turning conversation messages into memories and writing them to stores.

Recall and injection are enabled by default when you attach a store; writing memories is opt-in.

## Give your agent memory

[Control what your agent remembers](../managing-memory/index.md)Configure recall, injection, and extraction, and read or write memory programmatically.

[Test memory store](../test-memory-store/index.md)A zero-setup store backed by a local JSON file, for prototyping and tests.

[File memory store](../file-memory-store/index.md)Knowledge as markdown files on any Storage backend, with topic-aware extraction.

[Bedrock Knowledge Base store](../bedrock-knowledge-base/index.md)A managed store with semantic search over a vector store, for production.

[Build a custom store](../managing-memory/index.md#custom-stores)Back memory with any database or service by implementing the MemoryStore interface.

## A running agent with memory

Attach a memory manager to an agent through the `memory_manager``memoryManager` parameter. The [test store](/docs/user-guide/sdk/memory/test-memory-store/index.md) needs no cloud account and persists to disk by default, so this agent remembers across restarts with no setup:

(( tab "Python" ))
```python
from strands import Agent
from strands.memory import MemoryManager
from strands.vended_memory_stores.test_memory_store import TestMemoryStore

# Persists to ~/.strands/memory/notes.json by default.
store = TestMemoryStore(name="notes")

agent = Agent(memory_manager=MemoryManager(stores=[store]))
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent, BedrockModel } from '@strands-agents/sdk'
import { TestMemoryStore } from '@strands-agents/sdk/vended-memory-stores/test-memory-store'

// Persists to ~/.strands/memory/notes.json by default.
const store = new TestMemoryStore({ name: 'notes' })

const agent = new Agent({
  model: new BedrockModel(),
  memoryManager: { stores: [store] },
})
```
(( /tab "TypeScript" ))

With no further configuration, recall and injection are on. From here you choose a backend and control what the agent reads and writes.

## Where to go next

New to memory? Reach for the [test store](/docs/user-guide/sdk/memory/test-memory-store/index.md) to give an agent memory in one line, then [control what your agent remembers](/docs/user-guide/sdk/memory/managing-memory/index.md) to turn on writing and tune recall, injection, and extraction. For a production backend with semantic search, use the [Bedrock Knowledge Base store](/docs/user-guide/sdk/memory/bedrock-knowledge-base/index.md).

Memory is one of three ways an agent carries state. [Session management](/docs/user-guide/sdk/agents/session-management/index.md) persists the full conversation so an agent can resume where it left off; [conversation management](/docs/user-guide/sdk/agents/conversation-management/index.md) keeps a session within the model’s context window; memory carries durable knowledge *across* sessions, without replaying past conversations.

## Related pages

- [Control what your agent remembers](/docs/user-guide/sdk/memory/managing-memory/index.md) (1 shared tag)
- [File Memory Store](/docs/user-guide/sdk/memory/file-memory-store/index.md) (1 shared tag)
- [Test Memory Store](/docs/user-guide/sdk/memory/test-memory-store/index.md) (1 shared tag)
- [Bedrock Knowledge Base Store](/docs/user-guide/sdk/memory/bedrock-knowledge-base/index.md) (1 shared tag)


## Implementation

### Python

- [harness-sdk/strands-py/src/strands/memory/memory_manager.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/memory/memory_manager.py)
- [harness-sdk/strands-py/src/strands/memory/types.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/memory/types.py)

### TypeScript

- [harness-sdk/strands-ts/src/memory/memory-manager.ts](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/memory-manager.ts)
- [harness-sdk/strands-ts/src/memory/types.ts](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/types.ts)
