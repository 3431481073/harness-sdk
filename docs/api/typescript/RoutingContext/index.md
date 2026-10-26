Defined in: [src/models/routing/strategy.ts:17](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/strategy.ts#L17)

Read-only inputs supplied to a routing strategy.

## Properties

### messages

```ts
readonly messages: Message[];
```

Defined in: [src/models/routing/strategy.ts:19](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/strategy.ts#L19)

Fresh copy of the messages for this strategy ask.

---

### systemPrompt?

```ts
readonly systemPrompt?: SystemPrompt;
```

Defined in: [src/models/routing/strategy.ts:21](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/strategy.ts#L21)

Fresh copy of the system prompt for this strategy ask.

---

### toolSpecs

```ts
readonly toolSpecs: ToolSpec[];
```

Defined in: [src/models/routing/strategy.ts:23](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/strategy.ts#L23)

Fresh copy of tool specifications for this strategy ask.

---

### candidates

```ts
readonly candidates: readonly RoutingCandidate[];
```

Defined in: [src/models/routing/strategy.ts:25](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/strategy.ts#L25)

Stable configured candidate instances.

---

### invocationState

```ts
readonly invocationState: Readonly<InvocationState>;
```

Defined in: [src/models/routing/strategy.ts:27](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/strategy.ts#L27)

Live invocation state, exposed as read-only.

---

### attempts

```ts
readonly attempts: readonly RoutingAttempt[];
```

Defined in: [src/models/routing/strategy.ts:29](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/strategy.ts#L29)

Chronological attempts made during this invocation.

---

### invocationContext?

```ts
readonly invocationContext?: InvocationContext;
```

Defined in: [src/models/routing/strategy.ts:31](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/strategy.ts#L31)

The request this routing decision runs for, if any; a nested call that joins it adds to the request’s usage, but the request’s limits don’t apply.