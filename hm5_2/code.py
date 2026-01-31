import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генеруємо всі дійсні числа з тексту, що записані через пробіли
    """
    pattern = r" \d+\.\d+ "

    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
 
    #Обчислюємо суму всіх дійсних чисел у тексті
    
    return sum(func(text))


#Перевірка
text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими надходженнями "
    "27.45 і 324.00 доларів."
)

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")