Storage backends expose a `search()``search()` method that delegates to a pluggable search strategy. A strategy implements the

`SearchStrategy``SearchStrategy`

protocol/interface: given a storage backend and a query string, it returns a ranked list of matching keys with relevance scores. Strategies that maintain an index use `index()``index()` to update incrementally on each write; strategies that search on the fly implement it as a no-opstrategies that search on the fly omit it.

All shipped backends default to `KeywordSearchStrategy`. Pass a different strategy via the `search_strategy``searchStrategy` parameter on any built-in backend to override it.

## KeywordSearchStrategy

The default strategy shipped with both SDKs. Tokenizes the query into lowercased words, reads every key in storage, and scores each entry by the number of distinct query tokens that appear in the key and content. No index, embedding model, or external dependency required.

(( tab "Python" ))
```python
from strands.storage import LocalFileStorage
from strands.storage.search import KeywordSearchStrategy

strategy = KeywordSearchStrategy()
storage = LocalFileStorage("./my-data/")
results = await strategy.search(
    storage, "dark mode toggle"
)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { KeywordSearchStrategy } from '@strands-agents/sdk/storage/search'
import { LocalFileStorage } from '@strands-agents/sdk/storage'

const storage = new LocalFileStorage('./my-data/')
const results = await KeywordSearchStrategy.search(storage, 'dark mode toggle')
```
(( /tab "TypeScript" ))

Because it reads every entry on each search, keyword search is best suited for small-to-medium stores (up to a few thousand keys). For larger stores, use the BM25 strategy.

## BM25 search

BM25 full-text search backed by a SQLite inverted index. Scores results by term frequency, inverse document frequency, and document length normalization, producing significantly better relevance ranking than keyword overlap for large stores. It works only with `LocalFileStorage`, because it keeps its index file on the host filesystem next to the storage directory. For the same reason it can’t be used with a sandboxed `LocalFileStorage`; use keyword search there, which works with every backend.

(( tab "Python" ))
`Bm25SearchStrategy` uses the built-in `sqlite3` FTS5 module, with no external dependencies. It indexes entries at write time and never re-scans storage, so only content written after the strategy is attached is searchable (there is no backfill).

```python
from strands.storage import LocalFileStorage
from strands.storage.search import Bm25SearchStrategy

strategy = Bm25SearchStrategy()
storage = LocalFileStorage(
    "./memory/", search_strategy=strategy
)

await storage.write(
    "auth.md",
    b"OAuth2 authentication flow",
)
results = await storage.search("authentication")

await strategy.close()
```
(( /tab "Python" ))

