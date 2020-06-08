def main():
    class SimpleChattyBot:
        user_name: str = ""
        user_age: int = 0

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
            SimpleChattyBot.user_name = user_name
            print(f"What a great name you have, {SimpleChattyBot.user_name}!")

        def guess_age(self, r3, r5, r7):
            SimpleChattyBot.user_age = (r3 * 70 + r5 * 21 + r7 * 15) % 105
            print(f"Your age is {SimpleChattyBot.user_age}; that's a good time to start programming!")

    my_chatty_bot = SimpleChattyBot("Aid", 2020)

    my_chatty_bot.hello()

    name: str = input("Please, remind me your name. \n"
                      "> ")
    my_chatty_bot.greeting_user(name)

    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder_3: int = int(input("> "))
    remainder_5: int = int(input("> "))
    remainder_7: int = int(input("> "))
    my_chatty_bot.guess_age(remainder_3, remainder_5, remainder_7)


if __name__ == "__main__":
    main()
