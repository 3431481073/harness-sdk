Defined in: [src/models/streaming.ts:493](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L493)

Token usage statistics for a model invocation. Tracks input, output, and total tokens, plus cache-related metrics.

## Extended by

-   [`InvocationContextUsage`](/docs/api/typescript/InvocationContextUsage/index.md)

## Properties

### inputTokens

```ts
inputTokens: number;
```

Defined in: [src/models/streaming.ts:497](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L497)

Number of tokens in the input (prompt).

---

### outputTokens

```ts
outputTokens: number;
```

Defined in: [src/models/streaming.ts:502](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L502)

Number of tokens in the output (completion).

---

### totalTokens

```ts
totalTokens: number;
```

Defined in: [src/models/streaming.ts:507](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L507)

Total number of tokens (input + output).

---

### cacheReadInputTokens?

```ts
cacheReadInputTokens?: number;
```

Defined in: [src/models/streaming.ts:513](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L513)

Number of input tokens read from cache. This can reduce latency and cost.

---

### cacheWriteInputTokens?

```ts
cacheWriteInputTokens?: number;
```

Defined in: [src/models/streaming.ts:519](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L519)

Number of input tokens written to cache. These tokens can be reused in future requests.