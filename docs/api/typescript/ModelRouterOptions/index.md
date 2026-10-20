Defined in: [src/models/routing/router.ts:86](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/router.ts#L86)

Options for constructing a [ModelRouter](/docs/api/typescript/ModelRouter/index.md).

## Properties

### strategy?

```ts
readonly optional strategy?: RoutingStrategy;
```

Defined in: [src/models/routing/router.ts:88](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/router.ts#L88)

Strategy responsible for every routing decision.

---

### maxSwitches?

```ts
readonly optional maxSwitches?: number;
```

Defined in: [src/models/routing/router.ts:90](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/router.ts#L90)

Maximum successful candidate switches per invocation.