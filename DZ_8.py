def camel_case(string: str) -> str:
    string_title = string.title()[0:-1]
    return print(string_title.replace("-", ""))


def palindromeD_Z(num: int) -> int:
 i = num + 1
 if num <= 999:
  while str(i)[0] != str(i)[-1]:
      i += 1
 elif num >=1000:
   while str(i)[0] != str(i)[-1] or str(i)[1] != str(i)[2]:
      i += 1
 return print(i)













