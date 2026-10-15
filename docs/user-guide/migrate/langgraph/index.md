If you currently have a LangGraph application, you can migrate it to Strands Agents without rewriting the code that calls your graph (your callers), and keep the same external IDs for persistence and resumption.

This guide maps the two models concept for concept, then migrates a small example graph (three stages that research, analyze, and review a request) from its LangGraph form to a Strands equivalent. You’ll keep the same public entrypoint and external IDs, and port interrupts, run limits, and tracing to their Strands equivalents, with traces going to an existing OpenTelemetry backend.

This guide assumes you are comfortable with LangGraph’s `StateGraph` and checkpointer model. For the Strands graph model itself, read the [Graph pattern](/docs/user-guide/sdk/multi-agent/graph/index.md) first.

## How LangGraph concepts map to Strands

A LangGraph agent is built from a few moving parts, and this migration guide maps each one onto its Strands counterpart. The sections that follow walk through the important changes to be aware of, ending with a full comparison table.

Before getting started, let’s discuss two important differences for Strands: what a node is, and where state lives.

### A node is an agent, not a function

In LangGraph, a node is a plain function you write. It takes the state, does one thing (e.g., call a model, transform data, check a condition), returns an update, and control goes back to the graph. The reasoning, if any, is code you wrote.

> **Diagram:** In LangGraph, each node is a function you write. Three nodes run in a line, research, then analysis, then review, and each is a plain function that takes the state, such as research(state), does one thing, returns an update, and hands control back to the graph. There is no loop inside a node.

In Strands, a node is an agent that runs its own agent loop. When the node executes, it can reason, call tools, and iterate until it’s done, before handing off to the next node. A single Strands node therefore contains the kind of loop you would have written inside a LangGraph function.

> **Diagram:** In Strands, each node is an agent. The same three nodes, research, then analysis, then review, are each an Agent, and each one loops on its own, reasoning and calling tools until it is done, before handing off to the next node.

