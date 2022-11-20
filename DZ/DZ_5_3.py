def word_isogram(word: str) -> str:
    if len(set(word.lower())) == len(list(word.lower())):
        a = print(f"Слово {word} является изограммой")
    elif len(set(word.lower())) != len(list(word.lower())):
        a = print(f"Слово {word} не является изограммой")
    return a


word_isogram("ФкеЛД")