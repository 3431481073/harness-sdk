Defined in: [src/models/bedrock.ts:260](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L260)

Configuration interface for AWS Bedrock model provider.

Extends BaseModelConfig with Bedrock-specific configuration options for model parameters, caching, and additional request/response fields.

## Example

```typescript
const config: BedrockModelConfig = {
  modelId: 'global.anthropic.claude-sonnet-4-6',
  maxTokens: 1024,
  temperature: 0.7,
  cacheConfig: { strategy: 'auto' }
}
```

## Extends

-   [`BaseModelConfig`](/docs/api/typescript/BaseModelConfig/index.md)

## Extended by

-   [`BedrockModelOptions`](/docs/api/typescript/BedrockModelOptions/index.md)

## Properties

### maxTokens?

```ts
optional maxTokens?: number;
```

Defined in: [src/models/bedrock.ts:266](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L266)

Maximum number of tokens to generate in the response.

#### See

[https://docs.aws.amazon.com/bedrock/latest/APIReference/API\_runtime\_InferenceConfiguration.html](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InferenceConfiguration.html)

#### Overrides

[`BaseModelConfig`](/docs/api/typescript/BaseModelConfig/index.md).[`maxTokens`](/docs/api/typescript/BaseModelConfig/index.md#maxtokens)

---

### temperature?

```ts
optional temperature?: number;
```

Defined in: [src/models/bedrock.ts:273](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L273)

Controls randomness in generation.

#### See

[https://docs.aws.amazon.com/bedrock/latest/APIReference/API\_runtime\_InferenceConfiguration.html](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InferenceConfiguration.html)

#### Overrides

[`BaseModelConfig`](/docs/api/typescript/BaseModelConfig/index.md).[`temperature`](/docs/api/typescript/BaseModelConfig/index.md#temperature)

---

### topP?

```ts
optional topP?: number;
```

Defined in: [src/models/bedrock.ts:280](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L280)

Controls diversity via nucleus sampling.

#### See

[https://docs.aws.amazon.com/bedrock/latest/APIReference/API\_runtime\_InferenceConfiguration.html](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InferenceConfiguration.html)

#### Overrides

[`BaseModelConfig`](/docs/api/typescript/BaseModelConfig/index.md).[`topP`](/docs/api/typescript/BaseModelConfig/index.md#topp)

---

### stopSequences?

```ts
optional stopSequences?: string[];
```

Defined in: [src/models/bedrock.ts:285](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L285)

Array of sequences that will stop generation when encountered.

---

### cacheConfig?

```ts
optional cacheConfig?: CacheConfig;
```

Defined in: [src/models/bedrock.ts:292](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L292)

Configuration for prompt caching.

#### See

[https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)

---

### additionalRequestFields?

```ts
optional additionalRequestFields?: JSONValue;
```

Defined in: [src/models/bedrock.ts:297](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L297)

Additional fields to include in the Bedrock request.

---

### additionalResponseFieldPaths?

```ts
optional additionalResponseFieldPaths?: string[];
```

Defined in: [src/models/bedrock.ts:302](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L302)

Additional response field paths to extract from the Bedrock response.

---

### additionalArgs?

```ts
optional additionalArgs?: JSONValue;
```

Defined in: [src/models/bedrock.ts:308](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L308)

Additional arguments to pass through to the Bedrock Converse API.

#### See

[https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/bedrock-runtime/command/ConverseStreamCommand/](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/bedrock-runtime/command/ConverseStreamCommand/)

---

### stream?

```ts
optional stream?: boolean;
```

Defined in: [src/models/bedrock.ts:318](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L318)

Whether or not to stream responses from the model.

This will use the ConverseStream API instead of the Converse API.

#### See

-   [https://docs.aws.amazon.com/bedrock/latest/APIReference/API\_runtime\_Converse.html](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html)
-   [https://docs.aws.amazon.com/bedrock/latest/APIReference/API\_runtime\_ConverseStream.html](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)

---

### includeToolResultStatus?

```ts
optional includeToolResultStatus?: boolean | "auto";
```

Defined in: [src/models/bedrock.ts:326](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L326)

Flag to include status field in tool results.

-   `true`: Always include status field
-   `false`: Never include status field
-   `'auto'`: Automatically determine based on model ID (default)

---

### guardrailConfig?

```ts
optional guardrailConfig?: BedrockGuardrailConfig;
```

Defined in: [src/models/bedrock.ts:332](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L332)

Guardrail configuration for content filtering and safety controls.

#### See

[https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)

---

### useNativeTokenCount?

```ts
optional useNativeTokenCount?: boolean;
```

Defined in: [src/models/bedrock.ts:343](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L343)

Whether to use the native Bedrock CountTokens API.

When `true`, `countTokens()` calls the Bedrock CountTokens API for accurate counts. When `false` or not set (default), skips the API call and uses the character-based heuristic estimator.

#### Default Value

```ts
false
```

---

### strictTools?

```ts
optional strictTools?: boolean;
```

Defined in: [src/models/bedrock.ts:361](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/bedrock.ts#L361)

Constrain the model to emit tool names and inputs that conform to each tool’s schema.

When `true`, every tool is sent with `strict: true` and a copy of its `inputSchema` with `additionalProperties: false` added to each object type, so a free-form `{ type: 'object' }` parameter becomes one the model can only fill with `{}`. Bedrock rejects schemas that use features outside its strict subset (recursive or external `$ref`, `minimum`/`maximum`/ `multipleOf`, `minLength`/`maxLength`, `additionalProperties` other than `false`) with a 400 at request time, and compiles each new schema on first use, which can take minutes. Incompatible with citations for Anthropic models.

#### See

-   [https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html](https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html)
-   [https://docs.aws.amazon.com/bedrock/latest/APIReference/API\_runtime\_ToolSpecification.html](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ToolSpecification.html)

#### Default Value

```ts
false
```

---

### modelId?

```ts
optional modelId?: string;
```

Defined in: [src/models/model.ts:183](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L183)

The model identifier. This typically specifies which model to use from the provider’s catalog.

#### Inherited from

[`BaseModelConfig`](/docs/api/typescript/BaseModelConfig/index.md).[`modelId`](/docs/api/typescript/BaseModelConfig/index.md#modelid)

---

### contextWindowLimit?

```ts
optional contextWindowLimit?: number;
```

Defined in: [src/models/model.ts:216](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/model.ts#L216)

Maximum context window size in tokens for the model.

This value represents the total token capacity shared between input and output. When not provided, it is automatically resolved from a built-in lookup table based on the configured model ID. An explicit value always takes precedence.

When `modelId` is changed via `updateConfig()`, this value is automatically re-resolved if it was initially auto-populated. Explicitly set values are preserved.

#### Inherited from

[`BaseModelConfig`](/docs/api/typescript/BaseModelConfig/index.md).[`contextWindowLimit`](/docs/api/typescript/BaseModelConfig/index.md#contextwindowlimit)