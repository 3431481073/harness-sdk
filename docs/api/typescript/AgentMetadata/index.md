Defined in: [src/agent/agent-metadata.ts:8](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent-metadata.ts#L8)

Read-only view of agent metadata passed to a model on `stream()`.

Populated by the agent per request. Because it is rebuilt for every request, a single model instance shared across agents sees each agent’s own identity rather than a value baked in at construction.

## Properties

### sessionId?

```ts
sessionId?: string;
```

Defined in: [src/agent/agent-metadata.ts:10](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent-metadata.ts#L10)

The agent’s persisted session id; present only when a session manager is attached.