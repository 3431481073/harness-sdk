"""System One decision model tests — the behavioral spec shared by both providers."""

import json
from dataclasses import dataclass
from typing import Any

import httpx
import pytest

from strands.decisions import DecisionModel, DecisionsAPIDecisionModel, TypeSafeDecisionModel, Uncertain
from strands.types.exceptions import (
    ContextWindowOverflowException,
    ModelThrottledException,
    StructuredOutputException,
)

_SENTINEL = object()


@dataclass
class _ProviderCase:
    name: str
    model_cls: type[DecisionModel]
    endpoint: str
    default_model_id: str
    provider_name: str
    api_key_env: str


_PROVIDERS = [
    _ProviderCase(
        name="TypeSafeDecisionModel",
        model_cls=TypeSafeDecisionModel,
        endpoint="https://api.typesafe.ai/v1/systemone",
        default_model_id="jev-latest",
        provider_name="typesafe",
        api_key_env="TYPESAFE_API_KEY",
    ),
    _ProviderCase(
        name="DecisionsAPIDecisionModel",
        model_cls=DecisionsAPIDecisionModel,
        endpoint="https://decisionapi.net/v1/systemone",
        default_model_id="~typesafe/jev-latest",
        provider_name="decisionsApi",
        api_key_env="JEV_API_KEY",
    ),
]

_PROVIDER_IDS = [case.name for case in _PROVIDERS]


def _response_body(answers: dict[str, Any], usage: Any = _SENTINEL) -> dict[str, Any]:
    if usage is _SENTINEL:
        usage = {"input_tokens": 12, "output_tokens": 3}
    return {"model": "resolved-model", "answers": answers, "usage": usage}


def _fake_client(payload: Any, *, status: int = 200, captured: list[httpx.Request] | None = None) -> httpx.AsyncClient:
    def handler(request: httpx.Request) -> httpx.Response:
        if captured is not None:
            captured.append(request)
        return httpx.Response(status, json=payload)

    return httpx.AsyncClient(transport=httpx.MockTransport(handler))


def _request_body(request: httpx.Request) -> dict[str, Any]:
    return json.loads(request.content)


@pytest.fixture(autouse=True)
def _clear_provider_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for case in _PROVIDERS:
        monkeypatch.delenv(case.api_key_env, raising=False)


