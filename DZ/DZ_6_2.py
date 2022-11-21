def minmax(number: str) -> int:
   number1 = number.split()
   number2 = list(map(int, number1))
   return print(F" max = {max(number2)}, min = {min(number2)}")
minmax("-1 -2 -3 -100")
