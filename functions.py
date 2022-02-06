from datetime import datetime
from random import randint


def div(a, b):
    return float(a) / float(b)


def gen_month_number(value):
    min = 20
    amount = 0
    value = int(value)
    while value > 12:
        value -= min
        amount += min
    year = {
        20: '20',
        40: '21',
        60: '22',
        80: '18',
        0:'19',
    }
    return year[amount], value


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9,
               1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[: -1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2 != 0 else "female"
    year, month_number = gen_month_number(pesel[2:4])
    birth_date = datetime(int(year + pesel[0: 2]), int(month_number), int(pesel[4:6]))
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
    }
    return result
