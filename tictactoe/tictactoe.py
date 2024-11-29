def print_field(cells):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {cells[i]} {cells[i + 1]} {cells[i + 2]} |")
    print("---------")


def make_move(cells, player):
    while True:
        try:
            coordinates = input(f"Enter the coordinates ({player}): ").split()

            if len(coordinates) != 2:
                print("You should enter numbers!")
                continue

            x, y = map(int, coordinates)

            if not (1 <= x <= 3 and 1 <= y <= 3):
                print("Coordinates should be from 1 to 3!")
                continue

            index = (x - 1) * 3 + (y - 1)

            if cells[index] != '_':
                print("This cell is occupied! Choose another one!")
                continue

            cells = list(cells)
            cells[index] = player
            return ''.join(cells)

        except ValueError:
            print("You should enter numbers!")


def check_win(cells):
    win_combinations = [
        cells[0:3],
        cells[3:6],
        cells[6:9],
        cells[0] + cells[3] + cells[6],
        cells[1] + cells[4] + cells[7],
        cells[2] + cells[5] + cells[8],
        cells[0] + cells[4] + cells[8],
        cells[2] + cells[4] + cells[6]
    ]
    if 'XXX' in win_combinations:
        return 'X'
    elif 'OOO' in win_combinations:
        return 'O'
    return None


def main():
    cells = '_________'
    current_player = 'X'

    while True:
        print_field(cells)

        cells = make_move(cells, current_player)

        winner = check_win(cells)
        if winner:
            print_field(cells)
            print(f"{winner} wins")
            break

        if '_' not in cells:
            print_field(cells)
            print("Draw")
            break

        current_player = 'O' if current_player == 'X' else 'X'

main()