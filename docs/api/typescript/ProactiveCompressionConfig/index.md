```ts
type ProactiveCompressionConfig = {
  compressionThreshold: number;
};
```

Defined in: [src/conversation-manager/conversation-manager.ts:56](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/conversation-manager/conversation-manager.ts#L56)

Configuration for proactive compression when passed as an object.

## Properties

### compressionThreshold

```ts
compressionThreshold: number;
```

Defined in: [src/conversation-manager/conversation-manager.ts:62](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/conversation-manager/conversation-manager.ts#L62)

Ratio of context window usage that triggers proactive compression. Value between 0 (exclusive) and 1 (inclusive). Defaults to 0.7 (compress when 70% of the context window is used).