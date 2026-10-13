Defined in: [src/decisions/types.ts:62](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L62)

Sentinel returned in place of an answer when the decision model declined to commit. Carries an optional free-form reason supplied by the implementation.

## Constructors

### Constructor

```ts
new Uncertain(reason?): Uncertain;
```

Defined in: [src/decisions/types.ts:63](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L63)

#### Parameters

| Parameter | Type |
| --- | --- |
| `reason?` | `string` |

#### Returns

`Uncertain`

## Properties

### reason?

```ts
readonly optional reason?: string;
```

Defined in: [src/decisions/types.ts:63](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L63)

## Methods

### toString()

```ts
toString(): string;
```

Defined in: [src/decisions/types.ts:65](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L65)

#### Returns

`string`

---

### toJSON()

```ts
toJSON(): {
  uncertain: true;
  reason?: string;
};
```

Defined in: [src/decisions/types.ts:69](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L69)

#### Returns

```ts
{
  uncertain: true;
  reason?: string;
}
```

| Name | Type | Defined in |
| --- | --- | --- |
| `uncertain` | `true` | [src/decisions/types.ts:69](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L69) |
| `reason?` | `string` | [src/decisions/types.ts:69](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L69) |