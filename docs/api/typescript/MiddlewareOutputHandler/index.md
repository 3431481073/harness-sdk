```ts
type MiddlewareOutputHandler<TResult> = (result) => TResult | Promise<TResult>;
```

Defined in: [src/middleware/types.ts:76](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/middleware/types.ts#L76)

Handler for Output phase — transforms result after execution.

## Type Parameters

| Type Parameter |
| --- |
| `TResult` |

## Parameters

| Parameter | Type |
| --- | --- |
| `result` | `TResult` |

## Returns

`TResult` | `Promise`<`TResult`\>