Defined in: [src/models/bedrock.ts:179](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L179)

Configuration for Bedrock guardrails.

## See

[https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)

## Properties

### guardrailIdentifier

```ts
guardrailIdentifier: string;
```

Defined in: [src/models/bedrock.ts:181](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L181)

Guardrail identifier

---

### guardrailVersion

```ts
guardrailVersion: string;
```

Defined in: [src/models/bedrock.ts:184](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L184)

Guardrail version (e.g., “1”, “DRAFT”)

---

### trace?

```ts
optional trace?: "enabled" | "disabled" | "enabled_full";
```

Defined in: [src/models/bedrock.ts:187](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L187)

Trace mode for evaluation.

#### Default Value

```ts
'enabled'
```

---

### streamProcessingMode?

```ts
optional streamProcessingMode?: "sync" | "async";
```

Defined in: [src/models/bedrock.ts:190](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L190)

Stream processing mode

---

### redaction?

```ts
optional redaction?: BedrockGuardrailRedactionConfig;
```

Defined in: [src/models/bedrock.ts:193](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L193)

Redaction behavior when content is blocked

---

### guardLatestUserMessage?

```ts
optional guardLatestUserMessage?: boolean;
```

Defined in: [src/models/bedrock.ts:207](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L207)

Only evaluate the latest user message with guardrails. When true, wraps the latest user message’s text/image content in guardContent blocks. This can improve performance and reduce costs in multi-turn conversations.

#### Remarks

The implementation finds the last user message containing text or image content (not just the last message), ensuring correct behavior during tool execution cycles where toolResult messages may follow the user’s actual input.

#### Default Value

```ts
false
```