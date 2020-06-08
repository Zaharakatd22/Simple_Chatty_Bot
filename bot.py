def main():
    class SimpleChattyBot:
        def __init__(self, name: str, birth_year: int):
            self.name: str = name
            self.birth_year: int = birth_year

        def __repr__(self):
            return f"Simple Chatty Bot, name: {self.name}, {self.birth_year}"

        def __str__(self):
            return f"The simple chatty bot {self.name}, his birth year is {self.birth_year}"

        def hello(self):
            print(f"Hello! My name is {self.name} \n"
                  f"I was create in {self.birth_year}")

    my_chatty_bot = SimpleChattyBot("Aid", 2020)

    my_chatty_bot.hello()


if __name__ == "__main__":
    main()