The practical rule when migrating: a LangGraph node that called a model becomes an agent, and a node that only did deterministic work (validating input, reshaping state) becomes a [custom node](/docs/user-guide/sdk/multi-agent/graph/index.md#custom-node-types), a callable added to the graph with no agent loop around it, so you don’t wrap pure logic in an unnecessary agent loop.

### State is passed along edges, not shared

State works differently. In LangGraph you define one shared state object, and every node reads from it and returns a partial update that a reducer merges back in. State is a single structure threaded through the entire graph, and the checkpointer snapshots that structure to persist it.

> **Diagram:** In LangGraph, state is one shared object. The research, analysis, and review functions each read the state and return updates that are merged back into a single shared CaseState object, and a checkpointer such as SqliteSaver snapshots that object to persist it.

Strands has no shared state object that nodes write to. Each node passes its output to the nodes that depend on it, and a session manager attached to the graph persists the run separately. Instead of one graph-wide state dict, each agent holds its own conversation for the duration of the run, and the session manager records the graph’s progress so an interrupted run can resume.

> **Diagram:** In Strands, output flows along the edges and there is no shared state object. Research passes its output to analysis, and analysis passes its output to review; each agent keeps its own conversation. A session manager attached to the graph, keyed by the case ID, persists the graph's run state separately.

In practice, you stop modeling state as a single typed object and let each agent carry its own context. The cutover requires no data migration: your public entrypoint and external IDs stay the same, and there is no checkpoint format to translate. Point the new session store at a fresh location and let it fill as cases run.

Note

Once your graph has a join (a node with more than one incoming edge), the Strands SDK behaves differently depending on the language. The Python SDK uses OR semantics, firing a node when any incoming edge from the completed batch is satisfied; TypeScript uses AND semantics, waiting for all incoming edges. See [Waiting for All Dependencies](/docs/user-guide/sdk/multi-agent/graph/index.md#waiting-for-all-dependencies) to make a Python join wait for every branch.

With those in mind, most other LangGraph concepts have a direct Strands counterpart.

| Concept | LangGraph | Strands |
| --- | --- | --- |
| Graph construction | `StateGraph`, `add_node``addNode`, `add_edge``addEdge`, `add_conditional_edges``addConditionalEdges` | `GraphBuilder``new Graph({ nodes, edges })` |
| Entry point | `set_entry_point``setEntryPoint`, edge from `START` | `set_entry_point()``sources` |
| Persistence | Checkpointer (`SqliteSaver`, `InMemorySaver``MemorySaver`) | session manager on the graph |
| Tools | `@tool`, LangChain `bind_tools``bindTools`, `ToolNode`, `tools_condition``toolsCondition` | `Agent(tools=[...])``new Agent({ tools: [...] })` |
| Interrupts | `interrupt()`, `interrupt_before``interruptBefore` | interrupts raised from a hook or a tool |
| Run limits | `recursion_limit``recursionLimit` | invocation limits plus node caps (`set_max_node_executions()``maxSteps`) |
| Streaming | `.stream()`, `astream_events` | `stream_async()``stream()` |
| Tracing | LangSmith | OpenTelemetry via `StrandsTelemetry``setupTracer()` |

## Set up the Strands SDK

Before starting the migration, install the SDK:

(( tab "Python" ))
```bash
pip install strands-agents
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```bash
npm install @strands-agents/sdk
```
(( /tab "TypeScript" ))

## Migrating an example graph

The example for this guide is a small three-stage graph for handling a legal case: a research stage that gathers the facts, an analysis stage that weighs the options, and a review stage that recommends a decision. Each stage feeds the next. The snippets below are abbreviated; complete, runnable versions of both the LangGraph and the Strands programs are in the samples repository, for [Python](https://github.com/strands-agents/samples/tree/main/python/migration/langgraph) and [TypeScript](https://github.com/strands-agents/samples/tree/main/typescript/migration/langgraph). The pipeline is linear, so the migration is easier to follow, and the stages are the same in both frameworks.

> **Diagram:** The example graph. A case prompt goes to the research stage, which gathers the facts. Research feeds the analysis stage, which weighs the options, and analysis feeds the review stage, which recommends a decision.

The LangGraph version wires three node functions into a `StateGraph` and compiles it with a checkpointer, keyed per case by `thread_id`:

(( tab "Python" ))
```python
import sqlite3
from typing import Annotated, TypedDict

from langchain_core.messages import AnyMessage
from langchain_core.tools import tool
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition


@tool
def fetch_case_record(case_id: str) -> str:
    """Fetch the filed record for a case."""
    ...


@tool
def search_precedent(question: str) -> str:
    """Search prior decisions for relevant precedent."""
    ...


class CaseState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    prompt: str
    research: str
    analysis: str
    review: str


def research(state: CaseState) -> dict: ...
def analysis(state: CaseState) -> dict: ...
def review(state: CaseState) -> dict: ...


builder = StateGraph(CaseState)
builder.add_node("research", research)
builder.add_node("research_tools", ToolNode([fetch_case_record]))
builder.add_node("analysis", analysis)
builder.add_node("analysis_tools", ToolNode([search_precedent]))
builder.add_node("review", review)
builder.add_edge(START, "research")
builder.add_conditional_edges("research", tools_condition,
                              {"tools": "research_tools", END: "analysis"})
builder.add_edge("research_tools", "research")
builder.add_conditional_edges("analysis", tools_condition,
                              {"tools": "analysis_tools", END: "review"})
builder.add_edge("analysis_tools", "analysis")
builder.add_edge("review", END)

conn = sqlite3.connect("cases.db", check_same_thread=False)
graph = builder.compile(checkpointer=SqliteSaver(conn))


# Entrypoint: this signature is what your callers use, and it stays the same
def run_case(case_id: str, prompt: str):
    # External ID: case_id keys the conversation, and becomes the Strands session id
    config = {"configurable": {"thread_id": case_id}}
    return graph.invoke({"prompt": prompt}, config)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { tool } from '@langchain/core/tools'
import {
  END,
  MessagesValue,
  START,
  StateGraph,
  StateSchema,
  type GraphNode,
} from '@langchain/langgraph'
import { SqliteSaver } from '@langchain/langgraph-checkpoint-sqlite'
import { ToolNode, toolsCondition } from '@langchain/langgraph/prebuilt'
import { z } from 'zod'

const fetchCaseRecord = tool(async ({ caseId }) => '...', {
  name: 'fetch_case_record',
  description: 'Fetch the filed record for a case.',
  schema: z.object({ caseId: z.string() }),
})

const searchPrecedent = tool(async ({ question }) => '...', {
  name: 'search_precedent',
  description: 'Search prior decisions for relevant precedent.',
  schema: z.object({ question: z.string() }),
})

const CaseState = new StateSchema({
  messages: MessagesValue,
  prompt: z.string(),
  researchText: z.string(),
  analysisText: z.string(),
  reviewText: z.string(),
})

const research: GraphNode<typeof CaseState> = async (state) => ({/* ... */})
const analysis: GraphNode<typeof CaseState> = async (state) => ({/* ... */})
const review: GraphNode<typeof CaseState> = async (state) => ({/* ... */})

const builder = new StateGraph(CaseState)
  .addNode('research', research)
  .addNode('research_tools', new ToolNode([fetchCaseRecord]))
  .addNode('analysis', analysis)
  .addNode('analysis_tools', new ToolNode([searchPrecedent]))
  .addNode('review', review)
  .addEdge(START, 'research')
  .addConditionalEdges('research', toolsCondition, {
    tools: 'research_tools',
    [END]: 'analysis',
  })
  .addEdge('research_tools', 'research')
  .addConditionalEdges('analysis', toolsCondition, {
    tools: 'analysis_tools',
    [END]: 'review',
  })
  .addEdge('analysis_tools', 'analysis')
  .addEdge('review', END)

const graph = builder.compile({ checkpointer: SqliteSaver.fromConnString('cases.db') })

// Entrypoint: this signature is what your callers use, and it stays the same
export async function runCase(caseId: string, prompt: string) {
  // External ID: caseId keys the conversation, and becomes the Strands session id
  const config = { configurable: { thread_id: caseId } }
  return graph.invoke({ prompt }, config)
}
```
(( /tab "TypeScript" ))

Pay close attention to the highlighted lines above. Migrating without breaking your callers means holding both of them stable while you swap the internals:

1.  Public function: keep the function your callers invoke unchanged. `run_case(case_id, prompt)``runCase(caseId, prompt)` keeps that exact signature, and only its body changes. Nothing that calls it has to change.
    
2.  External ID: keep the ID your callers already pass. Both frameworks use an ID to recognize that a call belongs to existing persisted state. LangGraph calls this a `thread_id`; Strands calls it a session ID. Pass the same `case_id``caseId` to Strands as the session ID, so callers do not change and a run interrupted in Strands resumes under the same ID. Strands session IDs must use only lowercase letters, digits, `_` and `-`. The TypeScript SDK rejects anything else; Python rejects only path separators. A `thread_id` outside that set has to be mapped before it becomes a session ID.
    

The Strands version keeps `run_case(case_id, prompt)``runCase(caseId, prompt)` intact. Each node becomes an agent with a system prompt, the pipeline edges stay the same, and the checkpointer becomes a session manager keyed by the case ID:

(( tab "Python" ))
```python
from strands import Agent, tool
from strands.multiagent import GraphBuilder
from strands.session import FileSessionManager

@tool
def fetch_case_record(case_id: str) -> str:
    """Fetch the filed record for a case.

    Args:
        case_id: Identifier of the case to fetch
    """
    return f"...filed record for {case_id}..."


@tool
def search_precedent(question: str) -> str:
    """Search prior decisions for relevant precedent.

    Args:
        question: What to look for in prior decisions
    """
    return "...matching prior decisions..."


# Entrypoint: same signature as the LangGraph version
def run_case(case_id: str, prompt: str):
    researcher = Agent(
        name="research",
        system_prompt="You gather the facts of the case.",
        tools=[fetch_case_record],
    )
    analyst = Agent(
        name="analysis",
        system_prompt="You weigh the options.",
        tools=[search_precedent],
    )
    reviewer = Agent(name="review", system_prompt="You recommend a decision.")

    builder = GraphBuilder()
    builder.add_node(researcher, "research")
    builder.add_node(analyst, "analysis")
    builder.add_node(reviewer, "review")
    builder.add_edge("research", "analysis")
    builder.add_edge("analysis", "review")
    builder.set_entry_point("research")
    builder.set_max_node_executions(10)

    # case_id is the session id: an interrupted graph resumes from it on the next call
    builder.set_session_manager(
        FileSessionManager(session_id=case_id, storage_dir="./cases/")
    )
    # The task text is what the model sees, so the case id is prefixed onto it.
    return builder.build()(f"Case {case_id}: {prompt}")


result = run_case("case-4127", "Assess the dispute and recommend a decision.")
print(f"Status: {result.status}")
print(f"Order: {[node.node_id for node in result.execution_order]}")
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent, Graph, SessionManager, tool } from '@strands-agents/sdk'
import { LocalFileStorage } from '@strands-agents/sdk/storage'
import { z } from 'zod'

const fetchCaseRecord = tool({
  name: 'fetch_case_record',
  description: 'Fetch the filed record for a case',
  inputSchema: z.object({
    caseId: z.string().describe('Identifier of the case to fetch'),
  }),
  callback: (input) => `...filed record for ${input.caseId}...`,
})

const searchPrecedent = tool({
  name: 'search_precedent',
  description: 'Search prior decisions for relevant precedent',
  inputSchema: z.object({
    question: z.string().describe('What to look for in prior decisions'),
  }),
  callback: () => '...matching prior decisions...',
})

// Same public entrypoint your callers already use
async function runCase(caseId: string, prompt: string) {
  const researcher = new Agent({
    id: 'research',
    systemPrompt: 'You gather the facts of the case.',
    tools: [fetchCaseRecord],
  })
  const analyst = new Agent({
    id: 'analysis',
    systemPrompt: 'You weigh the options.',
    tools: [searchPrecedent],
  })
  const reviewer = new Agent({
    id: 'review',
    systemPrompt: 'You recommend a decision.',
  })

  const graph = new Graph({
    nodes: [researcher, analyst, reviewer],
    edges: [
      ['research', 'analysis'],
      ['analysis', 'review'],
    ],
    sources: ['research'],
    maxSteps: 10,
    // caseId is the session id: an interrupted graph resumes from it on the next call
    sessionManager: new SessionManager({
      sessionId: caseId,
      storage: new LocalFileStorage('./cases/'),
    }),
  })
  // The task text is what the model sees, so the case id is prefixed onto it.
  return graph.invoke(`Case ${caseId}: ${prompt}`)
}

const result = await runCase(
  'case-4127',
  'Assess the dispute and recommend a decision.'
)
console.log('Status:', result.status)
console.log('Order:', result.results.map((r) => r.nodeId).join(' -> '))
```
(( /tab "TypeScript" ))

The result object reports the run status and which nodes ran, through `execution_order``results`, so you can assert the pipeline ran end to end. For conditional routing, give an edge a condition function, the equivalent of LangGraph’s `add_conditional_edges``addConditionalEdges`. For more information, see the [conditional edges documentation](/docs/user-guide/sdk/multi-agent/graph/index.md#conditional-edges).

## Port your tools

In LangGraph, tools sit outside the model call: you bind them to the model, execute them in a `ToolNode`, and route back with a `tools_condition``toolsCondition` edge, which adds a cycle to the graph. A Strands agent runs that loop itself, so the tools move onto the agent and both the tool node and its edges disappear.

| Concept | LangGraph | Strands |
| --- | --- | --- |
| Define a tool | plain function, or `@tool from langchain_core.tools``tool() from @langchain/core/tools` | `@tool``tool()` |
| Attach it | `bind_tools([...])``bindTools([...])` | `Agent(tools=[...])``new Agent({ tools: [...] })` |
| Execute the call | `ToolNode` | the agent loop |
| Route back to the model | `tools_condition``toolsCondition` edge | automatic |

Not every node needs tools. The review stage above works from what the earlier stages produced, so it has none.

(( tab "Python" ))
Parameter descriptions start reaching the model

LangChain parses a docstring’s `Args:` section only when you pass `parse_docstring=True`, and it defaults to `False`. Strands always parses it, so parameter descriptions your LangGraph tool never sent to the model will start being sent. That changes the tool schema the model sees.
(( /tab "Python" ))

(( tab "TypeScript" ))
Parameter descriptions reach the model the same way

Both frameworks take the tool’s parameter schema from zod, so a `.describe()` on a field reaches the model the same way in each. The schema the model sees does not change.
(( /tab "TypeScript" ))

For class-based and module-format tools, see [Create custom tools](/docs/user-guide/sdk/tools/custom-tools/index.md).

## Managing state and persistence

LangGraph’s checkpointer serializes the shared state object per super-step, and because a node is a function that writes its messages into that state, saving the state saves the conversation with it. A Strands node is an agent running its own loop, so its messages belong to the agent rather than to the graph. Strands uses a session manager attached to the graph, so what it persists is the run: which nodes completed, what each one returned, and which are still pending. The conversation of a completed node is not kept. A node that stopped on an interrupt is the exception: its messages are saved with the run so that the node can pick up where it left off when the run resumes.

In the migrated example above, we attached a session manager directly to the graph:

(( tab "Python" ))
```python
builder.set_session_manager(
    FileSessionManager(session_id=case_id, storage_dir="./cases/")
)
```

Attach a `FileSessionManager`, `S3SessionManager` or `SnapshotSessionManager` (with a `storage` argument) to the graph with `set_session_manager`. An agent inside the graph must **not** carry its own session manager; `add_node` raises `ValueError` if it does.
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { LocalFileStorage } from '@strands-agents/sdk/storage'

const graph = new Graph({
  // ...nodes, edges, and sources
  sessionManager: new SessionManager({
    sessionId: caseId,
    storage: new LocalFileStorage('./cases/'),
  }),
})
```

One `SessionManager` covers both single agents and graphs, and it is passed to the graph through the `sessionManager` field. A node agent may also carry its own `SessionManager`, in which case its conversation is persisted alongside the graph’s run. By default a graph node restores the agent to its pre-run state when it completes, so `agent.messages` is unchanged in memory and the persisted conversation lives only in the session store. Pass `preserveContext: true` on the node to let the agent accumulate state across executions instead.
(( /tab "TypeScript" ))

What that session manager saves decides what a repeat call sees. Take the same case run twice:

(( tab "Python" ))
```python
run_case("case-4127", "Assess the dispute and recommend a decision.")
run_case("case-4127", "Assess the dispute and recommend a decision.")
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
await runCase('case-4127', 'Assess the dispute and recommend a decision.')
await runCase('case-4127', 'Assess the dispute and recommend a decision.')
```
(( /tab "TypeScript" ))

In LangGraph the second call starts with the first call’s `messages` already in `CaseState`, because the checkpointer restored them. In Strands the second call assesses the case again from research through review. The session store holds what each node returned last time, not the conversation that produced it, so every agent starts empty (in TypeScript, unless the node agent carries its own `SessionManager`). If a caller needs those earlier messages, keep them yourself and pass them in with `Agent(messages=...)``new Agent({ messages: ... })` when `run_case``runCase` rebuilds the graph.

The two SDKs differ in what the second call keeps from the first. Python resets the stored run, so each call reports three node results. TypeScript restarts at the source nodes without clearing the restored run, so the step count and the results array carry over: for this three-node graph the second call reports six results, the third nine, and the fourth call with `maxSteps: 10` fails with `max steps reached`. A failed node result from an earlier call also stays in the array, and because the aggregate status reports failed when any result is failed, the run keeps reporting failed. For a clean repeat in TypeScript, use a new session ID for each call or delete the stored session first.

The stored run does matter when the first call did not finish. If the process dies after research completes, the next call with that case ID reuses research’s result and runs only analysis and review. The restored node still appears in the result’s node list (`execution_order``results`), so check its tool calls rather than that list to confirm it was not re-run. Resumption works from a separate process, which is what lets an approval gate be answered elsewhere.

Both frameworks leave concurrency to you. Neither takes a distributed lock. Strands’ built-in stores write without a lock and without a version check, so a write never detects that another writer has changed the same record. Two writers on the same session ID can overwrite each other’s turns, the last write wins, and neither call errors. Give each case its own session ID, run one live writer per case, and add locking in the backend or the caller if concurrent writers are possible. See [Sessions, agents, and concurrency](/docs/user-guide/sdk/agents/session-management/index.md#sessions-agents-and-concurrency) and [Storage](/docs/user-guide/sdk/storage/index.md) for backend configuration and tradeoffs.

## Add approval gates with interrupts

LangGraph pauses a run with `interrupt()` or `interrupt_before``interruptBefore`. Strands raises an interrupt from a hook or a tool, hands control back with the pending interrupt, and resumes when you pass a response. To gate a node in a graph, raise the interrupt from a `BeforeNodeCallEvent` hook and loop until the run stops interrupting:

```python
import json

from strands import Agent
from strands.hooks import BeforeNodeCallEvent, HookProvider, HookRegistry
from strands.multiagent import GraphBuilder, Status


class ReviewApproval(HookProvider):
    def register_hooks(self, registry: HookRegistry, **kwargs) -> None:
        registry.add_callback(BeforeNodeCallEvent, self.approve)

    def approve(self, event: BeforeNodeCallEvent) -> None:
        if event.node_id != "review":
            return
        # Pauses the run here and returns the caller's answer when it resumes
        approval = event.interrupt("review-approval", reason={"node": event.node_id})
        if approval.lower() != "y":
            event.cancel_node = "Reviewer declined to proceed"


builder = GraphBuilder()
builder.add_node(Agent(name="analysis"), "analysis")
builder.add_node(Agent(name="review"), "review")
builder.add_edge("analysis", "review")
builder.set_entry_point("analysis")
builder.set_hook_providers([ReviewApproval()])
graph = builder.build()

result = graph("Assess the tenant dispute in the record.")
while result.status == Status.INTERRUPTED:
    responses = []
    for interrupt in result.interrupts:
        answer = input(f"Approve {interrupt.reason['node']}? (y/N): ")
        responses.append(
            {"interruptResponse": {"interruptId": interrupt.id, "response": answer}}
        )
    result = graph(responses)

print(json.dumps(result.results["review"].result.message, indent=2))
```

TypeScript follows the same shape. You raise from a `BeforeNodeCallEvent` hook, check for the interrupted status, and resume with the responses. However the API differs in a few areas: hooks attach via `graph.addHook()` rather than a `HookProvider`, `event.interrupt()` takes an options object, cancelling a node is `event.cancel`, responses resume through `graph.invoke()` as `InterruptResponseContent` instances, and `result.results` is an array of node results carrying a `nodeId` rather than a dictionary keyed by node ID. For runnable examples in both languages, see [Interrupts in multi-agent systems](/docs/user-guide/sdk/interrupts-multi-agent/index.md).

## Bound a run

LangGraph gives you `recursion_limit``recursionLimit` to cap a run. Strands has no single setting that does the same, because a Strands node is an agent that runs its own loop. The graph counts the nodes it runs, but it cannot see what happens inside them, so one node execution can use any number of turns. That means there are two places to set a limit: on the graph, with a node cap and a timeout, and on agent calls you make yourself, with turn and token budgets. Agents inside a graph are bounded by the graph’s cap and timeout; the graph does not pass invocation limits to its nodes.

### Node caps

The main example above sets a node cap when it builds the graph. A timeout goes in the same place:

(( tab "Python" ))
```python
# ...nodes and edges
builder.set_max_node_executions(10)
builder.set_execution_timeout(300)  # seconds, checked between batches
builder.set_node_timeout(60)  # seconds, cancels a node that is still running
```

Python checks the execution timeout between batches of nodes, so it does not stop an agent that is already running. Set a node timeout as well to bound each node while it runs.
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
const graph = new Graph({
  // ...nodes, edges, and sources
  maxSteps: 10,
  timeout: 300_000, // milliseconds
})
```
(( /tab "TypeScript" ))

Without a node cap or an execution timeout, the SDK logs a warning that the graph has no execution limit.

Because LangGraph executes a graph in super-steps, where every node scheduled together runs in parallel within a single step, the two counts are not equivalent. A node cap counts every node that runs, while `recursion_limit``recursionLimit` counts the steps. Reusing the same number will not give the same bound. TypeScript checks `maxSteps` as each node is scheduled. Python checks its cap between batches, so a parallel batch can carry the run past the configured value before it stops.

When a run reaches the limit, LangGraph and Strands report it differently. LangGraph raises `GraphRecursionError`. Strands in Python completes the run and reports a failed status on the result when it next checks the cap; if the batch that exceeded the cap is the last one, the run reports completed. Strands in TypeScript throws a plain `Error` whose message reads `steps=<10> | max steps reached`, with no dedicated type to catch.

### Invocation limits

Invocation limits apply to a single agent call. Pass a budget for turns, output tokens, and total tokens:

(( tab "Python" ))
```python
from strands import Agent

agent = Agent()

result = agent(
    "Summarize the case file",
    limits={"turns": 5, "output_tokens": 2000, "total_tokens": 10000},
)

if result.stop_reason == "limit_turns":
    print("Hit turn budget")
elif result.stop_reason == "limit_output_tokens":
    print("Hit output budget")
elif result.stop_reason == "limit_total_tokens":
    print("Hit token budget")
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent } from '@strands-agents/sdk'

const agent = new Agent()

const result = await agent.invoke('Summarize the case file', {
  limits: {
    turns: 5,
    outputTokens: 2000,
    totalTokens: 10000,
  },
})

if (result.stopReason === 'limitTurns') {
  console.log('Hit turn budget')
} else if (result.stopReason === 'limitOutputTokens') {
  console.log('Hit output budget')
} else if (result.stopReason === 'limitTotalTokens') {
  console.log('Hit token budget')
}
```
(( /tab "TypeScript" ))

These are checked at turn boundaries rather than mid-response, so treat them as soft ceilings: tools already in flight finish, and a run can overshoot its token budget by one turn.

### Cancellation

To stop a run from outside, such as on a client disconnect or a timeout, pass a cancellation signal:

(( tab "Python" ))
```python
import threading

from strands import Agent

agent = Agent()

cancel_signal = threading.Event()
threading.Timer(30.0, cancel_signal.set).start()  # fire the signal after 30s, bounding the run

result = agent("Assess the case file", cancel_signal=cancel_signal)

if result.stop_reason == "cancelled":
    print("Run cancelled: exceeded time budget")
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent } from '@strands-agents/sdk'

