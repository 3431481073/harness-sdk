[OpenAI GPT-Live](https://developers.openai.com/api/docs/guides/live) brings continuous voice conversations to your agents. The Live model listens and speaks while a separate Responses model handles reasoning and selects tools for `BidiAgent` to execute.

Follow the [quickstart](/docs/user-guide/sdk/bidi/quickstart/index.md) to build a voice agent, using the Live configuration below.

## Installation

Install the OpenAI Live extra in a separate virtual environment:

```bash
pip install "strands-agents[bidi-openai-live]"
```

For local audio dependencies and device setup, see [Audio I/O](/docs/user-guide/sdk/bidi/io/index.md#audio-io).

## Credentials

Create an [OpenAI API key](https://platform.openai.com/settings/organization/api-keys) with access to your chosen Live and Responses models, then set it in your environment:

```bash
export OPENAI_API_KEY="your-api-key"
```

`OpenAILiveModel` reads `OPENAI_API_KEY` automatically. Pass OpenAI client options through `client_args`, such as `client_args={"api_key": "your-api-key"}`.

## Configuration

Configure a Live model for speech and a Responses model for reasoning and tool use, then pass the provider to `BidiAgent`:

```python
from strands.bidi.agent import BidiAgent
from strands.bidi.models import OpenAILiveModel

model = OpenAILiveModel(
    model_id="gpt-live-1",
    delegation_config={"type": "responses", "model_id": "gpt-6-luna"},
    voice="marin",
    audio_config={"sample_rate": 24000},
)
agent = BidiAgent(model=model)
```

Both model IDs are required. The top-level `model_id` selects the voice model; `delegation_config["model_id"]` selects the Responses model. Only Responses delegation is supported.

Choose an OpenAI [voice](https://developers.openai.com/api/docs/guides/live-conversations#voice-options) or omit `voice` to use the API default. Input and output use mono PCM16 at 24 kHz; set `audio_config={"sample_rate": 16000}` for 16 kHz. Custom inputs must stream continuously, including silence.

See the [`OpenAILiveModel` API reference](/docs/api/python/strands.bidi.models#strands.bidi.models.OpenAILiveModel.__init__) for all constructor options.

### Delegation settings

Configure backend reasoning and output through `delegation_config`:

```python
from strands.bidi.models import OpenAILiveModel

model = OpenAILiveModel(
    model_id="gpt-live-1",
    delegation_config={
        "type": "responses",
        "model_id": "gpt-6-luna",
        "max_output_tokens": 512,
        "reasoning": {"effort": "low"},
    },
)
```

Set `delegation_config["system_prompt"]` to override the agent’s system prompt for backend reasoning and tool use. Otherwise, both models use the agent’s prompt. Register tools on `BidiAgent`.

For text settings, service tier, and other options, see [`OpenAILiveResponsesDelegationConfig`](/docs/api/python/strands.bidi.models#strands.bidi.models.OpenAILiveResponsesDelegationConfig) and OpenAI’s [Responses delegation guide](https://developers.openai.com/api/docs/guides/live-delegation).

## Connection restarts

The provider saves sessions with OpenAI and [forks them](https://developers.openai.com/api/docs/guides/live-conversations#store-and-fork-a-session) on restart, preserving the conversation and configuration. Forking requires enabled project storage and a finalized recording; it is unavailable with Zero Data Retention.

Automatic restart is disabled

Automatic restart defaults to disabled because Live cannot identify completed spoken turns. Set `connection={"auto_restart": True}` to enable it, accepting that a restart may cut off speech. See [Connection restarts](/docs/user-guide/sdk/bidi/agent/index.md#connection-restarts) for scheduling options.

## Compatibility

When consuming [Strands events](/docs/user-guide/sdk/bidi/events/index.md#event-ordering), account for these differences:

Response stops do not mark completed speech

Live has no event marking the end of each spoken response. The provider creates Strands response boundaries at new backend text streams or tool-use groups. Without such a transition, audio and response streams can remain open until the session closes.

`BidiResponseStopEvent` does not indicate that speech has finished. Track playback in your audio player, and do not end a conversation on the first response stop.

-   **Transcripts:** Each API fragment becomes a completed transcript block and [history message](/docs/user-guide/sdk/bidi/events/index.md#messages), even when it contains only part of a sentence. Backend text and spoken transcripts both enter history.
-   **Barge-in:** The provider does not emit `BidiBargeInEvent`. Strands cannot automatically clear buffered audio or cancel tools when the user speaks.
-   **Usage:** Token usage covers the Responses model only. Live reports voice duration in seconds, which Strands token metrics do not include. See OpenAI’s [usage guidance](https://developers.openai.com/api/docs/guides/live-conversations#usage-and-graceful-close).

## Related pages

- [BidiAgent](/docs/user-guide/sdk/bidi/agent/index.md) (1 shared tag)
- [Bidirectional Streaming](/docs/user-guide/sdk/bidi/index.md) (1 shared tag)
- [Bidirectional Streaming Models](/docs/user-guide/sdk/bidi/models/index.md) (1 shared tag)
- [Google Gemini Live](/docs/user-guide/sdk/bidi/models/google/index.md) (1 shared tag)
- [I/O Streams](/docs/user-guide/sdk/bidi/io/index.md) (1 shared tag)
- [Input Content](/docs/user-guide/sdk/bidi/content/index.md) (1 shared tag)
- [Interrupts](/docs/user-guide/sdk/bidi/interrupts/index.md) (1 shared tag)
- [OpenAI Realtime](/docs/user-guide/sdk/bidi/models/openai/realtime/index.md) (1 shared tag)
- [Stream Events](/docs/user-guide/sdk/bidi/events/index.md) (1 shared tag)
- [Tools](/docs/user-guide/sdk/bidi/tools/index.md) (1 shared tag)


## Implementation

### Python

- [harness-sdk/strands-py/src/strands/bidi/models/openai/live.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/bidi/models/openai/live.py)
- [harness-sdk/strands-py/src/strands/bidi/models/openai/configs.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/bidi/models/openai/configs.py)
