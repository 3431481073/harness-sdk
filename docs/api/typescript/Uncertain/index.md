Defined in: [src/decisions/types.ts:69](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L69)

Sentinel returned in place of an answer when the decision model declined to commit. Carries an optional free-form reason supplied by the implementation.

## Constructors

### Constructor

```ts
new Uncertain(reason?): Uncertain;
```

Defined in: [src/decisions/types.ts:70](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L70)

#### Parameters

| Parameter | Type |
| --- | --- |
| `reason?` | `string` |

#### Returns

`Uncertain`

## Properties

### reason?

```ts
readonly reason?: string;
```

Defined in: [src/decisions/types.ts:70](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L70)

## Methods

### toString()

```ts
toString(): string;
```

Defined in: [src/decisions/types.ts:72](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L72)

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

Defined in: [src/decisions/types.ts:76](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L76)

#### Returns

```ts
{
  uncertain: true;
  reason?: string;
}
```

| Name | Type | Defined in |
| --- | --- | --- |
| `uncertain` | `true` | [src/decisions/types.ts:76](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L76) |
| `reason?` | `string` | [src/decisions/types.ts:76](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/decisions/types.ts#L76) |