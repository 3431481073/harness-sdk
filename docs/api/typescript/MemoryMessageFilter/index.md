Defined in: [src/memory/extraction/types.ts:29](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/types.ts#L29)

Filters content blocks out of messages before extraction.

Blocks whose kind is in [exclude](#exclude) are stripped; a message left with no content is dropped entirely. Defaults to excluding tool traffic (`toolUse` / `toolResult`), which is rarely useful as long-term memory and adds noise.

## Properties

### exclude

```ts
exclude: MemoryContentBlockType[];
```

Defined in: [src/memory/extraction/types.ts:31](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/memory/extraction/types.ts#L31)

Content block kinds to strip before extraction.