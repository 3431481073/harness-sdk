Defined in: [src/interrupt.ts:104](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/interrupt.ts#L104)

Error thrown when human input is required to continue agent execution. Caught by the agent loop to trigger an interrupt stop.

## Extends

-   `Error`

## Constructors

### Constructor

```ts
new InterruptError(interrupt): InterruptError;
```

Defined in: [src/interrupt.ts:110](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/interrupt.ts#L110)

#### Parameters

| Parameter | Type |
| --- | --- |
| `interrupt` | | [`Interrupt`](/docs/api/typescript/Interrupt/index.md) | [`Interrupt`](/docs/api/typescript/Interrupt/index.md)\[\] |

#### Returns

`InterruptError`

#### Overrides

`Error.constructor`

## Properties

### interrupts

```ts
readonly interrupts: Interrupt[];
```

Defined in: [src/interrupt.ts:108](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/interrupt.ts#L108)

The interrupts that caused this error.