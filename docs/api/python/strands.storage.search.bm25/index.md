BM25 full-text search strategy powered by SQLite FTS5.

Maintains a SQLite-backed inverted index over storage contents and uses BM25 scoring for relevance ranking. Accounts for term frequency, inverse document frequency, and document length normalization.

Indexes entries at write time via :meth:`Bm25SearchStrategy.index` so searches do not need to re-read storage contents. Requires a `base_dir` property on the storage instance only to locate the SQLite database file on the host filesystem.

Zero external dependencies — uses Python’s stdlib `sqlite3` module which ships FTS5 support on all modern platforms.

## Bm25SearchStrategyConfig

```python
@dataclass
class Bm25SearchStrategyConfig()
```

Defined in: [src/strands/storage/search/bm25.py:52](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/bm25.py#L52)

Configuration for :class:`Bm25SearchStrategy`.

**Attributes**:

-   `db_path` - Path to the SQLite database file for the FTS5 index. Defaults to `.<dir>-fts5.sqlite` alongside the storage directory, which gives each directory its own index. An explicit `db_path` holds one directory’s index, so a strategy with `db_path` set raises `ValueError` if it is then used with a second directory (for example a second `FileMemoryStore` on the same storage).

## Bm25SearchStrategy

```python
class Bm25SearchStrategy()
```

Defined in: [src/strands/storage/search/bm25.py:67](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/bm25.py#L67)

BM25 full-text search strategy powered by SQLite FTS5.

Maintains a SQLite-backed inverted index over the storage contents and uses BM25 scoring for relevance ranking. Accounts for term frequency, inverse document frequency, and document length normalization.

Indexes entries at write time via :meth:`index` — consumers call `strategy.index(storage, key, data)` on each write, and `search()` queries the pre-built index. Only entries passed through `index()` are searchable; pre-existing storage contents are not backfilled automatically.

The FTS5 index is persisted on the host filesystem via the storage’s `base_dir` and is not sandbox-aware.

Keeps one index per storage directory, so one instance can serve several namespaced storages, such as multiple `FileMemoryStore` instances on the same `LocalFileStorage`, and :meth:`close` closes all of them.

**Example**:

```python
from strands.storage import LocalFileStorage
from strands.storage.search.bm25 import Bm25SearchStrategy

storage = LocalFileStorage("./memory/")
strategy = Bm25SearchStrategy()

await strategy.index(storage, "auth.md", b"OAuth2 authentication flow")
results = await strategy.search(storage, "authentication flow")
await strategy.close()
```

#### \_\_init\_\_

```python
def __init__(config: Bm25SearchStrategyConfig | None = None) -> None
```

Defined in: [src/strands/storage/search/bm25.py:102](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/bm25.py#L102)

Initialize the BM25 search strategy.

**Arguments**:

-   `config` - Optional configuration. See :class:`Bm25SearchStrategyConfig`.

#### index

```python
async def index(storage: LocalFileStorage, key: str, data: bytes,
                **kwargs: Any) -> None
```

Defined in: [src/strands/storage/search/bm25.py:114](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/bm25.py#L114)

Index a single entry for future searches.

Skips hidden files (keys whose final segment starts with ’.’). Uses content hashing to avoid redundant re-indexing when the data has not changed.

**Arguments**:

-   `storage` - The storage backend (used to locate the index db).
-   `key` - The storage key being written.
-   `data` - The raw bytes being stored.
-   `**kwargs` - Unused; accepted for protocol compatibility.

#### search

```python
async def search(storage: LocalFileStorage, query: str,
                 **kwargs: Any) -> list[StorageSearchResult]
```

Defined in: [src/strands/storage/search/bm25.py:137](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/bm25.py#L137)

Search the index using BM25 full-text search.

**Arguments**:

-   `storage` - The storage backend (used to locate the index db).
-   `query` - Natural-language search query.
-   `**kwargs` - Unused; accepted for protocol compatibility.

**Returns**:

Matched keys with BM25 relevance scores, ranked best-first.

**Raises**:

-   `RuntimeError` - If the SQLite build lacks FTS5 support.

#### close

```python
async def close() -> None
```

Defined in: [src/strands/storage/search/bm25.py:159](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/bm25.py#L159)

Close every SQLite connection this strategy has opened and release resources.