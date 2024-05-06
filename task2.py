import re

from typing import Callable


def generator_numbers(text: str):
    pattern = r"\d+\.\d+"
    elements = re.findall(pattern, text)
    for element in elements:
        yield element


def sum_profit(text: str, func: Callable):
    generator = func(text)
    summa = 0
    for number in generator: 
        summa += float(number)
    return summa


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
