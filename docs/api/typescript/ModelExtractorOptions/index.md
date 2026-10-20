Defined in: [src/memory/extraction/model-extractor.ts:15](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/model-extractor.ts#L15)

Options for [ModelExtractor](/docs/api/typescript/ModelExtractor/index.md).

## Properties

### model?

```ts
optional model?: Model;
```

Defined in: [src/memory/extraction/model-extractor.ts:17](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/model-extractor.ts#L17)

Model used to extract facts. Resolution order: `this model > agent.auxModel > agent.model`.

---

### systemPrompt?

```ts
optional systemPrompt?: string;
```

Defined in: [src/memory/extraction/model-extractor.ts:19](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/model-extractor.ts#L19)

System prompt steering what counts as a fact. Defaults to a general fact-extraction prompt.