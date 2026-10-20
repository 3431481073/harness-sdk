```ts
type AgentConfig = {
  model?:   | Model<BaseModelConfig>
     | ModelRouter
     | string;
  auxModel?:   | Model<BaseModelConfig>
     | string;
  messages?:   | Message[]
     | MessageData[];
  tools?: ToolList;
  systemPrompt?:   | SystemPrompt
     | SystemPromptData;
  appState?: Record<string, JSONValue>;
  modelState?: Record<string, JSONValue>;
  printer?: boolean;
  conversationManager?: ConversationManager;
  contextManager?: ContextManagerStrategy;
  plugins?: Plugin[];
  backgroundTasks?:   | boolean
     | BackgroundTasksConfig;
  retryStrategy?:   | RetryStrategy
     | RetryStrategy[]
     | null;
  interventions?: InterventionHandler[];
  structuredOutputSchema?: z.ZodSchema;
  sessionManager?: SessionManager;
  memoryManager?:   | MemoryManager
     | MemoryManagerConfig;
  traceAttributes?: Record<string, AttributeValue>;
  baggageAttributes?: Record<string, string>;
  name?: string;
  description?: string;
  id?: string;
  toolExecutor?:   | ConcurrentToolExecutor
     | SequentialToolExecutor
     | ToolExecutorStrategy;
  checkpointing?: boolean;
  sandbox?: Sandbox | false;
  storage?: Storage;
};
```

Defined in: [src/agent/agent.ts:159](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L159)

Configuration object for creating a new Agent.

## Properties

### model?

```ts
optional model?:
  | Model<BaseModelConfig>
  | ModelRouter
  | string;
```

Defined in: [src/agent/agent.ts:182](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L182)

The model instance or router that the agent will use to make decisions. Accepts a Model, ModelRouter, or a string representing a Bedrock model ID. When a router is provided, `agent.model` remains its default concrete model.

#### Example

```typescript
// Using a string model ID (creates BedrockModel)
const agent = new Agent({
  model: 'global.anthropic.claude-sonnet-4-6'
})

// Using an explicit BedrockModel instance with configuration
const agent = new Agent({
  model: new BedrockModel({
    modelId: 'global.anthropic.claude-sonnet-4-6',
    temperature: 0.7,
    maxTokens: 2048
  })
})
```

---

### auxModel?

```ts
optional auxModel?:
  | Model<BaseModelConfig>
  | string;
```

Defined in: [src/agent/agent.ts:192](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L192)

Model for the auxiliary side calls the SDK makes outside the main agent loop: context summarization, memory extraction, the HITL risk classifier, LLM steering, the goal judge, and the `web_fetch` analyst. Defaults to `model`, so leaving it unset changes nothing; set it (typically to a smaller, cheaper model) to move every side call off the main model at once. Each side call resolves its model as `component's own model > auxModel > model`. Accepts a Model or a string representing a Bedrock model ID, like `model`; a ModelRouter is not accepted because auxiliary calls run outside the agent loop a router attaches to.

---

### messages?

```ts
optional messages?:
  | Message[]
  | MessageData[];
```

Defined in: [src/agent/agent.ts:194](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L194)

An initial set of messages to seed the agent’s conversation history.

---

### tools?

```ts
optional tools?: ToolList;
```

Defined in: [src/agent/agent.ts:200](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L200)

