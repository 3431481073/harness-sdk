Defined in: [src/memory/extraction/types.ts:55](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/types.ts#L55)

Context passed to [Extractor.extract](/docs/api/typescript/Extractor/index.md#extract).

Lets the manager hand an extractor a fallback model without the extractor having to be wired to the agent directly. [ModelExtractor](/docs/api/typescript/ModelExtractor/index.md) uses its own configured model when set, else [defaultModel](#defaultmodel).

## Properties

### defaultModel?

```ts
optional defaultModel?: Model;
```

Defined in: [src/memory/extraction/types.ts:57](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/types.ts#L57)

Model an extractor without its own falls back to (`agent.auxModel > agent.model`).