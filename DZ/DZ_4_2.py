def um_of_integers(start: int, finish: int) -> int:
    if start > finish:
        start, finish = finish, start
    subsequence = range(start, finish + 1)
    f = 0
    for number in subsequence:
        #if int(number) / float(number) == 1 :
         f += number
    return f
print(um_of_integers(10,5))