const agent = new Agent()

// Cancel the run if it exceeds the time budget
const result = await agent.invoke('Assess the case file', {
  cancelSignal: AbortSignal.timeout(30_000),
})

if (result.stopReason === 'cancelled') {
  console.log('Run cancelled: exceeded time budget')
}
```
(( /tab "TypeScript" ))

Every result carries a typed `result.stop_reason``result.stopReason` that tells you why the run ended. You compare it directly instead of matching on an error message. Python defines the values as a closed set; TypeScript names the same values but the type also admits other strings, so handle an unknown value rather than assuming the list is complete.

Beyond the limit and cancellation values above, common reasons include `end_turn``endTurn` (the agent finished) and `guardrail_intervened``guardrailIntervened`. The three limit values mean the run used up the turns or tokens you allowed in `limits`. Nothing is raised and the run stops at a turn boundary. You can call the agent again with larger numbers. A single model response that hits the provider’s output cap is not reported as a stop reason: it raises `MaxTokensReachedException``MaxTokensError`. See [Stop reasons](/docs/user-guide/sdk/agents/agent-loop/index.md#stop-reasons).

## Tracing

If your LangGraph app reports to LangSmith, point Strands at the same OpenTelemetry backend instead. Strands emits spans predominantly under the OpenTelemetry GenAI semantic conventions (`gen_ai.*`), so any OTLP-compatible collector receives them.

Install the tracing dependencies:

(( tab "Python" ))
```bash
pip install 'strands-agents[otel]'
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```bash
npm install @opentelemetry/api @opentelemetry/sdk-trace-node @opentelemetry/sdk-trace-base @opentelemetry/sdk-metrics @opentelemetry/resources @opentelemetry/exporter-trace-otlp-http @opentelemetry/exporter-metrics-otlp-http
```

