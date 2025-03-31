import math
import statistics
from typing import Union, List

def add(a: Union[int, float], b: Union[int, float]) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Оба аргумента должны быть числами")
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Оба аргумента должны быть числами")
    return a - b

def multiply(a: Union[int, float], b: Union[int, float]) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Оба аргумента должны быть числами")
    return a * b

def divide(a: Union[int, float], b: Union[int, float]) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Оба аргумента должны быть числами")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b

def power(base: Union[int, float], exponent: Union[int, float]) -> float:
    if not (isinstance(base, (int, float)) and isinstance(exponent, (int, float))):
        raise TypeError("Основание и показатель степени должны быть числами")
    return base ** exponent

def factorial(num: int) -> int:
    if not isinstance(num, int):
        raise TypeError("Аргумент должен быть целым числом")
    if num < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    return math.factorial(num)

print("Калькулятор запущен. Для выхода введите 'exit'.")

while True:
    print("\nДоступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    #print("4. Деление")
    #print("5. Возведение в степень")
    #print("6. Факториал")
    #print("7. Синус")
    #print("8. Медиана")

    if not choice.isdigit() or not 1 <= int(choice) <= 8:
        print("Ошибка: введите число от 1 до 8 или 'exit'.")
        continue

    try:
        choice_num = int(choice)
        if choice_num == 1:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            result = add(a, b)
        elif choice_num == 2:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            result = subtract(a, b)
        elif choice_num == 3:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            result = multiply(a, b)
        elif choice_num == 4:
            a = float(input("Введите делимое: "))
            b = float(input("Введите делитель: "))
            result = divide(a, b)
