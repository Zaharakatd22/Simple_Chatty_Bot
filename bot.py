def main():
    class SimpleChattyBot:
        def __init__(self, bot_name: str, bot_birth_year: int):
            self.bot_name: str = bot_name
            self.bot_birth_year: int = bot_birth_year

        def __repr__(self):
            return f"Simple Chatty Bot, name: {self.bot_name}, {self.bot_birth_year}"

        def __str__(self):
            return f"The simple chatty bot {self.bot_name}, his birth year is {self.bot_birth_year}"

        def hello(self):
            print(f"Hello! My name is {self.bot_name} \n"
                  f"I was create in {self.bot_birth_year}")

        def greeting_user(self, user_name: str):
            print(f"What a great name you have, {user_name}!")

    my_chatty_bot = SimpleChattyBot("Aid", 2020)

    my_chatty_bot.hello()

    name: str = input("Please, remind me your name. \n"
                      "> ")
    my_chatty_bot.greeting_user(name)


if __name__ == "__main__":
    main()
