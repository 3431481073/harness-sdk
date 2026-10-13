Defined in: [src/context-manager/types.ts:90](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/types.ts#L90)

**`Experimental`**

Configuration for the L1 stash (offloaded content persistence).

Each agent stashes under `context/<sessionId>/scopes/agent/<agentId>/`. The prefix is dropped only when a namespaced view from a built-in backend’s `namespace()` is passed as this config’s `storage`; that view becomes the exact stash root, so agents given the same view share one stash. Deleting a session leaves a caller-scoped stash in place, and on in-memory storage each session snapshot captures and restores the whole view.

## Example

```typescript
const storage = new S3Storage('my-bucket')

// Namespaced view passed to the stash: stashes at "team/" (prefix dropped, shared).
new ContextManager({ stash: { storage: storage.namespace('team') } })

// Plain storage passed to the stash:
// stashes at "context/<sessionId>/scopes/agent/<agentId>/".
new ContextManager({ stash: { storage } })

// Namespaced view passed as agent-level storage: prefix still applies, under the view:
// stashes at "team/context/<sessionId>/scopes/agent/<agentId>/".
new Agent({ storage: storage.namespace('team'), contextManager: new ContextManager() })
```

## Properties

### storage?

```ts
optional storage?: Storage;
```

Defined in: [src/context-manager/types.ts:92](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/types.ts#L92)

**`Experimental`**

Storage backend. Defaults to the agent’s `storage`, then InMemoryStorage, when omitted.

---

### retrievalTool?

```ts
optional retrievalTool?: false;
```

Defined in: [src/context-manager/types.ts:99](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/types.ts#L99)

**`Experimental`**

Whether to register the `retrieve_context` tool for the agent. Set to `false` to keep stash persistence without exposing the retrieval tool. Defaults to `true`.