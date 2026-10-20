Defined in: [src/hooks/events.ts:137](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L137)

Event triggered when an agent has finished initialization. Fired after the agent has been fully constructed and all built-in components have been initialized.

## Extends

-   [`HookableEvent`](/docs/api/typescript/HookableEvent/index.md)

## Constructors

### Constructor

```ts
new InitializedEvent(data): InitializedEvent;
```

Defined in: [src/hooks/events.ts:141](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L141)

#### Parameters

| Parameter | Type |
| --- | --- |
| `data` | { `agent`: `LocalAgent`; } |
| `data.agent` | `LocalAgent` |

#### Returns

`InitializedEvent`

#### Overrides

[`HookableEvent`](/docs/api/typescript/HookableEvent/index.md).[`constructor`](/docs/api/typescript/HookableEvent/index.md#constructor)

## Properties

### invocationContext?

```ts
readonly optional invocationContext?: InvocationContext;
```

Defined in: [src/hooks/events.ts:100](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L100)

The request this event belongs to (`undefined` outside one); pass it to [InvokeOptions.invocationContext](/docs/api/typescript/InvokeOptions/index.md#invocationcontext) to join it.

#### Inherited from

[`HookableEvent`](/docs/api/typescript/HookableEvent/index.md).[`invocationContext`](/docs/api/typescript/HookableEvent/index.md#invocationcontext)

---

### type

```ts
readonly type: "initializedEvent";
```

Defined in: [src/hooks/events.ts:138](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L138)

---

### agent

```ts
readonly agent: LocalAgent;
```

Defined in: [src/hooks/events.ts:139](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L139)

## Methods

### toJSON()

```ts
toJSON(): Pick<InitializedEvent, "type">;
```

Defined in: [src/hooks/events.ts:150](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L150)

Serializes for wire transport, excluding the agent reference. Called automatically by JSON.stringify().

#### Returns

`Pick`<`InitializedEvent`, `"type"`\>