@pytest.mark.parametrize("provider", _PROVIDERS, ids=_PROVIDER_IDS)
class TestAsk:
    @pytest.mark.asyncio
    async def test_maps_questions_and_returns_typed_answers_with_confidence_metadata(self, provider: _ProviderCase):
        captured: list[httpx.Request] = []
        client = _fake_client(
            _response_body(
                {
                    "urgent": {"type": "noul", "noul": 0.9},
                    "department": {
                        "type": "choice",
                        "choice": "billing",
                        "probabilities": {"billing": 0.7, "support": 0.2, "sales": 0.1},
                        "confidence": 0.55,
                    },
                }
            ),
            captured=captured,
        )
        decision = provider.model_cls(api_key="test-key", http_client=client)

        result = await decision.ask(
            "Refund this today",
            {
                "urgent": {"question": "Is this urgent?", "choices": "boolean"},
                "department": {
                    "question": "Which team should handle this?",
                    "choices": ["billing", "support", "sales"],
                },
            },
        )

        assert str(captured[0].url) == provider.endpoint
        assert captured[0].headers["authorization"] == "Bearer test-key"
        assert captured[0].headers["content-type"] == "application/json"
        assert _request_body(captured[0]) == {
            "state": "Refund this today",
            "model": provider.default_model_id,
            "questions": {
                "urgent": {"type": "noul", "instructions": "Is this urgent?"},
                "department": {
                    "type": "choice",
                    "instructions": "Which team should handle this?",
                    "criteria": {"billing": None, "support": None, "sales": None},
                },
            },
        }

        assert result.answers == {"urgent": True, "department": "billing"}
        assert result.usage == {"inputTokens": 12, "outputTokens": 3, "totalTokens": 15}
        assert result.metadata.latency_ms >= 0
        assert result.metadata.provider_name == provider.provider_name
        assert result.metadata.model_id == "resolved-model"
        assert result.metadata.probabilities == {
            "urgent": pytest.approx({"true": 0.9, "false": 0.1}),
            "department": pytest.approx({"billing": 0.7, "support": 0.2, "sales": 0.1}),
        }
        assert result.metadata.confidence == {"urgent": pytest.approx(0.8), "department": pytest.approx(0.55)}

    @pytest.mark.asyncio
    async def test_applies_the_provider_wide_default_minimum_confidence(self, provider: _ProviderCase):
        client = _fake_client(_response_body({"q": {"type": "noul", "noul": 0.625}}))
        decision = provider.model_cls(api_key="test-key", http_client=client)

        result = await decision.ask("state", {"q": {"question": "ok?", "choices": "boolean"}})

        assert result.answers == {"q": Uncertain()}
        assert result.metadata.confidence == {"q": pytest.approx(0.25)}

    @pytest.mark.asyncio
    async def test_applies_override_default_and_disabled_uncertainty_in_precedence_order(self, provider: _ProviderCase):
        client = _fake_client(
            _response_body(
                {
                    "providerDefault": {"type": "noul", "noul": 0.8},
                    "questionOverride": {"type": "noul", "noul": 0.8},
                    "disabled": {"type": "noul", "noul": 0.5},
                }
            )
        )
        decision = provider.model_cls(api_key="test-key", default_min_confidence=0.7, http_client=client)

        result = await decision.ask(
            "state",
            {
                "providerDefault": {"question": "default?", "choices": "boolean"},
                "questionOverride": {
                    "question": "override?",
                    "choices": "boolean",
                    "uncertainty": {"min_confidence": 0.5},
                },
                "disabled": {"question": "forced?", "choices": "boolean", "uncertainty": False},
            },
        )

        assert result.answers == {"providerDefault": Uncertain(), "questionOverride": True, "disabled": True}
        assert result.metadata.confidence == {
            "providerDefault": pytest.approx(0.6),
            "questionOverride": pytest.approx(0.6),
            "disabled": pytest.approx(0.0),
        }

    @pytest.mark.asyncio
    async def test_thresholds_choice_answers_on_provider_confidence_with_overrides(self, provider: _ProviderCase):
        answer = {"type": "choice", "choice": "a", "probabilities": {"a": 0.9, "b": 0.1}, "confidence": 0.65}
        client = _fake_client(_response_body({"providerDefault": answer, "questionOverride": answer}))
        decision = provider.model_cls(api_key="test-key", default_min_confidence=0.7, http_client=client)

        result = await decision.ask(
            "state",
            {
                "providerDefault": {"question": "pick?", "choices": ["a", "b"]},
                "questionOverride": {
                    "question": "pick?",
                    "choices": ["a", "b"],
                    "uncertainty": {"min_confidence": 0.6},
                },
            },
        )

        assert result.answers == {"providerDefault": Uncertain(), "questionOverride": "a"}
        assert result.metadata.confidence == {
            "providerDefault": pytest.approx(0.65),
            "questionOverride": pytest.approx(0.65),
        }

    @pytest.mark.asyncio
    async def test_projects_messages_without_internal_tracking_ids_or_metadata(self, provider: _ProviderCase):
        captured: list[httpx.Request] = []
        client = _fake_client(_response_body({"q": {"type": "noul", "noul": 1}}), captured=captured)
        decision = provider.model_cls(api_key="test-key", http_client=client)
        message = {
            "role": "user",
            "content": [{"text": "hello"}],
            "tracking_id": "internal-id",
            "metadata": {"custom": {"private": "framework-value"}},
        }

        await decision.ask([message], {"q": {"question": "Greeting?", "choices": "boolean"}})

        assert _request_body(captured[0])["state"] == [{"role": "user", "content": [{"text": "hello"}]}]

    @pytest.mark.asyncio
    async def test_rejects_binary_content_blocks_before_sending(self, provider: _ProviderCase):
        captured: list[httpx.Request] = []
        client = _fake_client(_response_body({}), captured=captured)
        decision = provider.model_cls(api_key="test-key", http_client=client)
        image = {"image": {"format": "png", "source": {"bytes": b"\x01\x02\x03"}}}

        with pytest.raises(ValueError, match="do not support binary ContentBlock state"):
            await decision.ask([image], {"q": {"question": "What is shown?", "choices": "boolean"}})
        assert captured == []

    @pytest.mark.asyncio
    async def test_honors_an_explicit_model_id(self, provider: _ProviderCase):
        captured: list[httpx.Request] = []
        client = _fake_client(_response_body({"q": {"type": "noul", "noul": 1}}), captured=captured)
        decision = provider.model_cls(api_key="test-key", model_id="pinned-model", http_client=client)

        await decision.ask("state", {"q": {"question": "ok?", "choices": "boolean"}})

        assert _request_body(captured[0])["model"] == "pinned-model"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("status", [429, 529])
    async def test_maps_throttling_statuses_to_model_throttled(self, provider: _ProviderCase, status: int):
        client = _fake_client({"error": "retry later"}, status=status)
        decision = provider.model_cls(api_key="test-key", http_client=client)

        with pytest.raises(ModelThrottledException):
            await decision.ask("state", {"q": {"question": "ok?", "choices": "boolean"}})

    @pytest.mark.asyncio
    async def test_wraps_transport_failures_with_the_original_cause(self, provider: _ProviderCase):
        def handler(request: httpx.Request) -> httpx.Response:
            raise httpx.ConnectError("offline")

        client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
        decision = provider.model_cls(api_key="test-key", http_client=client)

        with pytest.raises(StructuredOutputException) as caught:
            await decision.ask("state", {"q": {"question": "ok?", "choices": "boolean"}})
        assert isinstance(caught.value.__cause__, httpx.ConnectError)

    @pytest.mark.asyncio
    async def test_omits_usage_when_the_provider_returns_null_token_counters(self, provider: _ProviderCase):
        client = _fake_client(
            _response_body({"q": {"type": "noul", "noul": 1}}, usage={"input_tokens": None, "output_tokens": None})
        )
        decision = provider.model_cls(api_key="test-key", http_client=client)

        result = await decision.ask("state", {"q": {"question": "ok?", "choices": "boolean"}})

        assert result.usage is None

    @pytest.mark.asyncio
    async def test_rejects_an_invalid_response_model_id(self, provider: _ProviderCase):
        client = _fake_client({"model": "", "answers": {"q": {"type": "noul", "noul": 1}}})
        decision = provider.model_cls(api_key="test-key", http_client=client)

        with pytest.raises(StructuredOutputException, match="model must be a non-empty string"):
            await decision.ask("state", {"q": {"question": "ok?", "choices": "boolean"}})

    @pytest.mark.asyncio
    async def test_rejects_a_choice_answer_that_is_not_the_most_probable(self, provider: _ProviderCase):
        client = _fake_client(
            _response_body(
                {"q": {"type": "choice", "choice": "a", "probabilities": {"a": 0.4, "b": 0.6}, "confidence": 0.2}}
            )
        )
        decision = provider.model_cls(api_key="test-key", http_client=client)

        with pytest.raises(StructuredOutputException, match="must have the highest probability"):
            await decision.ask("state", {"q": {"question": "pick?", "choices": ["a", "b"]}})

    @pytest.mark.asyncio
    async def test_rejects_malformed_probability_distributions(self, provider: _ProviderCase):
        client = _fake_client(
            _response_body(
                {"q": {"type": "choice", "choice": "a", "probabilities": {"a": 0.4, "b": 0.4}, "confidence": 0.1}}
            )
        )
        decision = provider.model_cls(api_key="test-key", http_client=client)

        with pytest.raises(StructuredOutputException, match="must sum to 1"):
            await decision.ask("state", {"q": {"question": "pick?", "choices": ["a", "b"]}})

    @pytest.mark.asyncio
    async def test_rejects_more_than_255_choice_options_before_sending(self, provider: _ProviderCase):
        captured: list[httpx.Request] = []
        client = _fake_client(_response_body({}), captured=captured)
        decision = provider.model_cls(api_key="test-key", http_client=client)
        choices = [f"choice-{index}" for index in range(256)]

        with pytest.raises(ValueError, match="at most 255 choices"):
            await decision.ask("state", {"q": {"question": "pick?", "choices": choices}})
        assert captured == []

    @pytest.mark.asyncio
    async def test_serializes_the_body_as_compact_unescaped_utf8(self, provider: _ProviderCase):
        captured: list[httpx.Request] = []
        client = _fake_client(_response_body({"q": {"type": "noul", "noul": 1}}), captured=captured)
        decision = provider.model_cls(api_key="test-key", http_client=client)

        await decision.ask("caf\u00e9 \u3042", {"q": {"question": "ok?", "choices": "boolean"}})

        content = captured[0].content
        assert "caf\u00e9 \u3042".encode() in content
        assert b"\\u" not in content
        assert b", " not in content

    @pytest.mark.asyncio
    async def test_rejects_binary_nested_below_the_top_level_block(self, provider: _ProviderCase):
        captured: list[httpx.Request] = []
        client = _fake_client(_response_body({}), captured=captured)
        decision = provider.model_cls(api_key="test-key", http_client=client)
        state = [{"toolResult": {"content": [{"image": {"format": "png", "source": {"bytes": b"\x01\x02"}}}]}}]

        with pytest.raises(ValueError, match="do not support binary ContentBlock state"):
            await decision.ask(state, {"q": {"question": "ok?", "choices": "boolean"}})
        assert captured == []

    @pytest.mark.asyncio
    async def test_omits_usage_for_non_finite_token_counters(self, provider: _ProviderCase):
        body = (
            '{"model":"resolved-model","answers":{"q":{"type":"noul","noul":1}},'
            '"usage":{"input_tokens":Infinity,"output_tokens":3}}'
        )

        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(200, text=body, headers={"content-type": "application/json"})

        client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
        decision = provider.model_cls(api_key="test-key", http_client=client)

        result = await decision.ask("state", {"q": {"question": "ok?", "choices": "boolean"}})

        assert result.usage is None

    @pytest.mark.asyncio
    async def test_wraps_a_closed_client_as_structured_output_error(self, provider: _ProviderCase):
        client = _fake_client(_response_body({"q": {"type": "noul", "noul": 1}}))
        await client.aclose()
        decision = provider.model_cls(api_key="test-key", http_client=client)

        with pytest.raises(StructuredOutputException):
            await decision.ask("state", {"q": {"question": "ok?", "choices": "boolean"}})


