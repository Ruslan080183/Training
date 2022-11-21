def prime_number(number: int) -> bool:
   subsequence = range(2, number)
   i = 0
   for num in subsequence:
       if number % num == 0:
           i += 1
       if i <= 0:
             result = True
       else:
             result = False

   return result
print(prime_number(13))