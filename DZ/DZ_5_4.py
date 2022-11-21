from random import randint
from collections import Counter
def random_list(start: int, end: int, count: int) -> list:
    random_list1 = []
    for _ in range(count):
        random_list1.append(randint(start, end))
    return random_list1


def count_same(n: list) -> dict:
    lst1 = []
    for num in n:
        if n.count(num) > 1:
            lst1.append(num)
    lst2 = []
    for a in set(lst1):
        if a in lst1:
            lst2.append(lst1.count(a))
    e = set(lst1)
    r = list(e)
    c = dict(zip(e, lst2))
    return c
print(count_same(random_list(1,20,20)))