An initial set of tools to register with the agent. Accepts nested arrays of tools at any depth, which will be flattened automatically. [Agent](/docs/api/typescript/Agent/index.md) instances are automatically wrapped as tools via [Agent.asTool](/docs/api/typescript/Agent/index.md#astool).

---

### systemPrompt?

```ts
optional systemPrompt?:
  | SystemPrompt
  | SystemPromptData;
```

Defined in: [src/agent/agent.ts:204](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L204)

A system prompt which guides model behavior.

---

### appState?

```ts
optional appState?: Record<string, JSONValue>;
```

Defined in: [src/agent/agent.ts:206](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L206)

Optional initial state values for the agent.

---

### modelState?

```ts
optional modelState?: Record<string, JSONValue>;
```

Defined in: [src/agent/agent.ts:211](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L211)

Optional initial model-provider state (e.g., restoring `responseId` from a prior session). Typically only set when hydrating from a snapshot.

---

### printer?

```ts
optional printer?: boolean;
```

Defined in: [src/agent/agent.ts:217](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L217)

Enable automatic printing of agent output to console. When true, prints text generation, reasoning, and tool usage as they occur. Defaults to true.

---

### conversationManager?

```ts
optional conversationManager?: ConversationManager;
```

Defined in: [src/agent/agent.ts:222](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L222)

Conversation manager for handling message history and context overflow. Defaults to SlidingWindowConversationManager with windowSize of 40.

---

### contextManager?

```ts
optional contextManager?: ContextManagerStrategy;
```

Defined in: [src/agent/agent.ts:237](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L237)

Context management strategy that controls how messages are compressed and offloaded.

-   `"auto"`: Proactive truncation of tool results + summarization at 85% utilization.
-   `"agentic"`: (Experimental) Lets the model drive context management via injected tools, with a higher truncation threshold and summarization only on overflow. This mode may change in future versions.
-   `ContextManagerConfig` object: Custom strategy pipeline and stash configuration.
-   `ContextManager` instance: Used as-is. An instance binds to one agent; construct one per `Agent`.
-   `false`: Explicitly disable context management (no compression, no offloading).

When set (except `false`), any co-provided `conversationManager` is ignored. Defaults to undefined (SlidingWindowConversationManager).

---

### plugins?

```ts
optional plugins?: Plugin[];
```

Defined in: [src/agent/agent.ts:241](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L241)

Plugins to register with the agent.

---

### backgroundTasks?

```ts
optional backgroundTasks?:
  | boolean
  | BackgroundTasksConfig;
```

Defined in: [src/agent/agent.ts:243](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L243)

Background tool execution configuration.

---

### retryStrategy?

```ts
optional retryStrategy?:
  | RetryStrategy
  | RetryStrategy[]
  | null;
```

Defined in: [src/agent/agent.ts:254](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L254)

Retry strategy (or strategies) for failed model/tool calls.

-   Omitted: a sensible default [DefaultModelRetryStrategy](/docs/api/typescript/DefaultModelRetryStrategy/index.md) with exponential backoff is used.
-   Single strategy: the given strategy is used.
-   Array of strategies: all are registered, in the given order. Passing two instances of the same concrete class logs a warning — they will collide on `plugin.name` when the plugin registry initializes.
-   `null` or `[]`: retries are explicitly disabled; failures propagate to the caller.

---

### interventions?

```ts
optional interventions?: InterventionHandler[];
```

Defined in: [src/agent/agent.ts:258](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L258)

Intervention handlers evaluated in registration order at each lifecycle point.

---

### structuredOutputSchema?

```ts
optional structuredOutputSchema?: z.ZodSchema;
```

Defined in: [src/agent/agent.ts:262](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L262)

Zod schema for structured output validation.

---

### sessionManager?

```ts
optional sessionManager?: SessionManager;
```

Defined in: [src/agent/agent.ts:266](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L266)

Session manager for saving and restoring agent sessions

---

### memoryManager?

```ts
optional memoryManager?:
  | MemoryManager
  | MemoryManagerConfig;
```

Defined in: [src/agent/agent.ts:272](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L272)

Memory manager for cross-session memory retrieval and storage. Manages one or more memory stores and exposes search/add tools. Accepts a [MemoryManager](/docs/api/typescript/MemoryManager/index.md) instance or a [MemoryManagerConfig](/docs/api/typescript/MemoryManagerConfig/index.md) object (auto-wrapped).

---

### traceAttributes?

```ts
optional traceAttributes?: Record<string, AttributeValue>;
```

Defined in: [src/agent/agent.ts:278](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L278)

Custom trace attributes to include in all spans. These attributes are merged with standard attributes in telemetry spans. Telemetry must be enabled globally via telemetry.setupTracer() for these to take effect.

---

### baggageAttributes?

```ts
optional baggageAttributes?: Record<string, string>;
```

Defined in: [src/agent/agent.ts:283](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L283)

OpenTelemetry baggage entries attached to the context for the whole invocation. Baggage propagates to downstream services via the W3C `baggage` header.

---

### name?

```ts
optional name?: string;
```

Defined in: [src/agent/agent.ts:287](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L287)

Optional name for the agent. Defaults to “Strands Agent”.

---

### description?

```ts
optional description?: string;
```

Defined in: [src/agent/agent.ts:291](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L291)

Optional description of what the agent does.

---

### id?

```ts
optional id?: string;
```

Defined in: [src/agent/agent.ts:295](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L295)

Optional unique identifier for the agent. Defaults to “agent”.

---

### toolExecutor?

```ts
optional toolExecutor?:
  | ConcurrentToolExecutor
  | SequentialToolExecutor
  | ToolExecutorStrategy;
```

Defined in: [src/agent/agent.ts:303](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L303)

Executor for tool calls from a single assistant turn.

Accepts a [ConcurrentToolExecutor](/docs/api/typescript/ConcurrentToolExecutor/index.md), a [SequentialToolExecutor](/docs/api/typescript/SequentialToolExecutor/index.md), or the corresponding [ToolExecutorStrategy](/docs/api/typescript/ToolExecutorStrategy/index.md) string shorthand. Defaults to concurrent execution.

---

### checkpointing?

```ts
optional checkpointing?: boolean;
```

Defined in: [src/agent/agent.ts:316](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L316)

**`Experimental`**

When `true`, the agent loop pauses at cycle boundaries (`afterModel`, `afterTools`) and returns `stopReason: 'checkpoint'` with a populated `checkpoint` field. Resume by passing the checkpoint back as `{ checkpointResume: { checkpoint: ... } }`.

The SDK does not capture conversation state in the checkpoint; pair with a `SessionManager` for cross-process state continuity. Defaults to `false`. See the experimental checkpoint module.

---

### sandbox?

```ts
optional sandbox?: Sandbox | false;
```

Defined in: [src/agent/agent.ts:330](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L330)

Execution environment for running commands, code, and file operations. When provided, sandbox-aware tools route operations through it.

Two distinct intents, even though they resolve to the same host execution in Node today:

-   Omitted: use the environment’s default sandbox (host execution in Node). This default is the slot reserved for richer behavior later.
-   `false`: explicitly opt out of a managed sandbox and run on the host.

Keep `false` distinct from omitting so the opt-out stays stable even if the default changes.

---

### storage?

```ts
optional storage?: Storage;
```

Defined in: [src/agent/agent.ts:340](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L340)

Default storage backend for agent subsystems.

When provided, subsystems that do not have their own explicit storage (e.g., SessionManager, ContextManager) resolve from this value. Each subsystem auto-namespaces under its own prefix to avoid key collisions. Storage specified directly on a subsystem always takes precedence over this agent-level default.