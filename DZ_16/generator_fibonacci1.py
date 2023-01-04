import sys

fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1


def fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    yield a

print(sys.getsizeof(fib()))
print(sys.getsizeof(fibonacci()))