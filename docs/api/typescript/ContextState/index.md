Defined in: [src/context-manager/types.ts:43](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/types.ts#L43)

**`Experimental`**

State passed to strategies during apply().

## Properties

### messages

```ts
messages: Message[];
```

Defined in: [src/context-manager/types.ts:45](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/types.ts#L45)

**`Experimental`**

The agent’s current message array (the context window). Strategies mutate this in place.

---

### agent

```ts
agent: LocalAgent;
```

Defined in: [src/context-manager/types.ts:48](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/types.ts#L48)

**`Experimental`**

The agent instance.

---

### utilization

```ts
utilization: number;
```

Defined in: [src/context-manager/types.ts:51](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/types.ts#L51)

**`Experimental`**

Current context utilization ratio (0-1+). Above 1.0 means overflow.

---

### overflow?

```ts
overflow?: boolean;
```

Defined in: [src/context-manager/types.ts:58](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/types.ts#L58)

**`Experimental`**

Set when running in response to a `ContextWindowOverflowError`. Strategies should bypass utilization gates when true — the provider already rejected the request, so the estimate is not trustworthy.

---

### stash?

```ts
stash?: Stash;
```

Defined in: [src/context-manager/types.ts:61](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/types.ts#L61)

**`Experimental`**

L1 stash for persisting offloaded content. Present when storage is configured.

---

### invocationContext?

```ts
readonly invocationContext?: InvocationContext;
```

Defined in: [src/context-manager/types.ts:64](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/types.ts#L64)

**`Experimental`**

The request this reduction runs for, if any; a nested call that joins it adds to the request’s usage, but the request’s limits don’t apply.