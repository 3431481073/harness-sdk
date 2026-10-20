Defined in: [src/hooks/events.ts:753](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L753)

Event emitted when an interrupt is raised during agent execution. The `interrupt.source` field discriminates between tool-callback and hook-callback origins. One event fires per unanswered interrupt at the moment the agent stops to wait for responses.

## Extends

-   [`HookableEvent`](/docs/api/typescript/HookableEvent/index.md)

## Constructors

### Constructor

```ts
new InterruptEvent(data): InterruptEvent;
```

Defined in: [src/hooks/events.ts:759](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L759)

#### Parameters

| Parameter | Type |
| --- | --- |
| `data` | { `agent`: `LocalAgent`; `interrupt`: [`Interrupt`](/docs/api/typescript/Interrupt/index.md); `invocationState`: [`InvocationState`](/docs/api/typescript/InvocationState/index.md); } & `HookableEventData` |

#### Returns

`InterruptEvent`

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
readonly type: "interruptEvent";
```

Defined in: [src/hooks/events.ts:754](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L754)

---

### agent

```ts
readonly agent: LocalAgent;
```

Defined in: [src/hooks/events.ts:755](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L755)

---

### interrupt

```ts
readonly interrupt: Interrupt;
```

Defined in: [src/hooks/events.ts:756](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L756)

---

### invocationState

```ts
readonly invocationState: InvocationState;
```

Defined in: [src/hooks/events.ts:757](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L757)

## Methods

### toJSON()

```ts
toJSON(): Pick<InterruptEvent, "type"> & {
  interrupt: {
     id: string;
     name: string;
     reason?: JSONValue;
     response?: JSONValue;
     source: InterruptSource;
  };
};
```

Defined in: [src/hooks/events.ts:767](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L767)

Serializes for wire transport, excluding agent and invocationState.

#### Returns

`Pick`<`InterruptEvent`, `"type"`\> & { `interrupt`: { `id`: `string`; `name`: `string`; `reason?`: [`JSONValue`](/docs/api/typescript/JSONValue/index.md); `response?`: [`JSONValue`](/docs/api/typescript/JSONValue/index.md); `source`: [`InterruptSource`](/docs/api/typescript/InterruptSource/index.md); }; }