Install the SDK before these packages. The SDK declares the versions it accepts, and installing them first can resolve to a newer release than the SDK allows.
(( /tab "TypeScript" ))

Point the exporter at your collector with the standard OpenTelemetry variables, the same ones a LangSmith OTLP setup uses:

```bash
export OTEL_EXPORTER_OTLP_ENDPOINT="http://collector.example.com:4318"
export OTEL_EXPORTER_OTLP_HEADERS="key1=value1,key2=value2"
```

Register a tracer provider once at startup. Tracing then turns on automatically. Attributes you pass to an agent are added to the spans that agent starts: in Python every span, in TypeScript the agent span, with graph and node spans carrying the attributes passed to the graph as a separate setting:

(( tab "Python" ))
```python
from strands import Agent
from strands.telemetry import StrandsTelemetry

telemetry = StrandsTelemetry()
telemetry.setup_otlp_exporter()     # export to your OTLP endpoint
telemetry.setup_console_exporter()  # print spans to the console

agent = Agent(
    system_prompt="You review casework.",
    trace_attributes={"case.id": "case-4127"},
)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent } from '@strands-agents/sdk'
import { setupTracer } from '@strands-agents/sdk/telemetry'

// Register a tracer provider once at startup
setupTracer({
  exporters: { otlp: true, console: true },
})

// Tracing turns on automatically; these attributes are added to this agent's span
const agent = new Agent({
  systemPrompt: 'You review casework.',
  traceAttributes: { 'case.id': 'case-4127' },
})
```
(( /tab "TypeScript" ))

