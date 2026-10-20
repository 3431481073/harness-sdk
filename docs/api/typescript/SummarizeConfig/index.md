Defined in: [src/context-manager/methods/summarize.ts:46](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/methods/summarize.ts#L46)

**`Experimental`**

Configuration for the summarize method.

## Properties

### model?

```ts
optional model?: Model;
```

Defined in: [src/context-manager/methods/summarize.ts:48](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/methods/summarize.ts#L48)

**`Experimental`**

Model used for summarization. Resolution order: `this model > agent.auxModel > agent.model`.

---

### systemPrompt?

```ts
optional systemPrompt?: string;
```

Defined in: [src/context-manager/methods/summarize.ts:51](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/methods/summarize.ts#L51)

**`Experimental`**

Custom system prompt for the summarization model.