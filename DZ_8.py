def camel_case(string: str) -> str:
    string_title = string.title()[1:-1]
    if len(string) == 0:
        return "Error"
    return print(string[0] + string_title.replace("-", "").replace("_", ""))



def palindromeD_Z(num: int) -> int:
 i = num + 1
 if num <= 999:
  while str(i)[0] != str(i)[-1]:
      i += 1
 elif num >= 1000:
   while str(i)[0] != str(i)[-1] or str(i)[1] != str(i)[2]:
      i += 1
 return print(i)

def get_digit(word: str) -> int or None:
    for symbol in word:
        if symbol.isdigit():
            return int(symbol)
    return None
def order(array: str) -> str:
    return " ".join(sorted(array.split(), key=get_digit))