@pytest.mark.parametrize("provider", _PROVIDERS, ids=_PROVIDER_IDS)
class TestConstruction:
    def test_requires_its_provider_specific_api_key(self, provider: _ProviderCase):
        with pytest.raises(ValueError, match=provider.api_key_env):
            provider.model_cls()

    def test_rejects_an_invalid_provider_default_threshold(self, provider: _ProviderCase):
        with pytest.raises(ValueError, match=r"default_min_confidence must be in \[0.0, 1.0\]"):
            provider.model_cls(api_key="test-key", default_min_confidence=1.1)

    def test_rejects_a_non_numeric_provider_default_threshold(self, provider: _ProviderCase):
        with pytest.raises(ValueError, match=r"default_min_confidence must be in \[0.0, 1.0\]"):
            provider.model_cls(api_key="test-key", default_min_confidence="high")

    def test_rejects_a_non_async_http_client(self, provider: _ProviderCase):
        with pytest.raises(TypeError, match="http_client must be an httpx.AsyncClient"):
            provider.model_cls(api_key="test-key", http_client=httpx.Client())


@pytest.mark.asyncio
async def test_typesafe_reads_its_api_key_from_the_environment(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("TYPESAFE_API_KEY", "typesafe-env-key")
    captured: list[httpx.Request] = []
    decision = TypeSafeDecisionModel(
        http_client=_fake_client(_response_body({"q": {"type": "noul", "noul": 1}}), captured=captured)
    )

    await decision.ask("state", {"q": {"question": "ok?", "choices": "boolean"}})

    assert captured[0].headers["authorization"] == "Bearer typesafe-env-key"


@pytest.mark.asyncio
async def test_decisions_api_reads_its_api_key_from_the_environment(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("JEV_API_KEY", "decisions-env-key")
    captured: list[httpx.Request] = []
    decision = DecisionsAPIDecisionModel(
        http_client=_fake_client(_response_body({"q": {"type": "noul", "noul": 1}}), captured=captured)
    )

    await decision.ask("state", {"q": {"question": "ok?", "choices": "boolean"}})

    assert captured[0].headers["authorization"] == "Bearer decisions-env-key"


@pytest.mark.asyncio
async def test_decisions_api_enforces_the_question_count_limit_before_sending():
    captured: list[httpx.Request] = []
    decision = DecisionsAPIDecisionModel(
        api_key="test-key", http_client=_fake_client(_response_body({}), captured=captured)
    )
    questions = {f"q{index}": {"question": f"question {index}?", "choices": "boolean"} for index in range(9)}

    with pytest.raises(ValueError, match="at most 8 questions"):
        await decision.ask("state", questions)
    assert captured == []


@pytest.mark.asyncio
async def test_decisions_api_enforces_the_request_body_limit_before_sending():
    captured: list[httpx.Request] = []
    decision = DecisionsAPIDecisionModel(
        api_key="test-key", http_client=_fake_client(_response_body({}), captured=captured)
    )

    with pytest.raises(ContextWindowOverflowException):
        await decision.ask("x" * (33 * 1024), {"q": {"question": "ok?", "choices": "boolean"}})
    assert captured == []
