Defined in: [src/models/streaming.ts:231](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L231)

Data for a metadata event.

## Properties

### type

```ts
type: "modelMetadataEvent";
```

Defined in: [src/models/streaming.ts:235](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L235)

Discriminator for metadata events.

---

### usage?

```ts
usage?: Usage;
```

Defined in: [src/models/streaming.ts:240](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L240)

Token usage information.

---

### metrics?

```ts
metrics?: Metrics;
```

Defined in: [src/models/streaming.ts:245](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L245)

Performance metrics.

---

### trace?

```ts
trace?: unknown;
```

Defined in: [src/models/streaming.ts:250](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/streaming.ts#L250)

Trace information for observability.