Defined in: [src/sandbox/errors.ts:38](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/sandbox/errors.ts#L38)

Thrown by [Sandbox.listFiles](/docs/api/typescript/Sandbox/index.md#listfiles) when the path does not exist, distinguishing genuine absence from permission or transport failures (which throw plain errors).

## Extends

-   `Error`

## Constructors

### Constructor

```ts
new SandboxPathNotFoundError(path): SandboxPathNotFoundError;
```

Defined in: [src/sandbox/errors.ts:39](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/sandbox/errors.ts#L39)

#### Parameters

| Parameter | Type |
| --- | --- |
| `path` | `string` |

#### Returns

`SandboxPathNotFoundError`

#### Overrides

`Error.constructor`