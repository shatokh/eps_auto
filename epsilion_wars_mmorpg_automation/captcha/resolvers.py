"""Captcha resolve methods."""

from dataclasses import dataclass
from typing import Callable

from telethon import events

from epsilion_wars_mmorpg_automation.captcha.simple_math import simple_math


@dataclass
class CaptchaAnswer:
    """Captcha answer type."""

    resolver_type: str
    question: str
    answer: str | None = None


def try_resolve(event: events.NewMessage.Event) -> CaptchaAnswer:
    """Try to resolve captcha."""
    resolvers_enabled: list[Callable] = [
        simple_math,
    ]

    for resolver in resolvers_enabled:
        answer_str = resolver(event.message.message)
        if answer_str:
            return CaptchaAnswer(
                resolver_type=resolver.__name__,
                question=event.message.message,
                answer=answer_str,
            )

    return CaptchaAnswer(resolver_type='', question=event.message.message, answer=None)
