class Robot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def move(self, commands: str):
        new_x = self.x
        new_y = self.y
        for command in commands:
            match command:
                case "N":
                  new_y += 1
                  if new_y not in range(0, 101):
                      return print("Robot can't move in this way!")
                case "S":
                  new_y -= 1
                  if new_y not in range(0, 101):
                      return print("Robot can't move in this way!")
                case "E":
                    new_x += 1
                    if new_x not in range(0, 101):
                        return print("Robot can't move in this way!")
                case "W":
                    new_x -= 1
                    if new_x not in range(0, 101):
                        return print("Robot can't move in this way!")

        self.x = new_x
        self.y = new_y
        return print(F"x = {self.x}, y = {self.y}")
