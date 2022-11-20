def letter_equality(text: str, letter1="x", letter2="o") -> bool:
    i = 0
    for c in text:
        if c == letter1 in text or c == letter1.lower() in text or c == letter1.title() in text:
         i += 1
    i2 = 0
    for p in text:
        if p == letter2 in text or p == letter2.lower() in text or p == letter2.title() in text:
         i2 += 1
    if i == i2:
          result = True
    else:
         result = False

    return result
print(letter_equality("xxooO", "x", "O"))