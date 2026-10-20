Amazon S3 storage implementation.

## S3Storage

```python
class S3Storage()
```

Defined in: [src/strands/storage/s3\_storage.py:20](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/s3_storage.py#L20)

Persists bytes as objects in an Amazon S3 bucket.

The AWS SDK (boto3) is imported lazily on first use so applications that never use S3 don’t pay the import cost.

**Example**:

```python
from strands.storage import S3Storage

storage = S3Storage("my-bucket", prefix="agents/")
await storage.write("session/abc/state.json", data)
```

#### \_\_init\_\_

```python
def __init__(bucket: str,
             *,
             prefix: str = "",
             region_name: str | None = None,
             boto_session: Any = None,
             boto_client_config: Any = None,
             search_strategy: SearchStrategy[S3Storage] | None = None) -> None
```

Defined in: [src/strands/storage/s3\_storage.py:35](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/s3_storage.py#L35)

Initialize S3 storage.

**Arguments**:

-   `bucket` - S3 bucket name.
-   `prefix` - Key prefix prepended to every key (namespace within the bucket).
-   `region_name` - AWS region override.
-   `boto_session` - Pre-configured boto3 session. Cannot combine with region\_name.
-   `boto_client_config` - Botocore Config object for the S3 client.
-   `search_strategy` - Optional search strategy. When set, `write()` automatically indexes entries and `search()` delegates to the strategy instead of the default keyword scan.

**Raises**:

-   `StorageError` - If both region\_name and boto\_session are provided.

#### write

```python
async def write(key: str, data: bytes) -> None
```

Defined in: [src/strands/storage/s3\_storage.py:74](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/s3_storage.py#L74)

Store data as an S3 object.

**Arguments**:

-   `key` - Opaque string key identifying the value.
-   `data` - Raw bytes to persist.

**Raises**:

-   `StorageError` - If the write fails.

#### read

```python
async def read(key: str) -> bytes | None
```

Defined in: [src/strands/storage/s3\_storage.py:99](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/s3_storage.py#L99)

Read an S3 object.

**Arguments**:

-   `key` - The key to read.

**Returns**:

The object contents as bytes, or None if the key does not exist.

**Raises**:

-   `StorageError` - If the read fails for a reason other than a missing key.

#### delete

```python
async def delete(key: str) -> None
```

Defined in: [src/strands/storage/s3\_storage.py:126](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/s3_storage.py#L126)

Delete an S3 object. No-op if the key does not exist.

**Arguments**:

-   `key` - The key to delete.

**Raises**:

-   `StorageError` - If the delete fails.

#### list

```python
async def list(query: str = "") -> builtins.list[str]
```

Defined in: [src/strands/storage/s3\_storage.py:144](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/s3_storage.py#L144)

List S3 objects matching the given prefix.

Paginates automatically for large result sets.

**Arguments**:

-   `query` - A prefix string to filter keys. Empty string matches all.

**Returns**:

Matching keys sorted ascending, with the storage-level prefix stripped.

**Raises**:

-   `StorageError` - If the listing fails.

#### search

```python
async def search(query: str) -> builtins.list[StorageSearchResult]
```

Defined in: [src/strands/storage/s3\_storage.py:195](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/s3_storage.py#L195)

Search stored content using the configured strategy.

Delegates to the search strategy when one is set, otherwise falls back to keyword token-overlap scoring.

**Arguments**:

-   `query` - Natural-language search query.

**Returns**:

All matches with relevance scores, ranked best-first.

#### namespace

```python
def namespace(prefix: str) -> S3Storage
```

Defined in: [src/strands/storage/s3\_storage.py:214](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/s3_storage.py#L214)

Return an `S3Storage` scoped to `prefix` within this storage’s bucket and prefix.

The scoped instance shares this instance’s S3 client and search strategy. Unlike a generic `_NamespacedStorage` wrapper, its `search()` only lists and reads objects under the prefix and scores keys without it, rather than scanning the whole bucket.

The shared search strategy receives the scoped instance and keys relative to the prefix. A strategy that keeps its own index must not key it by those relative keys alone; see `SearchStrategy.index`.

**Arguments**:

-   `prefix` - Prefix to prepend to all keys.

**Returns**:

An `S3Storage` scoped to the prefix.