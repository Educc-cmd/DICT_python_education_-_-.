def d_s():
    print("HANGMAN")
    print("The game will be available soon.")

d_s()

def play():
    print("HANGMAN")
    secret_word = "python"
    guess = input("Спробуй вгадати слово: > ")

    if guess.lower() == secret_word:
        print("Ти вгадав!")
    else:
        print("Спробуй ще раз!")

d_s()
play()
