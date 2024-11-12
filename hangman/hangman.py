def d_s():
    print("HANGMAN")
    print("The game will be available soon.")

d_s()

import random

def play():
    print("HANGMAN")
    words = ['python', 'java', 'javascript', 'php']
    secret_word = random.choice(words)
    hint = secret_word[:3] + "-" * (len(secret_word) - 3)

    print(f"Guess the word {hint}: ", end="")
    guess = input("> ")

    if guess.lower() == secret_word:
        print("Ти вгадав!")
    else:
        print("Спробуй ще раз!")

play()
