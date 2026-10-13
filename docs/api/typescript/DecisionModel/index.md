Defined in: [src/decisions/decision-model.ts:17](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/decision-model.ts#L17)

Abstract base for anything that can answer closed questions.

The public `ask` opens a `decision` span, validates the question map, delegates to the subclass `_ask`, records usage and the answer set as span attributes/events, and closes the span. Every implementation is traced identically.

## Extended by

-   [`LLMDecisionModel`](/docs/api/typescript/LLMDecisionModel/index.md)

## Constructors

### Constructor

```ts
new DecisionModel(): DecisionModel;
```

#### Returns

`DecisionModel`

## Methods

### ask()

```ts
ask<Q>(state, questions): Promise<DecisionResult<Q>>;
```

Defined in: [src/decisions/decision-model.ts:29](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/decision-model.ts#L29)

Ask one or more closed questions over the given state.

#### Type Parameters

| Type Parameter |
| --- |
| `Q` *extends* `Record`<`string`, [`Question`](/docs/api/typescript/Question/index.md)<`"boolean"` | readonly `string`\[\]>> |

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `state` | [`DecisionInput`](/docs/api/typescript/DecisionInput/index.md) | A plain string, a one-shot content list, or a message history. |
| `questions` | `Q` | Map of identifier → question. The returned `answers` object is keyed off this same map and statically narrowed per question. |

#### Returns

`Promise`<[`DecisionResult`](/docs/api/typescript/DecisionResult/index.md)<`Q`\>>

A [DecisionResult](/docs/api/typescript/DecisionResult/index.md) whose answers are statically narrowed from each question’s `choices`.

#### Throws

Error if `questions` is empty or contains an invalid `question`, `choices`, or `uncertainty`.

---

### \_ask()

```ts
abstract protected _ask<Q>(state, questions): Promise<DecisionResult<Q>>;
```

Defined in: [src/decisions/decision-model.ts:69](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/decision-model.ts#L69)

Implementation-specific decision logic. Must return a complete [DecisionResult](/docs/api/typescript/DecisionResult/index.md), including `metadata.latencyMs` sourced from the underlying model provider.

#### Type Parameters

| Type Parameter |
| --- |
| `Q` *extends* `Record`<`string`, [`Question`](/docs/api/typescript/Question/index.md)<`"boolean"` | readonly `string`\[\]>> |

#### Parameters

| Parameter | Type |
| --- | --- |
| `state` | [`DecisionInput`](/docs/api/typescript/DecisionInput/index.md) |
| `questions` | `Q` |

#### Returns

`Promise`<[`DecisionResult`](/docs/api/typescript/DecisionResult/index.md)<`Q`\>>