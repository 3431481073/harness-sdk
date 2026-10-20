Keyword search strategy using token-overlap scoring.

#### STOP\_WORDS

Common English words dropped from queries before matching.

#### tokenize

```python
def tokenize(text: str) -> set[str]
```

Defined in: [src/strands/storage/search/keyword.py:151](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/keyword.py#L151)

Lowercase and split text into a set of word tokens, dropping empties.

Splits on any run of non-word characters (Unicode-aware). Ensures cross-SDK compatibility with the TypeScript `/[^\p\{L}\p\{N}_]+/u` regex.

**Arguments**:

-   `text` - The text to tokenize.

**Returns**:

A set of lowercased word tokens.

#### token\_overlap\_score

```python
def token_overlap_score(query_tokens: set[str], content: str) -> int
```

Defined in: [src/strands/storage/search/keyword.py:166](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/keyword.py#L166)

Lexical relevance score: distinct query tokens present in the content.

A higher count means more of the query’s words are present. Returns 0 when there is no overlap.

**Arguments**:

-   `query_tokens` - Pre-tokenized query terms.
-   `content` - The content string to score against.

**Returns**:

Number of distinct query tokens found in the content.

## KeywordSearchStrategy

```python
class KeywordSearchStrategy()
```

Defined in: [src/strands/storage/search/keyword.py:182](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/keyword.py#L182)

Keyword search strategy using token-overlap scoring.

Tokenizes the query and each stored entry (key without its file extension + content), then scores by the number of distinct query tokens that appear. Stop words in the query (`the`, `is`, `what`, …) are ignored. Works on any storage backend with `list()` and `read()` — no index or embedding model required. Entries are read in small concurrent batches, and each result carries the bytes read during the scan. Entries whose `read()` raises `StorageError` are skipped.

This is the default search strategy for all shipped storage backends.

**Example**:

```python
from strands.storage.search import KeywordSearchStrategy

strategy = KeywordSearchStrategy()
results = await strategy.search(storage, "dark mode toggle")
```

#### index

```python
async def index(storage: Storage, key: str, data: bytes,
                **kwargs: Any) -> None
```

Defined in: [src/strands/storage/search/keyword.py:205](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/keyword.py#L205)

No-op — keyword search scans storage on the fly.

#### search

```python
async def search(storage: Storage, query: str,
                 **kwargs: Any) -> builtins.list[StorageSearchResult]
```

Defined in: [src/strands/storage/search/keyword.py:208](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/storage/search/keyword.py#L208)

Search content in storage by keyword token-overlap scoring.

**Arguments**:

-   `storage` - The storage to search over.
-   `query` - A natural-language string query.
-   `**kwargs` - Unused; accepted for protocol compatibility.

**Returns**:

Matched keys with relevance scores, ranked best-first.