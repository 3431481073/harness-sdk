Defined in: [src/middleware/stages.ts:76](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/middleware/stages.ts#L76)

Context passed to model-stage middleware. All inputs to the model call are explicit — middleware can inspect and transform any of them by passing a modified context to next(). Collection fields are defensive copies; invocationState and model are shared references.

## Properties

### agent

```ts
readonly agent: LocalAgent;
```

Defined in: [src/middleware/stages.ts:78](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/middleware/stages.ts#L78)

The agent instance (escape hatch for advanced use cases).

---

### model

```ts
readonly model: Model;
```

Defined in: [src/middleware/stages.ts:80](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/middleware/stages.ts#L80)

The model this call invokes. Initialized from agent.model and replaceable per call.

---

### messages

```ts
readonly messages: readonly Message[];
```

Defined in: [src/middleware/stages.ts:82](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/middleware/stages.ts#L82)

The messages to send to the model.

---

### systemPrompt?

```ts
readonly optional systemPrompt?: SystemPrompt;
```

Defined in: [src/middleware/stages.ts:84](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/middleware/stages.ts#L84)

System prompt to guide the model’s behavior.

---

### toolSpecs

```ts
readonly toolSpecs: readonly ToolSpec[];
```

Defined in: [src/middleware/stages.ts:86](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/middleware/stages.ts#L86)

Tool specifications available to the model.

---

### toolChoice?

```ts
readonly optional toolChoice?: ToolChoice;
```

Defined in: [src/middleware/stages.ts:88](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/middleware/stages.ts#L88)

Controls how the model selects tools.

---

### invocationState

```ts
readonly invocationState: InvocationState;
```

Defined in: [src/middleware/stages.ts:90](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/middleware/stages.ts#L90)

Per-invocation state. Shared by reference — mutations are visible to hooks, tools, and AgentResult.

---

### projectedInputTokens?

```ts
readonly optional projectedInputTokens?: number;
```

Defined in: [src/middleware/stages.ts:92](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/middleware/stages.ts#L92)

Estimated input token count for this model call, or undefined if estimation failed.

---

### dynamicTrailingBlocks?

```ts
readonly optional dynamicTrailingBlocks?: number;
```

Defined in: [src/middleware/stages.ts:101](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/middleware/stages.ts#L101)

How many trailing blocks of the last user message are rebuilt on every call.

Producers add to this; a provider placing cache points keeps its own ahead of the count, since a prefix that changes every call is never read back. Counted from the end of the message so it survives a provider’s content cleaning, which only drops earlier blocks.

---

### invocationContext?

```ts
readonly optional invocationContext?: InvocationContext;
```

Defined in: [src/middleware/stages.ts:104](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/middleware/stages.ts#L104)

The request this model call belongs to, if any. See [InvokeOptions.invocationContext](/docs/api/typescript/InvokeOptions/index.md#invocationcontext).