Defined in: [src/agent/agent.ts:413](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L413)

Orchestrates the interaction between a model, a set of tools, and MCP clients. The Agent is responsible for managing the lifecycle of tools and clients and invoking the core decision-making loop.

## Implements

-   `InvokableAgent`

## Constructors

### Constructor

```ts
new Agent(config?): Agent;
```

Defined in: [src/agent/agent.ts:560](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L560)

Creates an instance of the Agent.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `config?` | [`AgentConfig`](/docs/api/typescript/AgentConfig/index.md) | The configuration for the agent. |

#### Returns

`Agent`

## Properties

### messages

```ts
messages: Message[];
```

Defined in: [src/agent/agent.ts:420](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L420)

The conversation history of messages between user and assistant.

#### Implementation of

`LocalAgent.messages`

---

### appState

```ts
readonly appState: StateStore;
```

Defined in: [src/agent/agent.ts:425](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L425)

App state storage accessible to tools and application logic. State is not passed to the model during inference.

#### Implementation of

`LocalAgent.appState`

---

### modelState

```ts
readonly modelState: StateStore;
```

Defined in: [src/agent/agent.ts:431](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L431)

Runtime state for the model provider. Used by stateful models to persist provider-specific data (e.g., response IDs for conversation chaining) across invocations.

#### Implementation of

`LocalAgent.modelState`

---

### model

```ts
model: Model;
```

Defined in: [src/agent/agent.ts:437](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L437)

The model provider used by the agent for inference.

#### Implementation of

`LocalAgent.model`

---

### systemPrompt?

```ts
systemPrompt?: SystemPrompt;
```

Defined in: [src/agent/agent.ts:444](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L444)

The system prompt to pass to the model provider.

#### Implementation of

`LocalAgent.systemPrompt`

---

### name

```ts
readonly name: string;
```

Defined in: [src/agent/agent.ts:449](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L449)

The name of the agent.

#### Implementation of

`InvokableAgent.name`

---

### id

```ts
readonly id: string;
```

Defined in: [src/agent/agent.ts:454](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L454)

The unique identifier of the agent instance.

#### Implementation of

`LocalAgent.id`

---

### description?

```ts
readonly description?: string;
```

Defined in: [src/agent/agent.ts:459](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L459)

Optional description of what the agent does.

#### Implementation of

`InvokableAgent.description`

---

### contextManager?

```ts
readonly contextManager?: ContextManager;
```

Defined in: [src/agent/agent.ts:464](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L464)

The context manager for strategy-driven offloading, if configured.

#### Implementation of

`LocalAgent.contextManager`

---

### sessionManager?

```ts
readonly sessionManager?: SessionManager;
```

Defined in: [src/agent/agent.ts:468](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L468)

The session manager for saving and restoring agent sessions, if configured.

---

### memoryManager?

```ts
readonly memoryManager?: MemoryManager;
```

Defined in: [src/agent/agent.ts:474](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L474)

The memory manager for cross-session memory retrieval and storage, if configured.

---

### storage?

```ts
readonly storage?: Storage<string, string>;
```

Defined in: [src/agent/agent.ts:479](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L479)

Default storage backend for agent subsystems.

#### Implementation of

`LocalAgent.storage`

---

### baggageAttributes

```ts
readonly baggageAttributes: Readonly<Record<string, string>>;
```

Defined in: [src/agent/agent.ts:484](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L484)

OpenTelemetry baggage entries attached to the context for every invocation.

---

### \_interruptState

```ts
_interruptState: InterruptState;
```

Defined in: [src/agent/agent.ts:547](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L547)

Interrupt state for human-in-the-loop workflows.

## Accessors

### sandbox

#### Get Signature

```ts
get sandbox(): Sandbox;
```

Defined in: [src/agent/agent.ts:494](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L494)

Execution environment for running commands, code, and file operations.

##### Throws

DefaultNotConfiguredError if no sandbox is configured for this environment (e.g. browsers, where no host default is registered).

##### Returns

[`Sandbox`](/docs/api/typescript/Sandbox/index.md)

#### Implementation of

`LocalAgent.sandbox`

---

### auxModel

#### Get Signature

```ts
get auxModel(): Model;
```

Defined in: [src/agent/agent.ts:508](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L508)

Model for auxiliary side calls (summarization, memory extraction, classification, steering, web fetch). Resolution order: `configured auxModel > model`.

Reading always yields a resolved [Model](/docs/api/typescript/Model/index.md). Assigning accepts a Model, a Bedrock model ID string, or `undefined` to revert to following `model`. Memory extraction resolves its model when attached to the agent and keeps it; every other side call resolves it at call time.

