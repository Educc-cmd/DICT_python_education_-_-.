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
        guess = input("Введіть летеру: > ")

        if len(guess) != 1:
            print("Ви повинні ввести одну літеру")
            continue

        if not guess.isalpha() or not guess.islower():
            print("Будь ласка, введіть малу англійську літеру")
            continue

        if guess in guessed_letters:
            print("Ви вже здогадалися, що це за літера")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print("Ця буква не з'являється в слові")
            attempts -= 1

        if "".join(guessed_word) == secret_word:
            print(f"\nYou guessed the word {secret_word}!")
            print("Ти вижив!")
            return

    print("Ти програв!")
    print("Дякую за гру!")
    print("Побачимо, наскільки добре ви впоралися з завданням на наступному етапі.")

play()