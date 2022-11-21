def min_word(text: str) -> int:
    text1 = text.split()
    a = []
    for i in text1:
      a.append(len(i))
    return min(a)
print(min_word("В этой строке минимальное количество букв в слове"))
