Defined in: [src/models/routing/router.ts:38](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/router.ts#L38)

Construction data for a [RoutingCandidate](/docs/api/typescript/RoutingCandidate/index.md).

## Properties

### model

```ts
readonly model:
  | Model<BaseModelConfig>
  | ModelRouter;
```

Defined in: [src/models/routing/router.ts:40](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/router.ts#L40)

Concrete model or opaque nested router.

---

### name?

```ts
readonly name?: string;
```

Defined in: [src/models/routing/router.ts:42](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/router.ts#L42)

Optional strategy-facing name.

---

### description?

```ts
readonly description?: string;
```

Defined in: [src/models/routing/router.ts:44](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/router.ts#L44)

Optional strategy-facing description.

---

### metadata?

```ts
readonly metadata?: Readonly<Record<string, JSONValue>>;
```

Defined in: [src/models/routing/router.ts:46](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/routing/router.ts#L46)

Optional strategy-facing evidence; must be JSON-serializable and free of secrets.