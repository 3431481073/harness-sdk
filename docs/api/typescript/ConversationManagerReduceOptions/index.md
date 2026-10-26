```ts
type ConversationManagerReduceOptions = {
  agent: LocalAgent;
  model: Model;
  error?: ContextWindowOverflowError;
  invocationContext?: InvocationContext;
};
```

Defined in: [src/conversation-manager/conversation-manager.ts:28](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/conversation-manager/conversation-manager.ts#L28)

Options passed to [ConversationManager.reduce](/docs/api/typescript/ConversationManager/index.md#reduce).

When `error` is set, this is a reactive overflow recovery call — the implementation MUST remove enough history for the next model call to succeed.

When `error` is undefined, this is a proactive compression call — best-effort reduction to avoid hitting the context window limit.

## Properties

### agent

```ts
agent: LocalAgent;
```

Defined in: [src/conversation-manager/conversation-manager.ts:32](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/conversation-manager/conversation-manager.ts#L32)

The agent instance. Mutate `agent.messages` in place to reduce history.

---

### model

```ts
model: Model;
```

Defined in: [src/conversation-manager/conversation-manager.ts:39](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/conversation-manager/conversation-manager.ts#L39)

The model of the call that triggered the reduction (the routed model under a `ModelRouter`). Use it to size the reduction (`countTokens`, `estimateUtilization`); managers that reduce via a model call should resolve their own, typically `agent.auxModel`.

---

### error?

```ts
error?: ContextWindowOverflowError;
```

Defined in: [src/conversation-manager/conversation-manager.ts:51](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/conversation-manager/conversation-manager.ts#L51)

The [ContextWindowOverflowError](/docs/api/typescript/ContextWindowOverflowError/index.md) that triggered this call, or `undefined` for proactive compression calls.

When set, `reduce` MUST remove enough history for the next model call to succeed, or this error will propagate out of the agent loop uncaught.

When undefined, `reduce` is best-effort — errors are swallowed and the model call proceeds regardless.

---

### invocationContext?

```ts
readonly invocationContext?: InvocationContext;
```

Defined in: [src/conversation-manager/conversation-manager.ts:54](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/conversation-manager/conversation-manager.ts#L54)

The request this reduction runs for, if any; a nested call that joins it adds to the request’s usage, but the request’s limits don’t apply.