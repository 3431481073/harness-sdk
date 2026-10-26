Defined in: [src/decisions/llm-decision-model.ts:27](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/llm-decision-model.ts#L27)

Options for constructing an [LLMDecisionModel](/docs/api/typescript/LLMDecisionModel/index.md).

## Properties

### model?

```ts
readonly model?: Model;
```

Defined in: [src/decisions/llm-decision-model.ts:32](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/llm-decision-model.ts#L32)

Underlying vended model; must honor forced `toolChoice` so the structured-output tool is the only possible response. Defaults to a zero-config [BedrockModel](/docs/api/typescript/BedrockModel/index.md).

---

### systemPrompt?

```ts
readonly systemPrompt?: string;
```

Defined in: [src/decisions/llm-decision-model.ts:38](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/llm-decision-model.ts#L38)

System prompt used to frame the decision for the model. The SDK appends mandatory output and prompt-injection rules that the prompt cannot override. Defaults to a generic decision framing.