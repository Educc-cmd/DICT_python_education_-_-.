import random

def get_pencils():
    while True:
        user_input = input("Скільки олівців ви хотіли б використати:\n> ")
        if not user_input.isdigit():
            print("Кількість олівців має бути числовою")
        else:
            pencils = int(user_input)
            if pencils <= 0:
                print("Кількість олівців має бути додатною")
            else:
                return pencils

def get_first_player(player1, player2):
    while True:
        first_player = input(f"Хто буде першим ({player1}, {player2}):\n> ")
        if first_player not in [player1, player2]:
            print(f"Обирайте між '{player1}' і '{player2}'")
        else:
            return first_player

def player_turn(name, pencils):
    while True:
        try:
            take = int(input(f"{name} черга:\n> "))
            if take not in [1, 2, 3]:
                print("Можливі значення: '1', '2' or '3'")
            elif take > pencils:
                print("Занадто багато олівців було взято")
            else:
                return take
        except ValueError:
            print("Можливі значення: '1', '2' або '3'")

def bot_turn(name, pencils):
    if pencils % 4 == 0:
        take = 3
    elif pencils % 4 == 3:
        take = 2
    elif pencils % 4 == 2:
        take = 1
    else:
        take = random.randint(1, min(3, pencils))
    print(f"{name} черга:\n{take}")
    return take

def main():
    pencils = get_pencils()

    player1 = "John"
    player2 = "Jack"
    current_player = get_first_player(player1, player2)

    while pencils > 0:
        print("|" * pencils)

        if current_player == player2:
            take = bot_turn(player2, pencils)
        else:
            take = player_turn(player1, pencils)

        pencils -= take

        if pencils == 0:
            print(f"{current_player} виграв!")
            break

        current_player = player1 if current_player == player2 else player2

if __name__ == "__main__":
    main()