(( tab "TypeScript" ))
`QmdSearchStrategy` uses [QMD](https://github.com/tobi/qmd) and re-indexes the storage directory on each search, so existing content is always searchable. It requires `@tobilu/qmd` as a peer dependency:

```bash
npm install @tobilu/qmd
```

```typescript
import { QmdSearchStrategy } from '@strands-agents/sdk/storage/search/qmd'
import { LocalFileStorage } from '@strands-agents/sdk/storage'

const search = new QmdSearchStrategy()
const storage = new LocalFileStorage('./memory/', {
  searchStrategy: search,
})

await storage.write('auth.md', new TextEncoder().encode('OAuth2 authentication flow'))
const results = await storage.search('authentication')

await search.close()
```
(( /tab "TypeScript" ))

The strategy persists a SQLite database alongside the storage directory. Call `close()``close()` when the strategy is no longer needed to release the database connection.

## Passing a strategy to a storage backend

Every built-in backend (`InMemoryStorage`, `LocalFileStorage`, `S3Storage`) accepts a `search_strategy``searchStrategy` parameter. When set, writes automatically call the strategy’s `index()``index()` method, and `search()``search()` delegates to the strategy instead of the default keyword scan.

(( tab "Python" ))
```python
from strands.storage import LocalFileStorage
from strands.storage.search import Bm25SearchStrategy

storage = LocalFileStorage(
    "./memory/",
    search_strategy=Bm25SearchStrategy(),
)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { QmdSearchStrategy } from '@strands-agents/sdk/storage/search/qmd'
import { LocalFileStorage } from '@strands-agents/sdk/storage'

const storage = new LocalFileStorage('./memory/', {
  searchStrategy: new QmdSearchStrategy(),
})
```
(( /tab "TypeScript" ))

## Writing a custom strategy

To rank results your own way, implement

`SearchStrategy``SearchStrategy`

yourself. Its `search()``search()` method receives the storage backend and the query, and returns

`StorageSearchResult``StorageSearchResult`

entries (key, score, and optionally the stored bytes), best match first. Read entries through the storage passed in, using `list()``list()` and `read()``read()`, so the strategy works with every backend. When the search already read an entry’s bytes, include them in the result as `data` so callers don’t have to read the entry again.

If your strategy keeps its own index, such as a vector store or a full-text index, update it in `index()``index()`. The backend calls it on every write with the key and the stored bytes.

The example below ranks entries by how often the exact query phrase appears.

(( tab "Python" ))
`SearchStrategy` is a protocol, so any class with async `index()` and `search()` methods works without subclassing. `index()` is required; a strategy that searches on the fly implements it as a no-op.

```python
from typing import Any

from strands.storage import InMemoryStorage, Storage
from strands.storage.search import StorageSearchResult


class PhraseSearchStrategy:
    """Rank entries by how often the exact query phrase appears."""

    async def index(
        self, storage: Storage, key: str, data: bytes, **kwargs: Any
    ) -> None:
        pass  # Searches on the fly, so there is nothing to index.

    async def search(
        self, storage: Storage, query: str, **kwargs: Any
    ) -> list[StorageSearchResult]:
        phrase = query.strip().lower()
        if not phrase:
            return []
        results = []
        for key in await storage.list(""):
            data = await storage.read(key)
            if data is None:
                continue
            text = data.decode("utf-8", errors="replace")
            count = text.lower().count(phrase)
            if count:
                results.append(
                    StorageSearchResult(key=key, score=count, data=data)
                )
        results.sort(key=lambda result: result.score, reverse=True)
        return results


storage = InMemoryStorage(search_strategy=PhraseSearchStrategy())
```

To pass a strategy to a sandboxed `LocalFileStorage`, declare `requires_host_fs: Literal[False] = False` on the class, as `KeywordSearchStrategy` does. The type checker rejects a sandboxed `LocalFileStorage` with a strategy that doesn’t declare it. If your strategy reads or writes the host filesystem directly, declare `requires_host_fs: Literal[True] = True` instead, as `Bm25SearchStrategy` does, and `LocalFileStorage` raises `ValueError` when a sandbox is set.
(( /tab "Python" ))

(( tab "TypeScript" ))
Any object or class with a `search()` method works. `index()` is optional; a strategy that searches on the fly omits it.

```typescript
import { InMemoryStorage } from '@strands-agents/sdk/storage'
import type { Storage } from '@strands-agents/sdk/storage'
import type {
  SearchStrategy,
  StorageSearchResult,
} from '@strands-agents/sdk/storage/search'

// Rank entries by how often the exact query phrase appears.
const phraseSearch: SearchStrategy = {
  async search(storage: Storage, query: string): Promise<StorageSearchResult[]> {
    const phrase = query.trim().toLowerCase()
    if (!phrase) return []
    const results: StorageSearchResult[] = []
    for (const key of await storage.list('')) {
      const data = await storage.read(key)
      if (!data) continue
      const text = new TextDecoder().decode(data)
      const count = text.toLowerCase().split(phrase).length - 1
      if (count > 0) results.push({ key, score: count, data })
    }
    return results.sort((a, b) => b.score - a.score)
  },
}

const storage = new InMemoryStorage({
  searchStrategy: phraseSearch,
})
```

If your strategy reads or writes the host filesystem directly instead of going through the storage, declare `readonly requiresHostFs = true` on it. `LocalFileStorage` then throws when a sandbox is set, as it does for `QmdSearchStrategy`.
(( /tab "TypeScript" ))

## Related pages

- [Storage](/docs/user-guide/sdk/storage/index.md) (1 shared tag)
- [Conversation Management](/docs/user-guide/sdk/agents/conversation-management/index.md) (1 shared tag)
- [Session Management](/docs/user-guide/sdk/bidi/session-management/index.md) (1 shared tag)
- [Persist state across sessions](/docs/user-guide/sdk/agents/session-management/index.md) (1 shared tag)
- [State Management](/docs/user-guide/sdk/agents/state/index.md) (1 shared tag)


## Implementation

### Python

- [harness-sdk/strands-py/src/strands/storage/search/types.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/types.py)
- [harness-sdk/strands-py/src/strands/storage/search/keyword.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/keyword.py)
- [harness-sdk/strands-py/src/strands/storage/search/bm25.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/bm25.py)

### TypeScript

- [harness-sdk/strands-ts/src/storage/search/types.ts](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/storage/search/types.ts)
- [harness-sdk/strands-ts/src/storage/search/keyword.ts](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/storage/search/keyword.ts)
- [harness-sdk/strands-ts/src/storage/search/qmd.ts](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/storage/search/qmd.ts)
