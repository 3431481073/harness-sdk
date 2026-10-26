Defined in: [src/tools/tool.ts:48](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/tools/tool.ts#L48)

Data for a tool stream event.

## Properties

### type

```ts
type: "toolStreamEvent";
```

Defined in: [src/tools/tool.ts:52](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/tools/tool.ts#L52)

Discriminator for tool stream events.

---

### data?

```ts
data?: unknown;
```

Defined in: [src/tools/tool.ts:58](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/tools/tool.ts#L58)

Caller-provided data for the progress update. Can be any type of data the tool wants to report.