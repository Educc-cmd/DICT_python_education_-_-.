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
        guess = input("Введіть літери: > ")

        if guess in guessed_letters:
            print("Літера вже використана")
            attempts -= 1
        else:
            guessed_letters.add(guess)

            if guess in secret_word:
                found_improvement = False
                for i, letter in enumerate(secret_word):
                    if letter == guess and guessed_word[i] == "-":
                        guessed_word[i] = guess
                        found_improvement = True
                if not found_improvement:
                    print("У цьому слові відсутні наступні літери")
                    attempts -= 1
            else:
                print("Спробуй іншу літеру")
                attempts -= 1

        if "".join(guessed_word) == secret_word:
            print("\n" + secret_word)
            print("Ви вгадали слово!")
            print("Ти вижив!")
            return

    print("Ти програв!")
    print("Дякую за гру!")
    print("Побачимо, наскільки добре ви впоралися з завданням на наступному етапі.")

play()