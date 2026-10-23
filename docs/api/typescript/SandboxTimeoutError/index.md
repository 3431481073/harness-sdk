Defined in: [src/sandbox/errors.ts:13](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/sandbox/errors.ts#L13)

Thrown by sandbox execution when the configured `timeout` elapses.

`stdout` and `stderr` hold whatever the process wrote before it was killed.

## Extends

-   `Error`

## Constructors

### Constructor

```ts
new SandboxTimeoutError(
   seconds,
   stdout?,
   stderr?
): SandboxTimeoutError;
```

Defined in: [src/sandbox/errors.ts:14](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/sandbox/errors.ts#L14)

#### Parameters

| Parameter | Type | Default value |
| --- | --- | --- |
| `seconds` | `number` | `undefined` |
| `stdout?` | `string` | `''` |
| `stderr?` | `string` | `''` |

#### Returns

`SandboxTimeoutError`

#### Overrides

```ts
Error.constructor
```

## Properties

### stdout

```ts
readonly stdout: string = '';
```

Defined in: [src/sandbox/errors.ts:16](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/sandbox/errors.ts#L16)

---

### stderr

```ts
readonly stderr: string = '';
```

Defined in: [src/sandbox/errors.ts:17](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/sandbox/errors.ts#L17)