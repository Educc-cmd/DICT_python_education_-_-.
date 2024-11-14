import random

num_friends = int(input("Введіть кількість друзів, які приєднуються (включно з вами): "))

if num_friends <= 0:
    print("Ніхто не приєднується до вечірки")
else:
    friends = {}

    print("Введіть ім'я кожного друга (включно з вами), кожне з нового рядка:")

    for _ in range(num_friends):
        name = input("> ")
        friends[name] = 0

    total_amount = float(input("Введіть загальну суму: "))

    amount_per_person = round(total_amount / num_friends, 2)

    for friend in friends:
        friends[friend] = amount_per_person

    lucky_feature = input("Бажаєте використати функцію 'Хто щасливчик?' Напишіть Yes/No: ")

    if lucky_feature.lower() == "yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} - щасливчик!")

        amount_per_person = round(total_amount / (num_friends - 1), 2)
        for friend in friends:
            friends[friend] = amount_per_person
        friends[lucky_one] = 0

    else:
        print("Ніхто не буде щасливчиком")

    print(friends)