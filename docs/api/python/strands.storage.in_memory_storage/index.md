In-memory storage implementation.

## InMemoryStorage

```python
class InMemoryStorage()
```

Defined in: [src/strands/storage/in\_memory\_storage.py:19](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/in_memory_storage.py#L19)

Map-backed storage for testing and short-lived processes.

Content does not survive process restarts. The store is unbounded — consumers manage eviction themselves.

**Example**:

```python
from strands.storage import InMemoryStorage

storage = InMemoryStorage()
await storage.write("sessions/abc/state.json", b'\{"messages": []}')
data = await storage.read("sessions/abc/state.json")
```

#### \_\_init\_\_

```python
def __init__(
        *,
        search_strategy: SearchStrategy[InMemoryStorage] | None = None
) -> None
```

Defined in: [src/strands/storage/in\_memory\_storage.py:37](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/in_memory_storage.py#L37)

Initialize an empty in-memory store.

**Arguments**:

-   `search_strategy` - Optional search strategy. When set, `write()` automatically indexes entries and `search()` delegates to the strategy instead of the default keyword scan.

#### write

```python
async def write(key: str, data: bytes) -> None
```

Defined in: [src/strands/storage/in\_memory\_storage.py:51](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/in_memory_storage.py#L51)

Store data under key, overwriting any existing value.

**Arguments**:

-   `key` - Opaque string key identifying the value.
-   `data` - Raw bytes to persist.

**Raises**:

-   `StorageError` - If the key is invalid.

#### read

```python
async def read(key: str) -> bytes | None
```

Defined in: [src/strands/storage/in\_memory\_storage.py:71](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/in_memory_storage.py#L71)

Retrieve the bytes previously stored under key.

**Arguments**:

-   `key` - The key to read.

**Returns**:

The stored bytes, or None if no value exists for key.

**Raises**:

-   `StorageError` - If the key is invalid.

#### delete

```python
async def delete(key: str) -> None
```

Defined in: [src/strands/storage/in\_memory\_storage.py:88](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/in_memory_storage.py#L88)

Delete the value stored under key. A no-op if the key does not exist.

**Arguments**:

-   `key` - The key to delete.

**Raises**:

-   `StorageError` - If the key is invalid.

#### list

```python
async def list(query: str = "") -> builtins.list[str]
```

Defined in: [src/strands/storage/in\_memory\_storage.py:101](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/in_memory_storage.py#L101)

List keys matching the given prefix.

**Arguments**:

-   `query` - A prefix string to filter keys. Empty string matches all.

**Returns**:

Matching keys sorted ascending.

**Raises**:

-   `StorageError` - If the prefix is invalid.

#### search

```python
async def search(query: str) -> builtins.list[StorageSearchResult]
```

Defined in: [src/strands/storage/in\_memory\_storage.py:118](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/in_memory_storage.py#L118)

Search stored content using the configured strategy.

Delegates to the search strategy when one is set, otherwise falls back to keyword token-overlap scoring.

**Arguments**:

-   `query` - Natural-language search query.

**Returns**:

All matches with relevance scores, ranked best-first.

#### namespace

```python
def namespace(prefix: str) -> InMemoryStorage
```

Defined in: [src/strands/storage/in\_memory\_storage.py:134](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/in_memory_storage.py#L134)

Return an `InMemoryStorage` scoped to `prefix`.

The scoped instance shares this instance’s entries and search strategy. Unlike a generic `_NamespacedStorage` wrapper, its `search()` only sees entries under the prefix and scores keys without it, so a query never matches every entry just because it contains a word from the prefix.

The shared search strategy receives the scoped instance and keys relative to the prefix. A strategy that keeps its own index must not key it by those relative keys alone; see `SearchStrategy.index`.

**Arguments**:

-   `prefix` - Prefix to prepend to all keys.

**Returns**:

An `InMemoryStorage` scoped to the prefix.

#### clear

```python
def clear() -> None
```

Defined in: [src/strands/storage/in\_memory\_storage.py:161](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/in_memory_storage.py#L161)

Remove all entries visible to this instance.

That is every entry under its namespace, or every entry when not namespaced.