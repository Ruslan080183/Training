import sys
def finbon(n = 100) -> int:
    fib_1 = fib_2 = 1
    print(fib_1, fib_2, end=" ")
    for _ in range(2, n):
      fib_1, fib_2 = fib_2, fib_1 + fib_2
      yield print(fib_2, end=" ")
def finbon1(n = 100) -> int:
    fib_1 = fib_2 = 1
    print(fib_1, fib_2, end=" ")
    for _ in range(2, n):
      fib_1, fib_2 = fib_2, fib_1 + fib_2
      print(fib_2, end=" ")
print(F"\n{sys.getsizeof(finbon1(100))}")
print(sys.getsizeof(finbon(100)))