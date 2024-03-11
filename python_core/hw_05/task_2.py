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
