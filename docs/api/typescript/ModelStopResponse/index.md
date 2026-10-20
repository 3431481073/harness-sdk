Defined in: [src/hooks/events.ts:471](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L471)

Response from a model invocation containing the message and stop reason.

## Properties

### message

```ts
readonly message: Message;
```

Defined in: [src/hooks/events.ts:475](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L475)

The message returned by the model.

---

### stopReason

```ts
readonly stopReason: StopReason;
```

Defined in: [src/hooks/events.ts:479](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L479)

The reason the model stopped generating.

---

### redaction?

```ts
readonly optional redaction?: Redaction;
```

Defined in: [src/hooks/events.ts:485](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/hooks/events.ts#L485)

Optional redaction info when guardrails blocked input. When present, indicates the last user message was redacted. The redacted message is available in `agent.messages` (last message).