Defined in: [src/agent/invocation-context.ts:29](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/invocation-context.ts#L29)

What the work in an [InvocationContext](/docs/api/typescript/InvocationContext/index.md) has used: its turns and the token usage of every model call, including nested and auxiliary calls.

## Extends

-   [`Usage`](/docs/api/typescript/Usage/index.md)

## Properties

### turnsTaken

```ts
turnsTaken: number;
```

Defined in: [src/agent/invocation-context.ts:31](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/invocation-context.ts#L31)

Turns taken in this context, including its nested calls.

---

### inputTokens

```ts
inputTokens: number;
```

Defined in: [src/models/streaming.ts:497](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L497)

Number of tokens in the input (prompt).

#### Inherited from

[`Usage`](/docs/api/typescript/Usage/index.md).[`inputTokens`](/docs/api/typescript/Usage/index.md#inputtokens)

---

### outputTokens

```ts
outputTokens: number;
```

Defined in: [src/models/streaming.ts:502](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L502)

Number of tokens in the output (completion).

#### Inherited from

[`Usage`](/docs/api/typescript/Usage/index.md).[`outputTokens`](/docs/api/typescript/Usage/index.md#outputtokens)

---

### totalTokens

```ts
totalTokens: number;
```

Defined in: [src/models/streaming.ts:507](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L507)

Total number of tokens (input + output).

#### Inherited from

[`Usage`](/docs/api/typescript/Usage/index.md).[`totalTokens`](/docs/api/typescript/Usage/index.md#totaltokens)

---

### cacheReadInputTokens?

```ts
cacheReadInputTokens?: number;
```

Defined in: [src/models/streaming.ts:513](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L513)

Number of input tokens read from cache. This can reduce latency and cost.

#### Inherited from

[`Usage`](/docs/api/typescript/Usage/index.md).[`cacheReadInputTokens`](/docs/api/typescript/Usage/index.md#cachereadinputtokens)

---

### cacheWriteInputTokens?

```ts
cacheWriteInputTokens?: number;
```

Defined in: [src/models/streaming.ts:519](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L519)

Number of input tokens written to cache. These tokens can be reused in future requests.

#### Inherited from

[`Usage`](/docs/api/typescript/Usage/index.md).[`cacheWriteInputTokens`](/docs/api/typescript/Usage/index.md#cachewriteinputtokens)