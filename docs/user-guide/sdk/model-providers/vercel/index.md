The [Vercel AI SDK](https://sdk.vercel.ai/) is a TypeScript toolkit for building AI-powered applications. It defines a [Language Model Specification](https://github.com/vercel/ai/tree/main/packages/provider/src/language-model/v3) that standardizes how applications interact with LLMs across providers. The Strands Agents SDK includes a `VercelModel` adapter that wraps any Language Model Specification v3 (`LanguageModelV3`) provider for use as a Strands model provider.

This means you can bring models from the entire Vercel AI SDK ecosystem - including `@ai-sdk/openai`, `@ai-sdk/anthropic`, `@ai-sdk/amazon-bedrock`, `@ai-sdk/google`, and [many more](https://sdk.vercel.ai/docs/foundations/providers-and-models) - directly into Strands agents.

## Installation

Install the Strands Harness SDK along with the Vercel AI SDK provider package for the model you want to use:

```bash
# OpenAI
npm install @strands-agents/sdk @ai-sdk/openai

# Amazon Bedrock
npm install @strands-agents/sdk @ai-sdk/amazon-bedrock

# Anthropic
npm install @strands-agents/sdk @ai-sdk/anthropic

# Google Generative AI
npm install @strands-agents/sdk @ai-sdk/google
```

The `@ai-sdk/provider` package (which defines the `LanguageModelV3` interface) is listed as an optional peer dependency of `@strands-agents/sdk` and will be installed automatically with any `@ai-sdk/*` provider.

For community providers like Ollama, install the community package directly:

```bash
npm install @strands-agents/sdk ai-sdk-ollama
```

## Usage

Create a `LanguageModelV3` instance from any Vercel provider and wrap it with `VercelModel`:

### OpenAI

```typescript
import { Agent } from '@strands-agents/sdk'
import { VercelModel } from '@strands-agents/sdk/models/vercel'
import { openai } from '@ai-sdk/openai'

const agent = new Agent({
  model: new VercelModel({ provider: openai('gpt-4o') }),
})

const result = await agent.invoke('Hello!')
console.log(result)
```

### Amazon Bedrock

```typescript
import { Agent } from '@strands-agents/sdk'
import { VercelModel } from '@strands-agents/sdk/models/vercel'
import { bedrock } from '@ai-sdk/amazon-bedrock'

const agent = new Agent({
  model: new VercelModel({
    provider: bedrock('global.anthropic.claude-sonnet-4-6'),
  }),
})

const result = await agent.invoke('Hello!')
console.log(result)
```

### Anthropic

```typescript
import { Agent } from '@strands-agents/sdk'
import { VercelModel } from '@strands-agents/sdk/models/vercel'
import { anthropic } from '@ai-sdk/anthropic'

const agent = new Agent({
  model: new VercelModel({ provider: anthropic('claude-sonnet-4-6') }),
})

const result = await agent.invoke('Hello!')
console.log(result)
```

### Google Generative AI

```typescript
import { Agent } from '@strands-agents/sdk'
import { VercelModel } from '@strands-agents/sdk/models/vercel'
import { google } from '@ai-sdk/google'

const agent = new Agent({
  model: new VercelModel({ provider: google('gemini-2.5-flash') }),
})

const result = await agent.invoke('Hello!')
console.log(result)
```

### Ollama

```typescript
import { Agent } from '@strands-agents/sdk'
import { VercelModel } from '@strands-agents/sdk/models/vercel'
import { ollama } from 'ai-sdk-ollama'

const agent = new Agent({
  model: new VercelModel({ provider: ollama('llama3.1') }),
})

const result = await agent.invoke('Hello!')
console.log(result)
```

Note

Ollama must be [installed](https://ollama.com/download) and running locally with your desired model pulled (e.g., `ollama pull llama3.1`).

The [Vercel AI SDK recommends two community Ollama providers](https://ai-sdk.dev/providers/community-providers/ollama): `ollama-ai-provider-v2` as a basic option for simple text generation, and `ai-sdk-ollama` as a more advanced option with reliable tool calling and complete responses. Use `ai-sdk-ollama` so Strands agents get full tool calling support.

## Configuration

`VercelModel` accepts configuration directly alongside the `provider` option. These include all [LanguageModelV3CallOptions](https://github.com/vercel/ai/tree/main/packages/provider/src/language-model/v3) settings (temperature, topP, topK, penalties, stop sequences, seed, etc.) plus the base Strands model config fields.

```typescript
const model = new VercelModel({
  provider: openai('gpt-4o'),
  maxTokens: 1000,
  temperature: 0.7,
  topP: 0.9,
})

const agent = new Agent({ model })
const result = await agent.invoke('Write a short poem')
console.log(result)
```

| Parameter | Description | Example |
| --- | --- | --- |
| `modelId` | Override the model ID (defaults to the provider’s model ID) | `'gpt-4o'` |
| `maxTokens` | Maximum tokens to generate | `1000` |
| `temperature` | Controls randomness | `0.7` |
| `topP` | Nucleus sampling | `0.9` |
| `topK` | Top-k sampling | `40` |
| `presencePenalty` | Encourages new topics | `0.5` |
| `frequencyPenalty` | Reduces repetition | `0.5` |
| `stopSequences` | Custom stop sequences | `['END']` |
| `seed` | Deterministic generation | `42` |

When new fields are added to the Language Model Specification, they become available in the config automatically.

## Streaming

The adapter supports streaming text, reasoning content, and tool use:

```typescript
const agent = new Agent({
  model: new VercelModel({ provider: openai('gpt-4o') }),
})

for await (const event of agent.stream('Tell me a story')) {
  if (
    event.type === 'modelContentBlockDeltaEvent' &&
    event.delta.type === 'textDelta'
  ) {
    process.stdout.write(event.delta.text)
  }
}
```

## Structured Output

The adapter supports structured output through the underlying provider’s native capabilities. Define a Zod schema, pass it as `structuredOutputSchema`, and read validated output from `result.structuredOutput`:

```typescript
import { Agent } from '@strands-agents/sdk'
import { VercelModel } from '@strands-agents/sdk/models/vercel'
import { openai } from '@ai-sdk/openai'
import { z } from 'zod'

const MovieReview = z.object({
  title: z.string().describe('Movie title'),
  rating: z.number().min(1).max(10).describe('Rating from 1-10'),
  genre: z.string().describe('Primary genre'),
  sentiment: z.enum(['positive', 'negative', 'neutral']).describe('Overall sentiment'),
  summary: z.string().describe('Brief summary of the review'),
})

const agent = new Agent({
  model: new VercelModel({ provider: openai('gpt-4o') }),
  structuredOutputSchema: MovieReview,
})

const result = await agent.invoke(
  `Just watched "The Matrix" - what an incredible sci-fi masterpiece!
   The groundbreaking visual effects and philosophical themes make this
   a must-watch. Keanu Reeves delivers a solid performance. 9/10!`
)

const review = result.structuredOutput as z.infer<typeof MovieReview>
console.log(`Movie: ${review.title}`)
console.log(`Rating: ${review.rating}/10`)
console.log(`Sentiment: ${review.sentiment}`)
```

For schema patterns, error handling, and per-invocation overrides, see [Structured Output](/docs/user-guide/sdk/agents/structured-output/index.md).

## Use Strands in a Next.js app

Because `VercelModel` wraps the same `@ai-sdk/*` provider you already use, Strands is *additive* to a Vercel AI SDK app rather than a replacement. Keep your provider packages and your client, and run the Strands agent server-side in an App Router route handler: you get the agent loop, tools, sessions, and hooks around the model you were already calling.

### The route handler

Build the agent with `VercelModel` and stream its events back to the client. Strands requires Node 22+, so run the handler on the Node.js runtime, not the Edge runtime:

app/api/chat/route.ts

```typescript
import { Agent } from '@strands-agents/sdk'
import { VercelModel } from '@strands-agents/sdk/models/vercel'
import { openai } from '@ai-sdk/openai'

// Strands needs the Node.js runtime (Node 22+), not Edge.
export const runtime = 'nodejs'

export async function POST(req: Request) {
  const { prompt } = await req.json()

  const agent = new Agent({
    model: new VercelModel({ provider: openai('gpt-4o') }),
  })

  const encoder = new TextEncoder()
  const stream = new ReadableStream({
    async start(controller) {
      // Each event serializes to wire-safe JSON — its toJSON() drops the live
      // agent reference and keeps only the serializable fields.
      for await (const event of agent.stream(prompt, { cancelSignal: req.signal })) {
        controller.enqueue(encoder.encode(`data: ${JSON.stringify(event)}\n\n`))
      }
      controller.close()
    },
  })

  return new Response(stream, {
    headers: { 'Content-Type': 'text/event-stream' },
  })
}
```

Passing `cancelSignal: req.signal` stops the agent when the client disconnects.

### Rendering on the client

No built-in `useChat` bridge

Strands does not ship a converter from its stream events to the Vercel AI SDK’s UI message (data-stream) protocol, so `useChat` won’t consume the agent stream directly. You either read the event stream yourself, or write a small adapter that maps Strands events onto the [AI SDK stream protocol](https://ai-sdk.dev/docs/ai-sdk-ui/stream-protocol) your AI SDK version expects. Strands gives you the pieces; the target format is the AI SDK’s.

Reading the stream directly means switching on each event’s `type`. The events you care about for a chat UI are `modelStreamUpdateEvent` (streamed text and reasoning deltas), `toolStreamUpdateEvent` (tool progress), and `agentResultEvent` (the final result):

```typescript
const res = await fetch('/api/chat', {
  method: 'POST',
  body: JSON.stringify({ prompt }),
})

const reader = res.body!.getReader()
const decoder = new TextDecoder()

for (;;) {
  const { value, done } = await reader.read()
  if (done) break
  for (const line of decoder.decode(value).split('\n\n')) {
    if (!line.startsWith('data: ')) continue
    const event = JSON.parse(line.slice(6))
    if (event.type === 'modelStreamUpdateEvent') {
      const inner = event.event
      if (inner.type === 'modelContentBlockDeltaEvent' && inner.delta.type === 'textDelta') {
        appendToMessage(inner.delta.text) // render the streamed text
      }
    } else if (event.type === 'agentResultEvent') {
      // event.result is the final AgentResult
    }
  }
}
```

See [Streaming](/docs/user-guide/sdk/streaming/index.md) for the full event union, and [Agent Loop](/docs/user-guide/sdk/agents/agent-loop/index.md) for tools, sessions, and lifecycle hooks you can add around the model.

## Supported features

The `VercelModel` adapter handles:

-   Streaming text, reasoning, and tool use (both incremental and complete tool call events)
-   Message formatting: text, images, documents, video, tool use/results, and reasoning blocks
-   Tool specification and tool choice mapping
-   Usage and token tracking including cache read/write tokens
-   Error classification: maps provider errors to `ModelThrottledError`, `ContextWindowOverflowError`, and `ModelError`

## Compatible providers

Any package that implements the `LanguageModelV3` interface works with `VercelModel`. This includes both official Vercel AI SDK providers and community providers.

### [Official providers](https://sdk.vercel.ai/docs/foundations/providers-and-models)

| Provider | Package |
| --- | --- |
| OpenAI | `@ai-sdk/openai` |
| Amazon Bedrock | `@ai-sdk/amazon-bedrock` |
| Anthropic | `@ai-sdk/anthropic` |
| Google Generative AI | `@ai-sdk/google` |
| Google Vertex | `@ai-sdk/google-vertex` |
| Azure OpenAI | `@ai-sdk/azure` |
| Mistral | `@ai-sdk/mistral` |
| Cohere | `@ai-sdk/cohere` |
| xAI Grok | `@ai-sdk/xai` |
| DeepSeek | `@ai-sdk/deepseek` |
| Groq | `@ai-sdk/groq` |

### [Community providers](https://ai-sdk.dev/providers/community-providers)

| Provider | Package |
| --- | --- |
| Ollama | `ai-sdk-ollama` |

## Troubleshooting

### Missing peer dependency

If you see warnings about `@ai-sdk/provider`, install it explicitly:

```bash
npm install @ai-sdk/provider
```

### Authentication errors

Authentication is handled by the underlying Vercel provider package. Refer to the specific provider’s documentation for credential setup - for example, `@ai-sdk/openai` reads `OPENAI_API_KEY` from the environment, and `@ai-sdk/amazon-bedrock` uses the standard AWS credential chain.

## References

-   [Vercel AI SDK](https://sdk.vercel.ai/)
-   [Language Model Specification v3](https://github.com/vercel/ai/tree/main/packages/provider/src/language-model/v3)
-   [Vercel AI SDK Providers](https://sdk.vercel.ai/docs/foundations/providers-and-models)

## Related pages

- [Google](/docs/user-guide/sdk/model-providers/google/index.md) (1 shared tag)
- [OpenAI](/docs/user-guide/sdk/model-providers/openai/index.md) (1 shared tag)
- [Writer](/docs/user-guide/sdk/model-providers/writer/index.md) (1 shared tag)
- [Multimodal correctness evaluator](/docs/user-guide/evals-sdk/evaluators/multimodal_correctness_evaluator/index.md) (1 shared tag)
- [Multimodal faithfulness evaluator](/docs/user-guide/evals-sdk/evaluators/multimodal_faithfulness_evaluator/index.md) (1 shared tag)
- [Multimodal instruction following evaluator](/docs/user-guide/evals-sdk/evaluators/multimodal_instruction_following_evaluator/index.md) (1 shared tag)
- [Multimodal output evaluator](/docs/user-guide/evals-sdk/evaluators/multimodal_output_evaluator/index.md) (1 shared tag)
- [Multimodal overall quality evaluator](/docs/user-guide/evals-sdk/evaluators/multimodal_overall_quality_evaluator/index.md) (1 shared tag)
- [Amazon Nova](/docs/user-guide/sdk/model-providers/amazon-nova/index.md) (1 shared tag)
- [Amazon Bedrock](/docs/user-guide/sdk/model-providers/amazon-bedrock/index.md) (1 shared tag)


## Implementation

### TypeScript

- [harness-sdk/strands-ts/src/models/vercel.ts](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/models/vercel.ts)
