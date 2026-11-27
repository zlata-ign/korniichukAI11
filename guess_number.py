import random

secret = random.randint(1, 100)
count = 0

while True:
    num = int(input("Угадай число от 1 до 100:"))
    count += 1

    if num == secret:
        print("Угадал")
        print("Количество попыток:", count)
        break

    elif num < secret:
        print("Больше")

    else:
        print("Меньше")