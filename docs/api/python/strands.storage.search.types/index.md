Pluggable search strategy protocol for storage backends.

## SearchStrategy

```python
class SearchStrategy(Protocol[S])
```

Defined in: [src/strands/storage/search/types.py:14](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/types.py#L14)

A pluggable search strategy for storage backends.

Strategies encapsulate a single approach to searching stored content — keyword/lexical scan, vector similarity, full-text index, etc. Storage backends delegate their `search()` to a strategy, and consumers (memory stores, context offloaders) can override the default.

The `S` type parameter controls which storage backends the strategy is compatible with. Defaults to :class:`Storage` (any backend). Strategies that require specific backend features (e.g. `base_dir`) can narrow this to a concrete type like :class:`LocalFileStorage`.

#### index

```python
async def index(storage: S, key: str, data: bytes, **kwargs: Any) -> None
```

Defined in: [src/strands/storage/search/types.py:28](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/types.py#L28)

Index a single entry for future searches.

Consumers should call this on each write so strategies that maintain an index (FTS5, vector, etc.) can update incrementally. Strategies that search on the fly (keyword) may no-op.

`key` is relative to `storage`. A storage’s `namespace()` instances share its strategy and pass keys relative to their own prefix, so two different entries can arrive with the same key (`x.md` in two namespaces), and one entry can arrive under different keys and instances (`memory/a/x.md` written through the parent, `x.md` through `namespace("memory/a")`). A strategy that keeps its own index should key it by where the entry actually lives, such as `LocalFileStorage.base_dir` plus the key, not by the relative key or the storage instance. On a backend that does not expose that, use a separate storage with its own strategy for each index instead of sharing one strategy across namespaces.

**Arguments**:

-   `storage` - The storage backend the entry belongs to.
-   `key` - The storage key being written, relative to `storage`.
-   `data` - The raw bytes being stored.
-   `**kwargs` - Strategy-specific options for forward compatibility.

#### search

```python
async def search(storage: S, query: str,
                 **kwargs: Any) -> list[StorageSearchResult]
```

Defined in: [src/strands/storage/search/types.py:54](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/types.py#L54)

Search content in storage matching query.

**Arguments**:

-   `storage` - The storage to search over.
-   `query` - A natural-language string query.
-   `**kwargs` - Strategy-specific options for forward compatibility.

**Returns**:

Matched keys with relevance scores, ranked best-first.

## SandboxSafeSearchStrategy

```python
class SandboxSafeSearchStrategy(Protocol[S])
```

Defined in: [src/strands/storage/search/types.py:68](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/types.py#L68)

A search strategy that works inside a sandbox.

Strategies that operate purely through the :class:`Storage` API (e.g. keyword scan) are sandbox-safe. Strategies that persist state on the host filesystem (e.g. BM25 with a SQLite index) are not.

Declare `requires_host_fs: Literal[False] = False` on a strategy class to mark it as sandbox-safe.

#### index

```python
async def index(storage: S, key: str, data: bytes, **kwargs: Any) -> None
```

Defined in: [src/strands/storage/search/types.py:81](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/types.py#L81)

Index a single entry for future searches.

#### search

```python
async def search(storage: S, query: str,
                 **kwargs: Any) -> list[StorageSearchResult]
```

Defined in: [src/strands/storage/search/types.py:85](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/types.py#L85)

Search content in storage matching query.