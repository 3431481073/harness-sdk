Defined in: [src/hooks/events.ts:191](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L191)

Event triggered at the end of an agent request. Fired after all processing completes, regardless of success or error. Uses reverse callback ordering for proper cleanup semantics.

## Extends

-   [`HookableEvent`](/docs/api/typescript/HookableEvent/index.md)

## Constructors

### Constructor

```ts
new AfterInvocationEvent(data): AfterInvocationEvent;
```

Defined in: [src/hooks/events.ts:208](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L208)

#### Parameters

| Parameter | Type |
| --- | --- |
| `data` | { `agent`: `LocalAgent`; `invocationState`: [`InvocationState`](/docs/api/typescript/InvocationState/index.md); } & `HookableEventData` |

#### Returns

`AfterInvocationEvent`

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
readonly type: "afterInvocationEvent";
```

Defined in: [src/hooks/events.ts:192](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L192)

---

### agent

```ts
readonly agent: LocalAgent;
```

Defined in: [src/hooks/events.ts:193](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L193)

---

### invocationState

```ts
readonly invocationState: InvocationState;
```

Defined in: [src/hooks/events.ts:194](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L194)

---

### resume

```ts
resume: InvokeArgs = undefined;
```

Defined in: [src/hooks/events.ts:206](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L206)

Set by hook callbacks to trigger a follow-up agent invocation with new input. When set, after this event’s callbacks complete the agent re-enters its loop with these args as new input, under the same invocation lock. A fresh [BeforeInvocationEvent](/docs/api/typescript/BeforeInvocationEvent/index.md)/AfterInvocationEvent pair fires for the resumed run. Ignored if the invocation ended with an error or one of the request’s limits is reached, since a resumed run would stop again at once.

If multiple callbacks set `resume`, the last callback to run wins.

## Methods

### toJSON()

```ts
toJSON(): Pick<AfterInvocationEvent, "type">;
```

Defined in: [src/hooks/events.ts:223](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L223)

Serializes for wire transport, excluding the agent reference, invocationState, and mutable resume field. Called automatically by JSON.stringify().

#### Returns

`Pick`<`AfterInvocationEvent`, `"type"`\>