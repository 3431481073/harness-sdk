Defined in: [src/context-manager/methods/summarize.ts:55](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/methods/summarize.ts#L55)

**`Experimental`**

Configuration for the summarize method.

## Properties

### model?

```ts
model?: Model;
```

Defined in: [src/context-manager/methods/summarize.ts:57](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/methods/summarize.ts#L57)

**`Experimental`**

Model used for summarization. Resolution order: `this model > agent.auxModel > agent.model`.

---

### systemPrompt?

```ts
systemPrompt?: string;
```

Defined in: [src/context-manager/methods/summarize.ts:60](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/methods/summarize.ts#L60)

**`Experimental`**

Custom system prompt for the summarization model.