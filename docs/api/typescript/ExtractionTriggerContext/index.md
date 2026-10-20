Defined in: [src/memory/extraction/types.ts:93](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/types.ts#L93)

Context handed to [ExtractionTrigger.attach](/docs/api/typescript/ExtractionTrigger/index.md#attach) so a trigger can wire itself into the agent lifecycle and signal when extraction should run for its store.

## Properties

### agent

```ts
agent: LocalAgent;
```

Defined in: [src/memory/extraction/types.ts:95](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/types.ts#L95)

The agent the trigger attaches its hooks to.

---

### fire

```ts
fire: (invocationContext?) => void;
```

Defined in: [src/memory/extraction/types.ts:97](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/types.ts#L97)

Save this store’s unsaved messages now. Runs in the background and returns immediately, so calling it from a hook never blocks the agent. To await completion, see [MemoryManager.flush](/docs/api/typescript/MemoryManager/index.md#flush). Pass the firing hook event’s `invocationContext` so a client-side extractor’s model call joins that request.

#### Parameters

| Parameter | Type |
| --- | --- |
| `invocationContext?` | [`InvocationContext`](/docs/api/typescript/InvocationContext/index.md) |

#### Returns

`void`