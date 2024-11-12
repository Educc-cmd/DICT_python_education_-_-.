def d_s():
    print("HANGMAN")
    print("The game will be available soon.")

d_s()

import random


def play():
    print("HANGMAN")
    words = ['python', 'java', 'javascript', 'php']
    secret_word = random.choice(words)
    guessed_word = ["-"] * len(secret_word)
    attempts = 8
    guessed_letters = set()

    while attempts > 0:
        print("\n" + "".join(guessed_word))
        guess = input("Введіть букву: > ")

        if guess in guessed_letters:
            print("Ви вже вгадали букву")
        else:
            guessed_letters.add(guess)

            if guess in secret_word:
                for i, letter in enumerate(secret_word):
                    if letter == guess:
                        guessed_word[i] = guess
            else:
                attempts -= 1
                print("Такої літери немає в данному слові")

        if "".join(guessed_word) == secret_word:
            print("\n" + secret_word)
            print("Ти вгадав!")
            return

    print("Ти програв!")
    print("Дякую за гру!")
    print("Наступне завдання буде важче :).")

play()