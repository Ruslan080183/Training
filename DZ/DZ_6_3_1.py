def letter_number(textengl: str) -> str:

 a = "abcdefghijklmnopqrstuvwxyz"
 c = []
 for i in textengl.lower():
      if i in a:
        c.append(a.index(i) + 1)
 return print((" ".join(map(str, c))))

letter_number("The sunset sets at twelve o' clock.")