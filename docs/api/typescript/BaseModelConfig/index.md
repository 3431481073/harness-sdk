Defined in: [src/models/model.ts:179](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L179)

Base configuration interface for all model providers.

This interface defines the common configuration properties that all model providers should support. Provider-specific configurations should extend this interface.

## Extended by

-   [`BedrockModelConfig`](/docs/api/typescript/BedrockModelConfig/index.md)

## Properties

### modelId?

```ts
modelId?: string;
```

Defined in: [src/models/model.ts:184](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L184)

The model identifier. This typically specifies which model to use from the provider’s catalog.

---

### maxTokens?

```ts
maxTokens?: number;
```

Defined in: [src/models/model.ts:191](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L191)

Maximum number of tokens to generate in the response.

#### See

Provider-specific documentation for exact behavior

---

### temperature?

```ts
temperature?: number;
```

Defined in: [src/models/model.ts:198](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L198)

Controls randomness in generation.

#### See

Provider-specific documentation for valid range

---

### topP?

```ts
topP?: number;
```

Defined in: [src/models/model.ts:205](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L205)

Controls diversity via nucleus sampling.

#### See

Provider-specific documentation for details

---

### contextWindowLimit?

```ts
contextWindowLimit?: number;
```

Defined in: [src/models/model.ts:217](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L217)

Maximum context window size in tokens for the model.

This value represents the total token capacity shared between input and output. When not provided, it is automatically resolved from a built-in lookup table based on the configured model ID. An explicit value always takes precedence.

When `modelId` is changed via `updateConfig()`, this value is automatically re-resolved if it was initially auto-populated. Explicitly set values are preserved.