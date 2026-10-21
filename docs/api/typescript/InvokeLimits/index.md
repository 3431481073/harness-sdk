Defined in: [src/types/agent.ts:183](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/types/agent.ts#L183)

Limits for the request a top-level `invoke()` / `stream()` call starts. Each is optional; omit a field for no limit on that dimension. Token limits count every model call in the request, unlike a provider’s per-call `maxTokens`, and are checked before each turn, so the last turn can go over a limit, more so when nested calls run in parallel. See [InvokeOptions.limits](/docs/api/typescript/InvokeOptions/index.md#limits) for what they cover.

## Properties

### turns?

```ts
optional turns?: number;
```

Defined in: [src/types/agent.ts:185](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/types/agent.ts#L185)

Maximum turns (one model call plus the tool calls it requests) across the request.

---

### outputTokens?

```ts
optional outputTokens?: number;
```

Defined in: [src/types/agent.ts:188](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/types/agent.ts#L188)

Maximum model-generated tokens across every model call in the request.

---

### totalTokens?

```ts
optional totalTokens?: number;
```

Defined in: [src/types/agent.ts:191](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/types/agent.ts#L191)

Maximum input + output tokens across every model call in the request; input grows each turn, so this compounds.