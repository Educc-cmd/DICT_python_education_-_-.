class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "waiting"

    def process_input(self, user_input):
        if self.state == "waiting":
            self.handle_action(user_input)
        elif self.state == "buying":
            self.handle_buy(user_input)
        elif self.state == "filling_water":
            self.fill_water(user_input)
        elif self.state == "filling_milk":
            self.fill_milk(user_input)
        elif self.state == "filling_beans":
            self.fill_beans(user_input)
        elif self.state == "filling_cups":
            self.fill_cups(user_input)

    def handle_action(self, action):
        if action == "buy":
            print("\nЩо ви хочете купити? 1 - еспресо, 2 - лате, 3 - капучино, back - до головного меню:")
            self.state = "buying"
        elif action == "fill":
            print("Напишіть, скільки мл води ви хочете додати:")
            self.state = "filling_water"
        elif action == "take":
            print(f"Я дала тобі {self.money}")
            self.money = 0
        elif action == "remaining":
            self.print_state()
        elif action == "exit":
            self.state = "exit"
        else:
            print("Неправильна дія. Спробуйте ще раз.")

    def handle_buy(self, choice):
        if choice == "1":
            self.make_coffee(250, 0, 16, 4)
        elif choice == "2":
            self.make_coffee(350, 75, 20, 7)
        elif choice == "3":
            self.make_coffee(200, 100, 12, 6)
        elif choice == "back":
            self.state = "waiting"
        else:
            print("Неправильний вибір. Будь ласка, спробуйте ще раз.")
        self.state = "waiting"

    def fill_water(self, amount):
        if not amount.isdigit():
            print("Будь ласка, введіть число.")
            return
        self.water += int(amount)
        print("Напишіть, скільки мл молока ви хочете додати:")
        self.state = "filling_milk"

    def fill_milk(self, amount):
        if not amount.isdigit():
            print("Будь ласка, введіть число.")
            return
        self.milk += int(amount)
        print("Напишіть, скільки грамів кавових зерен ви хочете додати:")
        self.state = "filling_beans"

    def fill_beans(self, amount):
        if not amount.isdigit():
            print("Будь ласка, введіть число.")
            return
        self.beans += int(amount)
        print("Напишіть, скільки одноразових стаканчиків для кави ви хочете додати:")
        self.state = "filling_cups"

    def fill_cups(self, amount):
        if not amount.isdigit():
            print("Будь ласка, введіть число.")
            return
        self.cups += int(amount)
        self.state = "waiting"

    def make_coffee(self, water, milk, beans, cost):
        if self.water < water:
            print("Вибачте, недостатньо води!")
            return
        if self.milk < milk:
            print("Вибачте, недостатньо молока!")
            return
        if self.beans < beans:
            print("Вибачте, недостатньо кавових зерен!")
            return
        if self.cups < 1:
            print("Вибачте, не вистачає одноразових стаканчиків!")
            return
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= 1
        self.money += cost
        print("Я маю достатньо ресурсів, щоб приготувати тобі каву!")

    def print_state(self):
        print("\nКавоварка має:")
        print(f"{self.water} води")
        print(f"{self.milk} молока")
        print(f"{self.beans} кавових зерен")
        print(f"{self.cups} одноразових стаканчиків")
        print(f"{self.money} грошей\n")

coffee_machine = CoffeeMachine()

while coffee_machine.state != "exit":
    if coffee_machine.state == "waiting":
        print("Напишіть дію (buy, fill, take, remaining, exit):")
    user_input = input("> ")
    coffee_machine.process_input(user_input)
    
