from datetime import datetime

bot_name = "NKey"
birth_year = datetime.now().year

print(f"Салют! Моє ім'я {bot_name}.")
print(f"Я був створений в {birth_year}.")

print("Будь ласка, скажи мені своє ім'я.")
your_name = input("> ")

print(f"Прикольне ім'я, {your_name}!")

print("Давай я угадаю твой вік.")
print("Введіть залишки від ділення вашого віку на 3, 5 і 7.")

remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))

your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Тобі {your_age}; найкращий час, щоб почати програмувати!")

print("Я вмію рахувати до будь якого числа, можете перевірити.")
number = int(input("> "))

for i in range(number + 1):
    print(f"{i} !")

print("Чудово!")

print("Зараз ми пройдемо невеличкий тест.")
print("Що таке функція?")
print("1. Це засіб для повторення однієї команди декілька разів.")
print("2. Це можливість зберігати та обробляти дані.")
print("3. Це спосіб структурувати програму на окремі підпрограми.")
print("4. Це засіб для переривання виконання програми.")

while True:
    answer = int(input("> "))
    if answer == 3:
        print("Вітаю! Гарного дня.")
        break
    else:
        print("Спробуй ще раз :(")