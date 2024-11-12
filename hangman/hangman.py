def d_s():
    print("HANGMAN")
    print("The game will be available soon.")

d_s()

import random

def play():
    print("HANGMAN")
    words = ['python', 'java', 'javascript', 'php']
    secret_word = random.choice(words)
    guess = input("Спробуй вгадати слово: > ")

    if guess.lower() == secret_word:
        print("Ти вгадав!")
    else:
        print("Спробуй ще раз!")

play()
