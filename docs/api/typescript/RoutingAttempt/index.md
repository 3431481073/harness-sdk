Defined in: [src/models/routing/strategy.ts:9](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/strategy.ts#L9)

A candidate used during an invocation and the outcome of that attempt.

## Properties

### candidate

```ts
readonly candidate: RoutingCandidate;
```

Defined in: [src/models/routing/strategy.ts:11](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/strategy.ts#L11)

The configured candidate instance.

---

### exception?

```ts
readonly exception?: Error;
```

Defined in: [src/models/routing/strategy.ts:13](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/strategy.ts#L13)

The model or candidate-resolution error, absent when the call succeeded.