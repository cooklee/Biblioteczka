import pytest

from functions import div, analyze_pesel


@pytest.mark.parametrize("a,b,result", [
    (1, 1, 1),
    (1, 2, 0.5),
    (0, 1, 0),
    ('0', '1', 0),
])
def test_div(a, b, result):
    assert div(a, b) == result


def test_div_raises_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


@pytest.mark.parametrize('pesel, is_valid', [
    ("88071613927", True),
    ("86070279937", True),
    ("92061889573", True),
    ("86041974982", True),
    ("68082531797", True),
    ("85032578828", True),
    ("75080664881", False),
    ("57040936621", False),
    ("79111649771", False),

    ("49031198651", False),
])
def test_analyze_pesel_is_valid(pesel, is_valid):
    assert analyze_pesel(pesel)['valid'] == is_valid


@pytest.mark.parametrize('pesel, is_valid', [
    ('14283182599', True),
    ('16233179646', True),
    ('06322945179', True),
    ('07282994937', True),
    ('03261556244', True),
    ('19301339955', True),
    ('03212918321', True),
    ('08222213385', True),
    ('01242515695', True),
    ('10310743645', True)])
def test_analyze_pesel_is_valid_after_2000(pesel, is_valid):
    assert analyze_pesel(pesel)['valid'] == is_valid


@pytest.mark.parametrize('pesel, gender', [
    ('83091238491', 'male'),
    ('76022754195', 'male'),
    ('63032966157', 'male'),
    ('48021235919', 'male'),
    ('98080684814', 'male'),
    ('72101119817', 'male'),
    ('48082832333', 'male'),
    ('81112243536', 'male'),
    ('87080545254', 'male'),
    ('61041029535', 'male')])
def test_analyze_pesel_correct_sex(pesel, gender):
    assert analyze_pesel(pesel)['gender'] == gender
