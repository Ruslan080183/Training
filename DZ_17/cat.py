class Cat:
    counter = False
    moor_counter = 0
    meow_counter = 0

    def __init__(self, nickname: str):
        self.nickname = nickname

    def to_answer(self):
        if Cat.counter:
            Cat.moor_counter += 1
            Cat.counter = False
            return print(f"{self.nickname} moor")
        else:
            Cat.meow_counter += 1
            Cat.counter = True
            return print(f"{self.nickname} meow")

    @staticmethod
    def count_moor():
        return Cat.moor_counter

    @staticmethod
    def count_meow():
        return Cat.meow_counter

