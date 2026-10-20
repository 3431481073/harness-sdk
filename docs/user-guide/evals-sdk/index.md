Strands Evals is how you measure an agent before you ship it and watch it after. Score its output and its trajectory, detect and diagnose failures, probe it for unsafe behavior, and simulate the users and tools it will meet in production.

[Quickstart](quickstart/index.md)Run your first evaluation end to end.

[Evaluators](evaluators/index.md)Score output, trajectory, and interactions.

[Detectors](detectors/index.md)Find failures and trace their root cause.

[Red teaming](red-teaming/index.md)Probe an agent for unsafe behavior.

[Simulators](simulators/index.md)Simulate the users and tools an agent meets.

[CLI](cli/index.md)Run evaluations from the command line.

## Start with the CLI

The fastest way to try Strands Evals is the `strands-evals` command that installs with the package. Point it at a function that builds your agent and it runs a whole evaluation with no runner script:

```bash
pip install strands-agents-evals

# One-off check: does the agent's answer contain "Paris"?
strands-evals run \
  --input "What is the capital of France?" \
  --expected-output "Paris" \
  --agent my_agent:build_agent

# Generate a starter experiment from a description of your agent, then run it
strands-evals generate \
  --context "$(cat tools.txt)" \
  --num-cases 10 \
  --evaluator OutputEvaluator \
  -o experiment.json
strands-evals run experiment.json --agent my_agent:build_agent --display
```

The [CLI section](/docs/user-guide/evals-sdk/cli/index.md) documents every subcommand: running experiments, generating test cases, rendering reports, and diagnosing failing sessions.

## Score an agent

The same evaluation is available as a Python API when you need custom tasks, evaluators, or simulators. An evaluation is a task that produces output, cases that define the inputs and what you expect, and an evaluator that scores each result:

```python
from strands import Agent
from strands_evals import eval_task, Case, Experiment
from strands_evals.evaluators import OutputEvaluator

@eval_task()
def get_response():
    return Agent(system_prompt="Answer accurately and concisely.")

cases = [
    Case[str, str](
        name="capital",
        input="What is the capital of France?",
        expected_output="Paris",
    )
]

evaluator = OutputEvaluator(rubric="Score 1.0 if the answer is correct, else 0.0.")

report = Experiment[str, str](cases=cases, evaluators=[evaluator]).run_evaluations(
    get_response
)
report.display()
```

The [quickstart](/docs/user-guide/evals-sdk/quickstart/index.md) runs this end to end and reads the results.

## Reference

Strands Evals keeps its reference material on the pages that describe each piece, not in a separate section:

-   Every [evaluator](/docs/user-guide/evals-sdk/evaluators/index.md) page documents that evaluator’s parameters and scoring in full; the [evaluators overview](/docs/user-guide/evals-sdk/evaluators/index.md) summarizes what each one checks and links to that detail.
-   The [CLI section](/docs/user-guide/evals-sdk/cli/index.md) is the reference for the `strands-evals` command: every subcommand, its flags, and its exit codes.