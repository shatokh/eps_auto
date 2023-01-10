import pytest

from app.message_parsers import parse_hp_level
from app.exceptions import InvalidMessageError


@pytest.mark.parametrize('payload,expected', [
    ('🧟‍♂Dfd 🔸9 ❤️(463/506)\n🔸 Уровень монстров: 7-10', 92),
    ('🧟‍♂Unikcname 🔸9 ❤️(509/509)\n🔸 Уровень монстров: 7-10', 100),
    ('🧟‍♂Ник ащет 🔸9 ❤️(1/509)\n🔸 Уровень монстров: 7-10', 1),
])
def test_parse_hp_level_happy_path(payload: str, expected: int):
    result = parse_hp_level(payload)

    assert result == expected


def test_parse_hp_level_not_found():
    with pytest.raises(InvalidMessageError):
        parse_hp_level('')
