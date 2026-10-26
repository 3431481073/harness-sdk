Defined in: [src/memory/extraction/types.ts:42](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/types.ts#L42)

A discrete entry produced by an [Extractor](/docs/api/typescript/Extractor/index.md), ready to be written to a store via its `add`.

## Properties

### content

```ts
content: string;
```

Defined in: [src/memory/extraction/types.ts:44](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/types.ts#L44)

The textual content of the entry.

---

### metadata?

```ts
metadata?: Record<string, JSONValue>;
```

Defined in: [src/memory/extraction/types.ts:46](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/types.ts#L46)

Optional metadata to associate with the entry.