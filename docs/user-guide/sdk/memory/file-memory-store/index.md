`FileMemoryStore` is a [`MemoryStore`](/docs/user-guide/sdk/memory/managing-memory/index.md#stores) that persists memories as markdown files through the SDK’s unified [`Storage`](/docs/user-guide/sdk/storage/index.md) interface. Each topic gets its own `.md` file, and repeated writes to the same topic append rather than overwrite, so related facts accumulate in one place.

Because the store only talks to the `Storage` interface, any backend works: local files, S3, in-memory, or a [custom backend](/docs/user-guide/sdk/storage/index.md#custom-backends) you write for your own database. See [Storage Backend](#storage-backend).

Point it at a store name and the default local-file backend handles the rest:

(( tab "Python" ))
```python
from strands import Agent
from strands.memory import MemoryManager
from strands.vended_memory_stores.file_memory_store import (
    FileMemoryStore,
)

store = FileMemoryStore(name="agent-memory")

agent = Agent(
    memory_manager=MemoryManager(stores=[store]),
)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent, BedrockModel, MemoryManager } from '@strands-agents/sdk'
import { FileMemoryStore } from '@strands-agents/sdk/vended-memory-stores/file-memory-store'

const store = new FileMemoryStore({ name: 'agent-memory' })

const agent = new Agent({
  model: new BedrockModel(),
  memoryManager: new MemoryManager({
    stores: [store],
  }),
})
```
(( /tab "TypeScript" ))

The agent can recall from the store right away, but nothing writes to it until you turn on a way to add memories. Pass

`add_tool_config=True``addToolConfig: true`

to the `MemoryManager` to give the agent the [`add_memory` tool](/docs/user-guide/sdk/memory/managing-memory/index.md#memory-tools), or set `extraction` on the store to turn on [automatic extraction](#extraction). You don’t need to set `writable`: it defaults to `true`, so the store accepts writes as soon as either is on.

## How It Works

The store writes one markdown file per topic under a `memory/<name>/` namespace in storage. When you add content, the first line becomes the filename (slugified, truncated to 50 characters, lowercased). A heading like `# Travel preferences` produces `travel-preferences.md`.

If a file with that slug already exists, the store appends the new facts (lines after the heading) to it rather than overwriting it. This keeps related memories grouped by topic without the agent needing to know what already exists.

When the slug has no usable characters (all punctuation, for example), the store falls back to a timestamped name like `entry-1717459200000.md`.

## Configuration

Most stores need only a `name`. To control where the files live, pass `storage`, the `Storage` backend for file operations. It defaults to `LocalFileStorage` at `./.strands/` (see [Storage Backend](#storage-backend)).

The store also accepts the [shared `MemoryStore` fields](/docs/user-guide/sdk/memory/managing-memory/index.md#stores) (`name`, `description`, `max_search_results``maxSearchResults`, `writable`, `extraction`). `extraction` is off until you set it (see [Extraction](#extraction)).

## Storage Backend

The default `LocalFileStorage` writes to `./.strands/` relative to the working directory, so a store named `agent-memory` lands at `./.strands/memory/agent-memory/`.

To persist elsewhere, swap the backend: `S3Storage` for a shared bucket, `InMemoryStorage` for ephemeral runs, or a custom backend:

(( tab "Python" ))
```python
from strands.storage import S3Storage
from strands.vended_memory_stores.file_memory_store import (
    FileMemoryStore,
)

store = FileMemoryStore(
    name="agent-memory",
    storage=S3Storage(bucket="my-memory-bucket"),
)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { FileMemoryStore } from '@strands-agents/sdk/vended-memory-stores/file-memory-store'
import { S3Storage } from '@strands-agents/sdk/storage'

const store = new FileMemoryStore({
  name: 'agent-memory',
  storage: new S3Storage('my-memory-bucket'),
})
```
(( /tab "TypeScript" ))

The store scopes everything it reads and writes to the `memory/<name>/` path prefix on the backend you pass. The prefix, not the name, is what keeps stores apart: the store lists and searches every file under it, subfolders included.

-   Give each store a distinct name without `/`. A store named `team` reads and searches the files of a store named `team/alice`, because they sit under its prefix.
-   Stores with the same name on the same backend read and write the same files, and their writes aren’t coordinated (see [Scale and Limitations](#scale-and-limitations)).
-   Don’t use an empty `name`. It scopes the store to `memory/` itself, so it reads and searches every named store’s files on that backend.

The exception is a view you have already scoped with a built-in backend’s `namespace(...)`. The store uses that view as-is and does **not** add `memory/<name>/`, so its files land directly under your prefix. Every store you hand that same view shares its files regardless of `name`, so give each store its own namespaced view.

Caution

Don’t pass a view from `namespace("")`. An empty prefix scopes nothing: the store works at the root of the backend and reads and searches every key there, including other subsystems’ data, such as sessions, stored on the same backend.

## Writing Memories

To write a memory directly, call `add`. It stores the content and returns the file’s key, relative to the store’s `memory/<name>/` namespace. The heading line drives the filename; subsequent lines are the facts:

(( tab "Python" ))
```python
from strands.vended_memory_stores.file_memory_store import (
    FileMemoryStore,
)

store = FileMemoryStore(name="agent-memory")

key = await store.add(
    "# Travel preferences\n- Prefers aisle seats"
)
print(key)  # travel-preferences.md

results = await store.search("aisle seats")
for entry in results:
    print(entry.content, entry.metadata.get("score"))
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { FileMemoryStore } from '@strands-agents/sdk/vended-memory-stores/file-memory-store'

const store = new FileMemoryStore({ name: 'agent-memory' })

const key = await store.add('# Travel preferences\n- Prefers aisle seats')
console.log(key) // travel-preferences.md

const results = await store.search('aisle seats')
for (const entry of results) {
  console.log(entry.content, entry.metadata?.score)
}
```
(( /tab "TypeScript" ))

The store serializes concurrent writes through one instance so they don’t clobber each other.

## Search

The default search ranks files by keyword token overlap: it counts how many distinct words from the query appear in each file’s name and content, and returns the top scorers. Common stop words such as “the” and “is” don’t count, and neither does the `.md` extension. A query with no usable words returns nothing.

Note

The default search matches exact words, not meanings. “Seats” matches “seats” but not “seat” or “chair.” For embedding-based semantic search over a managed vector store, use the [Bedrock Knowledge Base store](/docs/user-guide/sdk/memory/bedrock-knowledge-base/index.md).

The store’s `search` delegates to the storage backend’s pluggable [search strategy](/docs/user-guide/sdk/storage/search-strategies/index.md), so to change the ranking, give the backend a different strategy:

(( tab "Python" ))
The backend indexes each write through its strategy. `Bm25SearchStrategy` ranks with BM25 using the built-in `sqlite3` FTS5 module. It only indexes content written after you attach it, so attach it before the store’s first write:

```python
from strands.storage import LocalFileStorage
from strands.storage.search import Bm25SearchStrategy
from strands.vended_memory_stores.file_memory_store import (
    FileMemoryStore,
)

strategy = Bm25SearchStrategy()
store = FileMemoryStore(
    name="agent-memory",
    storage=LocalFileStorage(search_strategy=strategy),
)

results = await store.search("aisle seats")

await strategy.close()
```
(( /tab "Python" ))

(( tab "TypeScript" ))
`QmdSearchStrategy` ranks with BM25 using [QMD](https://github.com/tobi/qmd) (requires `@tobilu/qmd`) and re-indexes the storage directory on each search, so existing files are searchable:

```typescript
import { FileMemoryStore } from '@strands-agents/sdk/vended-memory-stores/file-memory-store'
import { LocalFileStorage } from '@strands-agents/sdk/storage'
import { QmdSearchStrategy } from '@strands-agents/sdk/storage/search/qmd'

const strategy = new QmdSearchStrategy()
const store = new FileMemoryStore({
  name: 'agent-memory',
  storage: new LocalFileStorage('./.strands/', {
    searchStrategy: strategy,
  }),
})

// ... use the store ...

await strategy.close()
```
(( /tab "TypeScript" ))

See [BM25 search](/docs/user-guide/sdk/storage/search-strategies/index.md#bm25-search) for setup details, or [write a custom strategy](/docs/user-guide/sdk/storage/search-strategies/index.md#writing-a-custom-strategy) by implementing the `SearchStrategy` interface for your own ranking. Keep a reference to the strategy so you can call `close()` on it: the store does not close it for you.

## Extraction

Enable [automatic extraction](/docs/user-guide/sdk/memory/managing-memory/index.md#automatic-extraction) to capture memories from the conversation without the agent calling a tool:

(( tab "Python" ))
```python
from strands.vended_memory_stores.file_memory_store import (
    FileMemoryStore,
)

store = FileMemoryStore(
    name="agent-memory",
    extraction=True,
)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { FileMemoryStore } from '@strands-agents/sdk/vended-memory-stores/file-memory-store'

const store = new FileMemoryStore({
  name: 'agent-memory',
  extraction: true,
})
```
(( /tab "TypeScript" ))

With `extraction=True``extraction: true`, the store creates a **key-aware extractor** that reads the existing topic filenames from storage and injects them into the extraction prompt. The model then reuses those headings when new facts belong to an existing topic, keeping related memories grouped instead of fragmenting across files.

(( tab "Python" ))
To change only the cadence or filter, pass an `ExtractionConfig` with `trigger` or `filter` and no `extractor`; the store keeps the key-aware extractor.

To steer what the extractor captures, pass an `ExtractionConfig` with a custom `ModelExtractor`:

```python
from strands.models import BedrockModel
from strands.memory.extraction.model_extractor import (
    ModelExtractor,
)
from strands.memory.extraction.types import ExtractionConfig
from strands.vended_memory_stores.file_memory_store import (
    FileMemoryStore,
)

store = FileMemoryStore(
    name="agent-memory",
    extraction=ExtractionConfig(
        extractor=ModelExtractor(
            model=BedrockModel(
                model_id="us.anthropic.claude-haiku-4-5-20251001-v1:0",
            ),
            system_prompt=(
                "Extract durable user preferences. Start each"
                " entry with a markdown heading naming its topic."
            ),
        ),
    ),
)
```

Your `system_prompt` replaces the extractor’s default guidance; the extractor still appends the JSON output format it parses. A custom extractor replaces the key-aware one, though, so the store no longer adds its heading layout or the existing topics to the prompt. The store names each file after the first line of an entry, so to keep facts grouped by topic, have your prompt start each entry with a markdown heading naming its topic.
(( /tab "Python" ))

(( tab "TypeScript" ))
Pass these fields in the extraction config to customize the built-in extractor without replacing it:

-   `model`: the model that distills facts. Defaults to the agent’s `auxModel` if set, otherwise the agent’s own model; set a cheaper one to cut cost.
-   `systemPrompt`: what counts as a durable fact. It replaces the default guidance; the store still appends its heading layout and the existing topics, and the extractor appends the JSON output format.

```typescript
import { BedrockModel } from '@strands-agents/sdk'
import { FileMemoryStore } from '@strands-agents/sdk/vended-memory-stores/file-memory-store'

const store = new FileMemoryStore({
  name: 'agent-memory',
  extraction: {
    model: new BedrockModel({
      modelId: 'us.anthropic.claude-haiku-4-5-20251001-v1:0',
    }),
    systemPrompt: 'Extract durable user preferences as discrete facts.',
  },
})
```
(( /tab "TypeScript" ))

The store implements `add` but not `add_messages``addMessages`, so extraction runs client-side: a `ModelExtractor` distills facts from the conversation and writes each through `add`.

## Scale and Limitations

The store suits working memory for a single agent or a small team: hundreds to low thousands of files. The default keyword search lists and reads every file under the store’s prefix on each search, so search cost grows with the number and size of files. Each `add` reads the target file and rewrites it, so write throughput depends on the storage backend.

Write locking is per store instance. Separate instances writing the same files, whether through the same name or the same namespaced view, in one process or several, are not coordinated, and the last write wins. To share memories between agents in one process, hand them the same store instance.

## Related

-   [Memory](/docs/user-guide/sdk/memory/overview/index.md) - the `MemoryManager` concept this store plugs into, including the tools, extraction, and injection it enables.
-   [Test memory store](/docs/user-guide/sdk/memory/test-memory-store/index.md) - the zero-setup vended `MemoryStore` backed by a local JSON file, for prototyping and tests.
-   [Bedrock Knowledge Base store](/docs/user-guide/sdk/memory/bedrock-knowledge-base/index.md) - the managed `MemoryStore` with semantic search, for production workloads.

## Related pages

- [Control what your agent remembers](/docs/user-guide/sdk/memory/managing-memory/index.md) (1 shared tag)
- [Give your agent long-term memory](/docs/user-guide/sdk/memory/overview/index.md) (1 shared tag)
- [Test Memory Store](/docs/user-guide/sdk/memory/test-memory-store/index.md) (1 shared tag)
- [Bedrock Knowledge Base Store](/docs/user-guide/sdk/memory/bedrock-knowledge-base/index.md) (1 shared tag)


## Implementation

### Python

- [harness-sdk/strands-py/src/strands/vended_memory_stores/file_memory_store/store.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/vended_memory_stores/file_memory_store/store.py)

### TypeScript

- [harness-sdk/strands-ts/src/vended-memory-stores/file-memory-store/store.ts](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/vended-memory-stores/file-memory-store/store.ts)
