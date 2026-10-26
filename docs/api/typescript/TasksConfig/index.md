Defined in: [src/mcp/client.ts:162](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/mcp/client.ts#L162)

Configuration for MCP task execution.

MCP Tasks are experimental in both the MCP specification and this SDK. The API may change without notice in future versions.

`pollTimeout` bounds the complete automatic operation, including polling and input callbacks. `requestTimeout` limits each individual lifecycle request; progress resets it. The first limit reached ends the wait. A call’s `options.timeoutMs` overrides `pollTimeout`.

Field names and defaults match the Python SDK’s `TasksConfig` (milliseconds instead of timedeltas), except that `ttl` is a deprecated alias of `requestTimeout` and no legacy wire time-to-live is sent.

## Properties

### pollTimeout?

```ts
pollTimeout?: number;
```

Defined in: [src/mcp/client.ts:164](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/mcp/client.ts#L164)

Overall deadline in milliseconds for an automatic task operation. Defaults to 300000.

---

### requestTimeout?

```ts
requestTimeout?: number;
```

Defined in: [src/mcp/client.ts:167](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/mcp/client.ts#L167)

Timeout in milliseconds for each task lifecycle request; progress resets it. Defaults to 60000.

---

### pollInterval?

```ts
pollInterval?: number;
```

Defined in: [src/mcp/client.ts:170](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/mcp/client.ts#L170)

Polling delay in milliseconds when a legacy (2025-11-25) server omits its interval; SEP-2663 servers supply the cadence. Defaults to 1000.

---

### ~ttl?~

```ts
ttl?: number;
```

Defined in: [src/mcp/client.ts:177](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/mcp/client.ts#L177)

Timeout in milliseconds for each task lifecycle request.

#### Deprecated

Use `requestTimeout`, which takes precedence when both are set.