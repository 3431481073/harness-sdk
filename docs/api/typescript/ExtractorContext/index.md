Defined in: [src/memory/extraction/types.ts:56](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/types.ts#L56)

Context passed to [Extractor.extract](/docs/api/typescript/Extractor/index.md#extract).

Lets the manager hand an extractor a fallback model without the extractor having to be wired to the agent directly. [ModelExtractor](/docs/api/typescript/ModelExtractor/index.md) uses its own configured model when set, else [defaultModel](#defaultmodel).

## Properties

### defaultModel?

```ts
optional defaultModel?: Model;
```

Defined in: [src/memory/extraction/types.ts:58](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/types.ts#L58)

Model an extractor without its own falls back to (`agent.auxModel > agent.model`).

---

### invocationContext?

```ts
readonly optional invocationContext?: InvocationContext;
```

Defined in: [src/memory/extraction/types.ts:67](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/types.ts#L67)

The request this extraction runs for, if any; a nested call that joins it adds to the request’s usage, but the request’s limits don’t apply.