##### Throws

Error if assigned a [ModelRouter](/docs/api/typescript/ModelRouter/index.md).

##### Returns

[`Model`](/docs/api/typescript/Model/index.md)

#### Set Signature

```ts
set auxModel(auxModel): void;
```

Defined in: [src/agent/agent.ts:512](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L512)

Model used for auxiliary side calls; defaults to `model`. See [Agent.auxModel](#auxmodel).

##### Parameters

| Parameter | Type |
| --- | --- |
| `auxModel` | | `string` | [`Model`](/docs/api/typescript/Model/index.md)<[`BaseModelConfig`](/docs/api/typescript/BaseModelConfig/index.md)\> |

##### Returns

`void`

#### Implementation of

`LocalAgent.auxModel`

---

### sessionId

#### Get Signature

```ts
get sessionId(): string;
```

Defined in: [src/agent/agent.ts:522](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L522)

A stable, unique identifier for the current conversation session.

If a SessionManager is attached, delegates to its sessionId. Otherwise, lazily generates and caches a random 8-character hex string.

##### Returns

`string`

#### Implementation of

`LocalAgent.sessionId`

---

### tools

#### Get Signature

```ts
get tools(): Tool[];
```

Defined in: [src/agent/agent.ts:976](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L976)

The tools this agent can use.

##### Returns

[`Tool`](/docs/api/typescript/Tool/index.md)\[\]

---

### toolRegistry

#### Get Signature

```ts
get toolRegistry(): ToolRegistry;
```

Defined in: [src/agent/agent.ts:983](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L983)

The tool registry for managing the agent’s tools.

##### Returns

`ToolRegistry`

#### Implementation of

`LocalAgent.toolRegistry`

---

### toolExecutor

#### Get Signature

```ts
get toolExecutor():
  | ConcurrentToolExecutor
  | SequentialToolExecutor;
```

Defined in: [src/agent/agent.ts:996](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L996)

Executor for tool calls from a single assistant turn.

Reading always yields the resolved executor instance. Assigning accepts an executor instance or a [ToolExecutorStrategy](/docs/api/typescript/ToolExecutorStrategy/index.md) string shorthand, which is resolved to the matching instance on write.

##### Throws

Error if assigned an unrecognized string shorthand.

##### Returns

| [`ConcurrentToolExecutor`](/docs/api/typescript/ConcurrentToolExecutor/index.md) | [`SequentialToolExecutor`](/docs/api/typescript/SequentialToolExecutor/index.md)

#### Set Signature

```ts
set toolExecutor(toolExecutor): void;
```

Defined in: [src/agent/agent.ts:1000](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L1000)

##### Parameters

| Parameter | Type |
| --- | --- |
| `toolExecutor` | | [`ConcurrentToolExecutor`](/docs/api/typescript/ConcurrentToolExecutor/index.md) | [`SequentialToolExecutor`](/docs/api/typescript/SequentialToolExecutor/index.md) | [`ToolExecutorStrategy`](/docs/api/typescript/ToolExecutorStrategy/index.md) |

##### Returns

`void`

---

### metrics

#### Get Signature

```ts
get metrics(): AgentMetrics;
```

Defined in: [src/agent/agent.ts:1007](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L1007)

Read-only snapshot of accumulated agent metrics (cycles, token usage, tool stats).

##### Returns

[`AgentMetrics`](/docs/api/typescript/AgentMetrics/index.md)

#### Implementation of

`LocalAgent.metrics`

---

### isInvoking

#### Get Signature

```ts
get isInvoking(): boolean;
```

Defined in: [src/agent/agent.ts:1014](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L1014)

Whether the agent is currently processing an invocation.

##### Returns

`boolean`

---

### tool

#### Get Signature

```ts
get tool(): ToolCallerProxy;
```

Defined in: [src/agent/agent.ts:1035](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L1035)

Direct tool calling accessor.

Returns a proxy where each property is a [ToolHandle](/docs/api/typescript/ToolHandle/index.md) with `.invoke()` and `.stream()` methods:

```typescript
const result = await agent.tool.calculator!.invoke({ a: 5, b: 3 })

for await (const event of agent.tool.calculator!.stream({ a: 5, b: 3 })) {
  console.log('progress:', event)
}
```

Supports underscore-to-hyphen and case-insensitive name resolution. Results are recorded in message history by default (pass `{ recordDirectToolCall: false }` to skip).

##### Returns

[`ToolCallerProxy`](/docs/api/typescript/ToolCallerProxy/index.md)

---

### cancelSignal

#### Get Signature

```ts
get cancelSignal(): AbortSignal;
```

Defined in: [src/agent/agent.ts:1045](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L1045)

The cancellation signal for the current invocation.

SDK-managed tool contexts receive this as `context.cancelSignal` for cancellable operations. Hooks can check `event.agent.cancelSignal.aborted` to detect cancellation.

##### Returns

`AbortSignal`

#### Implementation of

`LocalAgent.cancelSignal`

## Methods

### addHook()

```ts
addHook<T>(
   eventType,
   callback,
   options?
): HookCleanup;
```

Defined in: [src/agent/agent.ts:743](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L743)

Register a hook callback for a specific event type.

#### Type Parameters

| Type Parameter |
| --- |
| `T` *extends* [`HookableEvent`](/docs/api/typescript/HookableEvent/index.md) |

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `eventType` | [`HookableEventConstructor`](/docs/api/typescript/HookableEventConstructor/index.md)<`T`\> | The event class constructor to register the callback for |
| `callback` | [`HookCallback`](/docs/api/typescript/HookCallback/index.md)<`T`\> | The callback function to invoke when the event occurs |
| `options?` | [`HookCallbackOptions`](/docs/api/typescript/HookCallbackOptions/index.md) | Optional configuration including execution order |

#### Returns

`HookCleanup`

Cleanup function that removes the callback when invoked

#### Example

```typescript
const agent = new Agent({ model })

const cleanup = agent.addHook(BeforeInvocationEvent, (event) => {
  console.log('Invocation started')
})

// Later, to remove the hook:
cleanup()
```

#### Implementation of

`LocalAgent.addHook`

---

### addMiddleware()

#### Call Signature

```ts
addMiddleware<TContext, TResult, TEvent>(phase, handler): () => void;
```

Defined in: [src/agent/agent.ts:763](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L763)

Register an Input phase handler that transforms context before execution. Input handlers run before Wrap and Output handlers.

##### Type Parameters

| Type Parameter |
| --- |
| `TContext` |
| `TResult` |
| `TEvent` |

##### Parameters

| Parameter | Type |
| --- | --- |
| `phase` | `MiddlewareInputPhase`<`TContext`, `TResult`, `TEvent`\> |
| `handler` | [`MiddlewareInputHandler`](/docs/api/typescript/MiddlewareInputHandler/index.md)<`TContext`\> |

##### Returns

() => `void`

##### Example

```typescript
agent.addMiddleware(InvokeModelStage.Input, async (context) => ({
  ...context,
  systemPrompt: injectToSystemPrompt(context),
}))
```

##### Implementation of

`LocalAgent.addMiddleware`

#### Call Signature

```ts
addMiddleware<TContext, TResult, TEvent>(phase, handler): () => void;
```

Defined in: [src/agent/agent.ts:771](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L771)

Register a Wrap phase handler via the explicit `.Wrap` sub-token. Equivalent to passing the stage token directly.

##### Type Parameters

| Type Parameter |
| --- |
| `TContext` |
| `TResult` |
| `TEvent` |

##### Parameters

| Parameter | Type |
| --- | --- |
| `phase` | `MiddlewareWrapPhase`<`TContext`, `TResult`, `TEvent`\> |
| `handler` | [`MiddlewareHandler`](/docs/api/typescript/MiddlewareHandler/index.md)<`TContext`, `TResult`, `TEvent`\> |

##### Returns

() => `void`

##### Implementation of

`LocalAgent.addMiddleware`

#### Call Signature

```ts
addMiddleware<TContext, TResult, TEvent>(phase, handler): () => void;
```

Defined in: [src/agent/agent.ts:788](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L788)

Register an Output phase handler that transforms the result after execution. Output handlers see the result after Wrap handlers complete. Execution order: Input → Wrap → Output.

##### Type Parameters

| Type Parameter |
| --- |
| `TContext` |
| `TResult` |
| `TEvent` |

##### Parameters

| Parameter | Type |
| --- | --- |
| `phase` | `MiddlewareOutputPhase`<`TContext`, `TResult`, `TEvent`\> |
| `handler` | [`MiddlewareOutputHandler`](/docs/api/typescript/MiddlewareOutputHandler/index.md)<`TResult`\> |

##### Returns

() => `void`

##### Example

```typescript
agent.addMiddleware(InvokeModelStage.Output, async (result) => {
  log(`Model returned stopReason=${result.result.stopReason}`)
  return result
})
```

##### Implementation of

`LocalAgent.addMiddleware`

#### Call Signature

```ts
addMiddleware<TContext, TResult, TEvent>(stage, handler): () => void;
```

Defined in: [src/agent/agent.ts:813](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L813)

Register a middleware handler for a given stage (Wrap phase). Middleware wraps stage execution and can intercept, transform, or short-circuit operations.

##### Type Parameters

| Type Parameter |
| --- |
| `TContext` |
| `TResult` |
| `TEvent` |

##### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `stage` | [`MiddlewareStage`](/docs/api/typescript/MiddlewareStage/index.md)<`TContext`, `TResult`, `TEvent`\> | The stage token identifying the interception point |
| `handler` | [`MiddlewareHandler`](/docs/api/typescript/MiddlewareHandler/index.md)<`TContext`, `TResult`, `TEvent`\> | The middleware handler function (async generator) |

##### Returns

A cleanup function that removes the middleware when called

() => `void`

##### Example

```typescript
const cleanup = agent.addMiddleware(InvokeModelStage, async function* (context, next) {
  const start = Date.now()
  const result = yield* next(context)
  console.log(`Model call took ${Date.now() - start}ms`)
  return result
})

// Later, remove the middleware:
cleanup()
```

##### Implementation of

`LocalAgent.addMiddleware`

---

### initialize()

```ts
initialize(): Promise<void>;
```

Defined in: [src/agent/agent.ts:859](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L859)

#### Returns

`Promise`<`void`\>

---

### cancel()

```ts
cancel(): void;
```

Defined in: [src/agent/agent.ts:1077](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L1077)

Cancels the current agent invocation cooperatively.

The agent will stop at the next cancellation-safe point:

-   During model response streaming
-   Before tool execution
-   Between sequential tool executions
-   At the top of each agent loop cycle

If a tool is already executing, it will run to completion unless the tool checks `context.cancelSignal` internally.

Hook callbacks can check `event.agent.cancelSignal.aborted` to detect cancellation and adjust their behavior accordingly.

The stream/invoke call will return an AgentResult with `stopReason: 'cancelled'`. If the agent is not currently invoking, this is a no-op.

#### Returns

`void`

#### Example

```typescript
const agent = new Agent({ model, tools })

// Cancel after 5 seconds
setTimeout(() => agent.cancel(), 5000)
const result = await agent.invoke('Do something')
console.log(result.stopReason) // 'cancelled'
```

---

### invoke()

```ts
invoke(args, options?): Promise<AgentResult>;
```

Defined in: [src/agent/agent.ts:1109](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L1109)

Invokes the agent and returns the final result.

This is a convenience method that consumes the stream() method and returns only the final AgentResult. Use stream() if you need access to intermediate streaming events.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `args` | [`InvokeArgs`](/docs/api/typescript/InvokeArgs/index.md) | Arguments for invoking the agent |
| `options?` | [`InvokeOptions`](/docs/api/typescript/InvokeOptions/index.md) | Optional per-invocation options |

#### Returns

`Promise`<[`AgentResult`](/docs/api/typescript/AgentResult/index.md)\>

Promise that resolves to the final AgentResult

#### Example

```typescript
const agent = new Agent({ model, tools })
const result = await agent.invoke('What is 2 + 2?')
console.log(result.lastMessage) // Agent's response
```

#### Implementation of

`InvokableAgent.invoke`

---

### shutdown()

```ts
shutdown(): Promise<void>;
```

Defined in: [src/agent/agent.ts:1132](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L1132)

Runs the agent’s shutdown procedures at end of life. Safe to call more than once, and a no-op when there is nothing to release.

Call it directly when you own the agent’s lifecycle (e.g. draining on a shutdown signal), or bind the agent with `await using` to run it automatically on scope exit.

#### Returns

`Promise`<`void`\>

#### Example

```typescript
await using agent = await createHarness()
await agent.invoke('summarize the repo')
// agent.shutdown() runs here as the scope exits
```

---

### \[asyncDispose\]()

```ts
[asyncDispose](): Promise<void>;
```

Defined in: [src/agent/agent.ts:1140](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L1140)

Runs [Agent.shutdown](#shutdown) when the agent leaves an `await using` scope, on normal exit and on throw, so its shutdown procedures run without a manual `finally`.

#### Returns

`Promise`<`void`\>

---

### stream()

```ts
stream(args, options?): AsyncGenerator<AgentStreamEvent, AgentResult, undefined>;
```

Defined in: [src/agent/agent.ts:1174](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L1174)

Streams the agent execution, yielding events and returning the final result.

The agent loop manages the conversation flow by:

1.  Streaming model responses and yielding all events
2.  Executing tools when the model requests them
3.  Continuing the loop until the model completes without tool use

Use this method when you need access to intermediate streaming events. For simple request/response without streaming, use invoke() instead.

An explicit goal of this method is to always leave the message array in a way that the agent can be reinvoked with a user prompt after this method completes. To that end assistant messages containing tool uses are only added after tool execution succeeds with valid toolResponses

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `args` | [`InvokeArgs`](/docs/api/typescript/InvokeArgs/index.md) | Arguments for invoking the agent |
| `options?` | [`InvokeOptions`](/docs/api/typescript/InvokeOptions/index.md) | Optional per-invocation options |

#### Returns

`AsyncGenerator`<[`AgentStreamEvent`](/docs/api/typescript/AgentStreamEvent/index.md), [`AgentResult`](/docs/api/typescript/AgentResult/index.md), `undefined`\>

Async generator that yields AgentStreamEvent objects and returns AgentResult

#### Example

```typescript
const agent = new Agent({ model, tools })

for await (const event of agent.stream('Hello')) {
  console.log('Event:', event.type)
}
// Messages array is mutated in place and contains the full conversation
```

#### Implementation of

`InvokableAgent.stream`

---

### asTool()

```ts
asTool(options?): Tool;
```

Defined in: [src/agent/agent.ts:1499](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L1499)

Returns a [Tool](/docs/api/typescript/Tool/index.md) that wraps this agent, allowing it to be used as a tool by another agent.

The returned tool accepts a single `input` string parameter, invokes this agent, and returns the text response as a tool result.

**Note:** You can also pass an Agent directly in another agent’s [tools](/docs/api/typescript/AgentConfig/index.md#tools) array — it will be wrapped automatically via this method.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | [`AgentAsToolOptions`](/docs/api/typescript/AgentAsToolOptions/index.md) | Optional configuration for the tool name, description, and context preservation |

#### Returns

[`Tool`](/docs/api/typescript/Tool/index.md)

A Tool wrapping this agent

#### Example

```typescript
const researcher = new Agent({ name: 'researcher', description: 'Finds info', printer: false })

// Explicit wrapping
const writer = new Agent({ tools: [researcher.asTool()] })

// Automatic wrapping (equivalent)
const writer = new Agent({ tools: [researcher] })
```

---

### takeSnapshot()

```ts
takeSnapshot(options): Snapshot;
```

Defined in: [src/agent/agent.ts:1533](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L1533)

Captures a point-in-time snapshot of the agent’s current state.

Use snapshots to checkpoint agent state for later restoration, enabling use cases like undo/redo, branching conversations, and session persistence.

Fields are selected via a preset/include/exclude model:

1.  Start with preset fields (e.g. `'session'` captures all fields)
2.  Add any `include` fields
3.  Remove any `exclude` fields

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `options` | [`TakeSnapshotOptions`](/docs/api/typescript/TakeSnapshotOptions/index.md) | Controls which fields to capture and optional app data to store |

#### Returns

[`Snapshot`](/docs/api/typescript/Snapshot/index.md)

A [Snapshot](/docs/api/typescript/Snapshot/index.md) containing the captured agent state

#### Throws

Error if no fields would be included after applying options

#### Example

```typescript
// Capture all session-relevant state
const snapshot = agent.takeSnapshot({ preset: 'session' })

// Capture only messages and state
const partial = agent.takeSnapshot({ include: ['messages', 'state'] })

// Capture session state but exclude interrupts
const noInterrupts = agent.takeSnapshot({ preset: 'session', exclude: ['interrupts'] })

// Attach application-owned metadata
const withMeta = agent.takeSnapshot({ preset: 'session', appData: { userId: 'u-123' } })
```

#### Implementation of

`LocalAgent.takeSnapshot`

---

### loadSnapshot()

```ts
loadSnapshot(snapshot): void;
```

Defined in: [src/agent/agent.ts:1562](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts#L1562)

Restores agent state from a previously captured snapshot.

Only fields present in `snapshot.data` are restored; absent fields are left unchanged. This allows partial snapshots to update specific aspects of state without affecting others.

#### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `snapshot` | [`Snapshot`](/docs/api/typescript/Snapshot/index.md) | The snapshot to restore from |

#### Returns

`void`

#### Throws

Error if `snapshot.schemaVersion` is incompatible or scope is wrong

#### Example

```typescript
// Save and restore a conversation checkpoint
const checkpoint = agent.takeSnapshot({ preset: 'session' })

// ... agent continues processing ...

// Restore to the checkpoint
agent.loadSnapshot(checkpoint)

// Restore from a JSON-serialized snapshot (e.g. from storage)
const stored = JSON.parse(savedSnapshotJson)
agent.loadSnapshot(stored)
```

#### Implementation of

`LocalAgent.loadSnapshot`