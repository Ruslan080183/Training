def least_common(a: int, b: int) -> int:
   c = 1
   while c % a != 0 or c % b != 0:
      c += 1
   return c
print(least_common(5,6))

def least_common1(a: int, b = 5 ) -> int:
   c = 1
   while c % a != 0 or c % b != 0:
      c += 1
   return c
print(least_common1(2))