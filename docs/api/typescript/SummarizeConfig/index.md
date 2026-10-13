Defined in: [src/context-manager/methods/summarize.ts:44](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/methods/summarize.ts#L44)

**`Experimental`**

Configuration for the summarize method.

## Properties

### model?

```ts
optional model?: Model;
```

Defined in: [src/context-manager/methods/summarize.ts:46](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/methods/summarize.ts#L46)

**`Experimental`**

Model used for summarization. Resolution order: `this model > agent.auxModel > agent.model`.

---

### systemPrompt?

```ts
optional systemPrompt?: string;
```

Defined in: [src/context-manager/methods/summarize.ts:49](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/methods/summarize.ts#L49)

**`Experimental`**

Custom system prompt for the summarization model.