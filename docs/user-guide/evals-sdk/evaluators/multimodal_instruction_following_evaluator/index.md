The `MultimodalInstructionFollowingEvaluator` assesses whether an agent response satisfies the explicit constraints in the user’s instruction (count, format, scope, order, completeness, and style), independently of factual accuracy.

## Key features

-   **Output-Level Evaluation**: Scores a single agent response per case
-   **Binary Scoring**: `1.0` if all constraints are satisfied, `0.0` if any constraint is violated
-   **Constraint-Focused**: Evaluates compliance with directives, not overall correctness or quality
-   **Image-Aware**: Verifies image-referential constraints (e.g., “describe only the background”)

## When to use

Use the `MultimodalInstructionFollowingEvaluator` when you need to:

-   Verify that responses respect format constraints (bullet vs. numbered list, paragraph, JSON)
-   Check count constraints (“exactly N sentences”, “in one paragraph”)
-   Assess scope constraints (“describe only the foreground”, “do not mention people”)
-   Validate order constraints (“left to right”, “largest to smallest”)
-   Evaluate instruction compliance independently from factual correctness

## Evaluation level

This evaluator operates at the **OUTPUT\_LEVEL**, scoring a single agent response per case.

## Parameters

### `rubric` (optional)

-   **Type**: `str | None`
-   **Default**: `INSTRUCTION_FOLLOWING_RUBRIC_V0`
-   **Description**: Custom rubric. Leave unset to use the default rubric.

### `model` (optional)

-   **Type**: `Model | str | None`
-   **Default**: `None` (uses default Bedrock model)
-   **Description**: Multimodal judge model.

### `include_inputs` (optional)

-   **Type**: `bool`
-   **Default**: `True`

### `system_prompt` (optional)

-   **Type**: `str | None`
-   **Default**: `None` (uses the built-in `MLLM_JUDGE_SYSTEM_PROMPT`)

### `reference_suffix` (optional)

-   **Type**: `str | None`
-   **Default**: `None` (uses the built-in default suffix)

### `uses_environment_state` (optional)

-   **Type**: `bool`
-   **Default**: `False`
-   **Description**: Whether to include environment state in the evaluation prompt, enabling assessment of agent side effects alongside the output.

## Scoring system

| Score | Label | Meaning |
| --- | --- | --- |
| 1.0 | Following | All explicit constraints are satisfied |
| 0.0 | Not Following | One or more constraints are violated |

A response passes only if the score is `1.0`.

## Basic usage

```python
import asyncio

from strands_evals import Case, Experiment
from strands_evals.evaluators import MultimodalInstructionFollowingEvaluator
from strands_evals.types import MultimodalInput
from strands_evals.types.evaluation_report import EvaluationReport


def task_function(case: Case) -> str:
    # Replace with your multimodal agent invocation.
    return "- tree\n- bench\n- lamppost"


cases = [
    Case(
        name="bullet-format",
        input=MultimodalInput(
            media="/path/to/park.jpg",
            instruction="List exactly three objects visible in the background as bullet points.",
        ),
    ),
]

experiment = Experiment(
    cases=cases,
    evaluators=[MultimodalInstructionFollowingEvaluator()],
)

async def main():
    report = await experiment.run_evaluations_async(task_function)
    report.run_display()

asyncio.run(main())
```

## Combining with other evaluators

Pair with correctness and faithfulness to assess different failure modes separately. `Experiment.run_evaluations` returns one combined report across all evaluators. Each row in `report.cases` carries an `evaluator` key naming the producing evaluator:

```python
from strands_evals import Experiment
from strands_evals.evaluators import (
    MultimodalCorrectnessEvaluator,
    MultimodalFaithfulnessEvaluator,
    MultimodalInstructionFollowingEvaluator,
)
from strands_evals.types.evaluation_report import EvaluationReport

evaluators = [
    MultimodalInstructionFollowingEvaluator(),  # Did it follow the instruction constraints?
    MultimodalCorrectnessEvaluator(),           # Are the listed objects correct?
    MultimodalFaithfulnessEvaluator(),          # Are they actually in the image?
]

experiment = Experiment(cases=cases, evaluators=evaluators)

async def main():
    report = await experiment.run_evaluations_async(task_function)
    report.run_display()

asyncio.run(main())
```

## Related evaluators

-   [**MultimodalOutputEvaluator**](/docs/user-guide/evals-sdk/evaluators/multimodal_output_evaluator/index.md): Parent class with full parameter reference
-   [**InstructionFollowingEvaluator**](/docs/user-guide/evals-sdk/evaluators/instruction_following_evaluator/index.md): Text-only counterpart

## Related pages

- [Multimodal correctness evaluator](/docs/user-guide/evals-sdk/evaluators/multimodal_correctness_evaluator/index.md) (2 shared tags)
- [Multimodal faithfulness evaluator](/docs/user-guide/evals-sdk/evaluators/multimodal_faithfulness_evaluator/index.md) (2 shared tags)
- [Multimodal output evaluator](/docs/user-guide/evals-sdk/evaluators/multimodal_output_evaluator/index.md) (2 shared tags)
- [Multimodal overall quality evaluator](/docs/user-guide/evals-sdk/evaluators/multimodal_overall_quality_evaluator/index.md) (2 shared tags)
- [Google](/docs/user-guide/sdk/model-providers/google/index.md) (1 shared tag)
- [Vercel](/docs/user-guide/sdk/model-providers/vercel/index.md) (1 shared tag)
- [OpenAI](/docs/user-guide/sdk/model-providers/openai/index.md) (1 shared tag)
- [Writer](/docs/user-guide/sdk/model-providers/writer/index.md) (1 shared tag)
- [Amazon Nova](/docs/user-guide/sdk/model-providers/amazon-nova/index.md) (1 shared tag)
- [Amazon Bedrock](/docs/user-guide/sdk/model-providers/amazon-bedrock/index.md) (1 shared tag)
