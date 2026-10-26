Defined in: [src/context-manager/types.ts:111](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/types.ts#L111)

**`Experimental`**

Full configuration for a ContextManager instance.

## Properties

### strategies?

```ts
strategies?: (
  | ContextStrategy
  | "proactiveSummarization"
  | "largeToolOffloading"
  | "overflowProtection"
  | "staleToolCleanup")[];
```

Defined in: [src/context-manager/types.ts:121](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/types.ts#L121)

**`Experimental`**

Strategies for context reduction. Applied as an ordered pipeline: each strategy sees the output of the previous. Order determines priority — if two strategies target the same content, the first one to shrink it below the next strategy’s threshold wins. When omitted, uses the default pipeline.

Accepts raw `ContextStrategy` objects, preset name strings (e.g. `'largeToolOffloading'`), or a mix of both. Preset strings are resolved to their default strategy configurations.

---

### stash?

```ts
stash?: boolean | StashConfig;
```

Defined in: [src/context-manager/types.ts:131](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/types.ts#L131)

**`Experimental`**

L1 stash configuration. The stash persists offloaded content so the agent can retrieve it on demand via the `retrieve_context` tool.

-   Omit or `true` → stash enabled with InMemoryStorage (default)
-   `{ storage }` → stash enabled with the given backend
-   `false` → stash disabled (no persistence, no retrieval tool)