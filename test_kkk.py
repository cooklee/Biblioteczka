import pytest
from testowanie import get_initials


def div(a, b):
    print('kotki')


Parameters = [
    ("Sławomir Bogusławski", "SB"),
    ("Krzysztof Bogusławski", "KB"),
    ("Krzysztof Gosia Bogusławski", "KGB"),
    ("B G A Bogusławski", "BGAB"),
]


@pytest.mark.parametrize("value, expected", Parameters)
def test_get_initial_SB(value, expected):
    assert get_initials(value) == expected


def test_cos_cos_tam():
    assert True




def test_div_cos_tam():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
