Defined in: [src/models/bedrock.ts:212](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L212)

Configuration for Bedrock guardrails.

## See

[https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)

## Properties

### guardrailIdentifier

```ts
guardrailIdentifier: string;
```

Defined in: [src/models/bedrock.ts:214](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L214)

Guardrail identifier

---

### guardrailVersion

```ts
guardrailVersion: string;
```

Defined in: [src/models/bedrock.ts:217](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L217)

Guardrail version (e.g., “1”, “DRAFT”)

---

### trace?

```ts
trace?: "enabled" | "disabled" | "enabled_full";
```

Defined in: [src/models/bedrock.ts:220](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L220)

Trace mode for evaluation.

#### Default Value

```ts
'enabled'
```

---

### streamProcessingMode?

```ts
streamProcessingMode?: "sync" | "async";
```

Defined in: [src/models/bedrock.ts:223](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L223)

Stream processing mode

---

### redaction?

```ts
redaction?: BedrockGuardrailRedactionConfig;
```

Defined in: [src/models/bedrock.ts:226](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L226)

Redaction behavior when content is blocked

---

### guardLatestUserMessage?

```ts
guardLatestUserMessage?: boolean;
```

Defined in: [src/models/bedrock.ts:240](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L240)

Only evaluate the latest user message with guardrails. When true, wraps the latest user message’s text/image content in guardContent blocks. This can improve performance and reduce costs in multi-turn conversations.

#### Remarks

The implementation finds the last user message containing text or image content (not just the last message), ensuring correct behavior during tool execution cycles where toolResult messages may follow the user’s actual input.

#### Default Value

```ts
false
```