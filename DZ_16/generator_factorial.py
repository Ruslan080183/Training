def factorial_generator(number: int) -> int:
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
        yield factorial

