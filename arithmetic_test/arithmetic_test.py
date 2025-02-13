import random


def generate_question(level):
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operator = random.choice(['+', '-', '*'])
        question = f"{num1} {operator} {num2}"
        answer = eval(question)
    else:
        num = random.randint(11, 29)
        question = f"{num}"
        answer = num ** 2
    return question, answer


def get_valid_input():
    while True:
        user_input = input("> ")
        if user_input.lstrip('-').isdigit():
            return int(user_input)
        print("Incorrect format.")


def main():
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        level_input = input("> ")
        if level_input in ["1", "2"]:
            level = int(level_input)
            break
        print("Incorrect format.")

    correct_answers = 0
    for _ in range(5):
        question, correct_answer = generate_question(level)
        print(question)
        user_answer = get_valid_input()

        if user_answer == correct_answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct_answers}/5.")
    print("Would you like to save your result to the file? Enter yes or no.")
    save_input = input("> ").strip().lower()

    if save_input in ["yes", "y"]:
        print("What is your name?")
        name = input("> ")
        level_desc = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
        result_text = f"{name}: {correct_answers}/5 in level {level} ({level_desc}).\n"
        with open("results.txt", "a") as file:
            file.write(result_text)
        print("The results are saved in \"results.txt\".")


if __name__ == "__main__":
    main()
