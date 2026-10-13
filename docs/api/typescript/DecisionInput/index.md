```ts
type DecisionInput =
  | string
  | ContentBlock[]
  | Message[];
```

Defined in: [src/decisions/types.ts:15](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L15)

Input state passed to a [DecisionModel](/docs/api/typescript/DecisionModel/index.md) invocation.

The subset of [InvokeArgs](/docs/api/typescript/InvokeArgs/index.md) that fits a stateless decision: a plain string question, a single-turn content list (multimodal), or a full message history.