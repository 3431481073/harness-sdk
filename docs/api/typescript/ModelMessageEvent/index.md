Defined in: [src/hooks/events.ts:630](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L630)

Event triggered when the model completes a full message. Wraps the assembled message and stop reason after model streaming finishes.

## Extends

-   [`HookableEvent`](/docs/api/typescript/HookableEvent/index.md)

## Constructors

### Constructor

```ts
new ModelMessageEvent(data): ModelMessageEvent;
```

Defined in: [src/hooks/events.ts:637](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L637)

#### Parameters

| Parameter | Type |
| --- | --- |
| `data` | { `agent`: `LocalAgent`; `message`: [`Message`](/docs/api/typescript/Message/index.md); `stopReason`: [`StopReason`](/docs/api/typescript/StopReason/index.md); `invocationState`: [`InvocationState`](/docs/api/typescript/InvocationState/index.md); } & `HookableEventData` |

#### Returns

`ModelMessageEvent`

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
readonly type: "modelMessageEvent";
```

Defined in: [src/hooks/events.ts:631](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L631)

---

### agent

```ts
readonly agent: LocalAgent;
```

Defined in: [src/hooks/events.ts:632](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L632)

---

### message

```ts
readonly message: Message;
```

Defined in: [src/hooks/events.ts:633](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L633)

---

### stopReason

```ts
readonly stopReason: StopReason;
```

Defined in: [src/hooks/events.ts:634](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L634)

---

### invocationState

```ts
readonly invocationState: InvocationState;
```

Defined in: [src/hooks/events.ts:635](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L635)

## Methods

### toJSON()

```ts
toJSON(): Pick<ModelMessageEvent, "type" | "message" | "stopReason">;
```

Defined in: [src/hooks/events.ts:656](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L656)

Serializes for wire transport, excluding the agent reference and invocationState. Called automatically by JSON.stringify().

#### Returns

`Pick`<`ModelMessageEvent`, `"type"` | `"message"` | `"stopReason"`\>