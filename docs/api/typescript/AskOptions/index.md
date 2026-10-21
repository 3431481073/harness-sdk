Defined in: [src/decisions/types.ts:19](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L19)

Per-call options for [DecisionModel.ask](/docs/api/typescript/DecisionModel/index.md#ask).

## Properties

### invocationContext?

```ts
optional invocationContext?: InvocationContext;
```

Defined in: [src/decisions/types.ts:21](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L21)

The request to add this decision’s token usage to, such as a hook event’s or tool context’s `invocationContext`; the request’s limits don’t apply to the decision.