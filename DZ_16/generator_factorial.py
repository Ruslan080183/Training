from functools import reduce
def factorial_generator(number: int) -> int:
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
        yield factorial

def factorial_generator_reduce(number1: int) -> int:
    factorial1 = reduce(lambda x, y: x * y, range(1, number1 + 1))
    return factorial1




