Defined in: [src/hooks/events.ts:127](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L127)

Mutable tool-use descriptor carried on tool-call hook events. Matches the shape of the tool use block the model emitted; hooks on [BeforeToolCallEvent](/docs/api/typescript/BeforeToolCallEvent/index.md) may mutate its fields (or reassign the object) to rewrite the input or tool name before the tool executes. The model-issued tool-use ID remains the authoritative provider correlation key.

## Properties

### name

```ts
name: string;
```

Defined in: [src/hooks/events.ts:128](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L128)

---

### toolUseId

```ts
toolUseId: string;
```

Defined in: [src/hooks/events.ts:129](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L129)

---

### input

```ts
input: JSONValue;
```

Defined in: [src/hooks/events.ts:130](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L130)