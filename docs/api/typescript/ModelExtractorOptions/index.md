Defined in: [src/memory/extraction/model-extractor.ts:18](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/model-extractor.ts#L18)

Options for [ModelExtractor](/docs/api/typescript/ModelExtractor/index.md).

## Properties

### model?

```ts
model?: Model;
```

Defined in: [src/memory/extraction/model-extractor.ts:20](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/model-extractor.ts#L20)

Model used to extract facts. Resolution order: `this model > agent.auxModel > agent.model`.

---

### systemPrompt?

```ts
systemPrompt?: string;
```

Defined in: [src/memory/extraction/model-extractor.ts:25](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/model-extractor.ts#L25)

System prompt steering what counts as a fact. Defaults to a general fact-extraction prompt. The JSON output format the extractor parses is always appended after it.