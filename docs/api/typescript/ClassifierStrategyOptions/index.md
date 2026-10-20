Defined in: [src/models/routing/classifier-strategy.ts:53](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/classifier-strategy.ts#L53)

Options for constructing a [ClassifierStrategy](/docs/api/typescript/ClassifierStrategy/index.md).

## Properties

### systemPrompt?

```ts
readonly optional systemPrompt?: string;
```

Defined in: [src/models/routing/classifier-strategy.ts:59](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/classifier-strategy.ts#L59)

Routing policy for the classifier, sent verbatim and never truncated. The SDK appends mandatory isolation, candidate-index, and structured-output rules that the policy cannot override. Defaults to the SDK input-complexity policy.

---

### timeoutMs?

```ts
readonly optional timeoutMs?: number;
```

Defined in: [src/models/routing/classifier-strategy.ts:65](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/classifier-strategy.ts#L65)

Maximum milliseconds to wait for classification. Defaults to 30000. The timeout bounds how long selection waits, not the classifier request itself: the in-flight call is aborted through its cancel signal, which is honored provider-dependently.

---

### maxMessageChars?

```ts
readonly optional maxMessageChars?: number;
```

Defined in: [src/models/routing/classifier-strategy.ts:67](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/classifier-strategy.ts#L67)

Maximum characters copied from the latest request into the classifier’s user message. Defaults to 4000.

---

### maxAgentInstructionsChars?

```ts
readonly optional maxAgentInstructionsChars?: number;
```

Defined in: [src/models/routing/classifier-strategy.ts:72](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/classifier-strategy.ts#L72)

Maximum characters copied from the parent agent’s system prompt text into the untrusted context. Defaults to 4000.

---

### maxCandidateChars?

```ts
readonly optional maxCandidateChars?: number;
```

Defined in: [src/models/routing/classifier-strategy.ts:78](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/classifier-strategy.ts#L78)

Maximum aggregate characters for the serialized evidence (names, descriptions, and metadata) of all candidates. Evidence is never truncated; selection throws when the budget is exceeded. Defaults to 4000.