If a global tracer provider already exists in your process, Strands uses it and you can skip the setup call. See [Traces](/docs/user-guide/sdk/observability-evaluation/traces/index.md) for the full span structure and attribute list.

## Verify the migration

Before finalizing the migration, confirm the port preserved behavior:

-   **The public API is unchanged.** Callers invoke the same entrypoint with the same arguments and the same external IDs.
-   **Resumption works.** Stop a run partway, then call the entrypoint again with the same case ID. A restored node still appears in the result’s node list, so confirm resumption by checking that the completed node made no new tool calls. Calling twice after a successful run does not demonstrate resumption, because a completed graph starts again from the beginning.
-   **Transcripts are equivalent.** Run representative cases through both systems and compare outputs for parity. Responses are non-deterministic, so check that each stage does its job rather than expecting identical text.
-   **Bounds hold.** Trip a turn or token limit and confirm the run stops with the expected stop reason instead of running away.
-   **Traces arrive.** Run one case and confirm spans reach your collector with the attributes you attached.

The complete before and after programs for the example in this guide are in the samples repository, for [Python](https://github.com/strands-agents/samples/tree/main/python/migration/langgraph) and [TypeScript](https://github.com/strands-agents/samples/tree/main/typescript/migration/langgraph). Each pair runs the same two cases, so you can use them to try the checks above before applying them to your own graph.