Defined in: [src/models/model.ts:223](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L223)

Options interface for configuring streaming model invocation.

## Properties

### cancelSignal?

```ts
cancelSignal?: AbortSignal;
```

Defined in: [src/models/model.ts:228](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L228)

Optional cancellation signal that a provider implementation can forward to abort an in-flight request. Support is provider-dependent.

---

### systemPrompt?

```ts
systemPrompt?: SystemPrompt;
```

Defined in: [src/models/model.ts:234](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L234)

System prompt to guide the model’s behavior. Can be a simple string or an array of content blocks for advanced caching.

---

### toolSpecs?

```ts
toolSpecs?: ToolSpec[];
```

Defined in: [src/models/model.ts:239](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L239)

Array of tool specifications that the model can use.

---

### toolChoice?

```ts
toolChoice?: ToolChoice;
```

Defined in: [src/models/model.ts:244](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L244)

Controls how the model selects tools to use.

---

### modelState?

```ts
modelState?: StateStore;
```

Defined in: [src/models/model.ts:252](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L252)

Runtime state for model providers that manage server-side conversation state. The model can read and write this state during streaming (e.g., to store a response ID for conversation chaining). Mutations via `set`/`delete` are visible to the caller after the stream completes.

---

### dynamicTrailingBlocks?

```ts
dynamicTrailingBlocks?: number;
```

Defined in: [src/models/model.ts:255](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L255)

How many trailing blocks of the last user message are rebuilt on every call.

---

### agentMetadata?

```ts
agentMetadata?: AgentMetadata;
```

Defined in: [src/models/model.ts:258](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L258)

Metadata of the invoking agent, supplied per request.

---

### structuredOutputSchema?

```ts
structuredOutputSchema?: ZodSchema;
```

Defined in: [src/models/model.ts:265](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L265)

Schema this call must produce, set by the agent on its structured output retry so the provider can choose how to enforce it. The response must then be either a call to the tool named in `toolChoice` or a final text response whose text is exactly one JSON object that validates against this schema.