The `MultimodalCorrectnessEvaluator` assesses whether an agent response is factually correct given the image content. It catches errors in objects, counts, colors, positions, readable text, and described actions.

## Key features

-   **Output-Level Evaluation**: Scores a single agent response per case
-   **Binary Scoring**: `1.0` for correct, `0.0` if any factual error is found
-   **Automatic Reference Comparison**: Appends a reference suffix to the rubric when `expected_output` is provided on the case
-   **Fact-Checking Focus**: Designed to catch factual errors in image descriptions and VQA answers

## When to use

Use the `MultimodalCorrectnessEvaluator` when you need to:

-   Verify factual accuracy of image captions, VQA answers, or chart/document QA responses
-   Measure exact correctness on benchmark tasks with a known answer
-   Catch small but important errors (off-by-one counts, wrong colors, misread text)

## Evaluation level

This evaluator operates at the **OUTPUT\_LEVEL**, scoring a single agent response per case.

## Parameters

### `rubric` (optional)

-   **Type**: `str | None`
-   **Default**: `CORRECTNESS_RUBRIC_V0`
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
-   **Description**: Override to customize reference-based grading.

### `uses_environment_state` (optional)

-   **Type**: `bool`
-   **Default**: `False`
-   **Description**: Whether to include environment state in the evaluation prompt, enabling assessment of agent side effects alongside the output.

## Scoring system

| Score | Label | Meaning |
| --- | --- | --- |
| 1.0 | Correct | No factual errors found |
| 0.0 | Incorrect | One or more factual errors found |

A response passes only if the score is `1.0`.

## Basic usage

### Reference-Free (fact-check against the image)

```python
import asyncio

from strands_evals import Case, Experiment
from strands_evals.evaluators import MultimodalCorrectnessEvaluator
from strands_evals.types import MultimodalInput
from strands_evals.types.evaluation_report import EvaluationReport


def task_function(case: Case) -> str:
    # Replace with your multimodal agent invocation.
    return "There are 3 people sitting on the red couch."


cases = [
    Case(
        name="scene-count",
        input=MultimodalInput(
            media="/path/to/living_room.jpg",
            instruction="How many people are on the couch and what color is it?",
        ),
    ),
]

experiment = Experiment(cases=cases, evaluators=[MultimodalCorrectnessEvaluator()])

async def main():
    report = await experiment.run_evaluations_async(task_function)
    report.run_display()

asyncio.run(main())
```

### Reference-Based (compare against a known answer)

```python
cases = [
    Case(
        name="chart-value",
        input=MultimodalInput(
            media="/path/to/revenue_chart.png",
            instruction="What is the Q3 revenue for Product A?",
        ),
        expected_output="$4.2M",
    ),
]

experiment = Experiment(cases=cases, evaluators=[MultimodalCorrectnessEvaluator()])

async def main():
    report = await experiment.run_evaluations_async(task_function)

asyncio.run(main())
```

When `expected_output` is set, the evaluator automatically appends the reference suffix so the judge compares the response to the reference answer.

## Related evaluators

-   [**MultimodalOutputEvaluator**](/docs/user-guide/evals-sdk/evaluators/multimodal_output_evaluator/index.md): Parent class with full parameter reference
-   [**MultimodalFaithfulnessEvaluator**](/docs/user-guide/evals-sdk/evaluators/multimodal_faithfulness_evaluator/index.md): Catches hallucinations (claims not verifiable from the image)
-   [**CorrectnessEvaluator**](/docs/user-guide/evals-sdk/evaluators/correctness_evaluator/index.md): Text-only counterpart

## Related pages

- [Multimodal faithfulness evaluator](/docs/user-guide/evals-sdk/evaluators/multimodal_faithfulness_evaluator/index.md) (2 shared tags)
- [Multimodal instruction following evaluator](/docs/user-guide/evals-sdk/evaluators/multimodal_instruction_following_evaluator/index.md) (2 shared tags)
- [Multimodal output evaluator](/docs/user-guide/evals-sdk/evaluators/multimodal_output_evaluator/index.md) (2 shared tags)
- [Multimodal overall quality evaluator](/docs/user-guide/evals-sdk/evaluators/multimodal_overall_quality_evaluator/index.md) (2 shared tags)
- [Google](/docs/user-guide/sdk/model-providers/google/index.md) (1 shared tag)
- [Vercel](/docs/user-guide/sdk/model-providers/vercel/index.md) (1 shared tag)
- [OpenAI](/docs/user-guide/sdk/model-providers/openai/index.md) (1 shared tag)
- [Writer](/docs/user-guide/sdk/model-providers/writer/index.md) (1 shared tag)
- [Amazon Nova](/docs/user-guide/sdk/model-providers/amazon-nova/index.md) (1 shared tag)
- [Amazon Bedrock](/docs/user-guide/sdk/model-providers/amazon-bedrock/index.md) (1 shared tag)
