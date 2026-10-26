Defined in: [src/hooks/events.ts:777](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L777)

Event triggered before executing tools. Fired when the model returns tool use blocks that need to be executed. Hook callbacks can set [cancel](#cancel) to prevent all tools from executing.

## Extends

-   [`HookableEvent`](/docs/api/typescript/HookableEvent/index.md)

## Implements

-   `Interruptible`

## Constructors

### Constructor

```ts
new BeforeToolsEvent(data): BeforeToolsEvent;
```

Defined in: [src/hooks/events.ts:790](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L790)

#### Parameters

| Parameter | Type |
| --- | --- |
| `data` | { `agent`: `LocalAgent`; `message`: [`Message`](/docs/api/typescript/Message/index.md); `invocationState`: [`InvocationState`](/docs/api/typescript/InvocationState/index.md); } & `HookableEventData` |

#### Returns

`BeforeToolsEvent`

#### Overrides

[`HookableEvent`](/docs/api/typescript/HookableEvent/index.md).[`constructor`](/docs/api/typescript/HookableEvent/index.md#constructor)

## Properties

### invocationContext?

```ts
readonly invocationContext?: InvocationContext;
```

Defined in: [src/hooks/events.ts:100](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L100)

The request this event belongs to (`undefined` outside one); pass it to [InvokeOptions.invocationContext](/docs/api/typescript/InvokeOptions/index.md#invocationcontext) to join it.

#### Inherited from

[`HookableEvent`](/docs/api/typescript/HookableEvent/index.md).[`invocationContext`](/docs/api/typescript/HookableEvent/index.md#invocationcontext)

---

### type

```ts
readonly type: "beforeToolsEvent";
```

Defined in: [src/hooks/events.ts:778](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L778)

---

### agent

```ts
readonly agent: LocalAgent;
```

Defined in: [src/hooks/events.ts:779](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L779)

---

### message

```ts
readonly message: Message;
```

Defined in: [src/hooks/events.ts:780](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L780)

---

### invocationState

```ts
readonly invocationState: InvocationState;
```

Defined in: [src/hooks/events.ts:781](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L781)

---

### cancel

```ts
cancel: string | boolean = false;
```

Defined in: [src/hooks/events.ts:788](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L788)

Set by hook callbacks to cancel all tool calls. When set to `true`, a default cancel message is used. When set to a string, that string is used as the tool result error message.

## Methods

### interrupt()

```ts
interrupt<T>(params): T;
```

Defined in: [src/hooks/events.ts:805](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L805)

Raises an interrupt for human-in-the-loop workflows. If a response is available (from a previous resume), returns it immediately. Otherwise, throws an InterruptError to halt agent execution.

#### Type Parameters

| Type Parameter | Default type |
| --- | --- |
| `T` | [`JSONValue`](/docs/api/typescript/JSONValue/index.md) |

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `params` | [`InterruptParams`](/docs/api/typescript/InterruptParams/index.md) | Interrupt parameters including name and optional reason |

#### Returns

`T`

The user’s response when resuming from an interrupt

#### Implementation of

`Interruptible.interrupt`

---

### toJSON()

```ts
toJSON(): Pick<BeforeToolsEvent, "type" | "message">;
```

Defined in: [src/hooks/events.ts:813](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L813)

Serializes for wire transport, excluding the agent reference, invocationState, and mutable cancel flag. Called automatically by JSON.stringify().

#### Returns

`Pick`<`BeforeToolsEvent`, `"type"` | `"message"`\>