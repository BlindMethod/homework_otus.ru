"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    square_numbers = [num**2 for num in args]
    return square_numbers


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num < 2:
        return False
    dealer = 2
    while num % dealer != 0: 
        dealer += 1
    if dealer == num:
        return True
    else:
        return False


def filter_numbers(numbers, refund):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if refund == ODD:
        result = [num for num in numbers if num % 2 != 0]
    elif refund == EVEN:
        result = [num for num in numbers if num % 2 == 0]
    elif refund == PRIME:    
        result = list(filter(is_prime, numbers))
    return result
