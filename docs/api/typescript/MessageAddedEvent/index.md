Defined in: [src/hooks/events.ts:234](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L234)

Event triggered when the framework adds a message to the conversation history. Fired for user input, assistant responses, and tool-result messages added during agent execution. Does not fire for messages preloaded via `AgentConfig.messages` or messages manually pushed to `agent.messages`.

## Extends

-   [`HookableEvent`](/docs/api/typescript/HookableEvent/index.md)

## Constructors

### Constructor

```ts
new MessageAddedEvent(data): MessageAddedEvent;
```

Defined in: [src/hooks/events.ts:240](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L240)

#### Parameters

| Parameter | Type |
| --- | --- |
| `data` | { `agent`: `LocalAgent`; `message`: [`Message`](/docs/api/typescript/Message/index.md); `invocationState`: [`InvocationState`](/docs/api/typescript/InvocationState/index.md); } & `HookableEventData` |

#### Returns

`MessageAddedEvent`

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
readonly type: "messageAddedEvent";
```

Defined in: [src/hooks/events.ts:235](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L235)

---

### agent

```ts
readonly agent: LocalAgent;
```

Defined in: [src/hooks/events.ts:236](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L236)

---

### message

```ts
readonly message: Message;
```

Defined in: [src/hooks/events.ts:237](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L237)

---

### invocationState

```ts
readonly invocationState: InvocationState;
```

Defined in: [src/hooks/events.ts:238](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L238)

## Methods

### toJSON()

```ts
toJSON(): Pick<MessageAddedEvent, "type" | "message">;
```

Defined in: [src/hooks/events.ts:251](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L251)

Serializes for wire transport, excluding the agent reference and invocationState. Called automatically by JSON.stringify().

#### Returns

`Pick`<`MessageAddedEvent`, `"type"` | `"message"`\>