Defined in: [src/agent/invocation-context.ts:18](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/invocation-context.ts#L18)

Handle to the request an object belongs to.

A top-level `invoke()` / `stream()` call starts a request, and the SDK attaches its handle to the objects it passes to hooks, tools, and extension points and to the call’s result. Pass it to [InvokeOptions.invocationContext](/docs/api/typescript/InvokeOptions/index.md#invocationcontext) to run a nested call in the same request, sharing its limits and usage, for example to continue a previous call’s budget.

Only the SDK can create one; its state is read-only.

## Properties

### \[invocationContextBrand\]

```ts
readonly [invocationContextBrand]: true;
```

Defined in: [src/agent/invocation-context.ts:19](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/invocation-context.ts#L19)

---

### usage

```ts
readonly usage: Readonly<InvocationContextUsage>;
```

Defined in: [src/agent/invocation-context.ts:22](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/invocation-context.ts#L22)

What the work in this context has used so far; it keeps growing while that work runs.