import re
from typing import Callable

# Функція генератор яка знаходить усі дійсні числа
def generator_numbers(text : str):
    pattern = r'\d+\.\d+'
    numbers = re.findall(pattern, text)
    for item in  numbers:
        yield item 

# Функція яка вираховую суму усіх дійсних чисел у тексті
def sum_profit(text : str, generator_numbers: Callable):
    suma = 0
    for numb in generator_numbers(text):
        suma += float(numb)
    return suma


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")