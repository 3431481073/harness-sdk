```ts
type MiddlewareInputHandler<TContext> = (context) => TContext | Promise<TContext>;
```

Defined in: [src/middleware/types.ts:73](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/middleware/types.ts#L73)

Handler for Input phase — transforms context before execution.

## Type Parameters

| Type Parameter |
| --- |
| `TContext` |

## Parameters

| Parameter | Type |
| --- | --- |
| `context` | `TContext` |

## Returns

`TContext` | `Promise`<`TContext`\>