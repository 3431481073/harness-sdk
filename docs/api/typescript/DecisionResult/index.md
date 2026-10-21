Defined in: [src/decisions/types.ts:102](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L102)

Result returned by [DecisionModel.ask](/docs/api/typescript/DecisionModel/index.md#ask), keyed by the same identifiers as the input question map.

## Type Parameters

| Type Parameter | Default type | Description |
| --- | --- | --- |
| `Q` *extends* `Record`<`string`, [`Question`](/docs/api/typescript/Question/index.md)\> | `Record`<`string`, [`Question`](/docs/api/typescript/Question/index.md)\> | The question map passed to `ask`. |

## Properties

### answers

```ts
answers: { [K in string | number | symbol]: AnswerOf<Q[K]> };
```

Defined in: [src/decisions/types.ts:104](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L104)

Per-question answer, statically narrowed from each question’s `choices`.

---

### usage?

```ts
optional usage?: {
  inputTokens: number;
  outputTokens: number;
  totalTokens: number;
};
```

Defined in: [src/decisions/types.ts:106](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L106)

Aggregate token usage for the underlying model call(s), when the provider reports it.

#### inputTokens

```ts
inputTokens: number;
```

#### outputTokens

```ts
outputTokens: number;
```

#### totalTokens

```ts
totalTokens: number;
```

---

### metadata

```ts
metadata: {
  latencyMs: number;
};
```

Defined in: [src/decisions/types.ts:112](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L112)

Per-call metadata recorded by the implementation.

#### latencyMs

```ts
latencyMs: number;
```

Time spent in the underlying model call, in milliseconds.