import random
while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum = dice1 + dice2
    print(f"Выпало: {dice1} и {dice2}, Сумма:{sum}")

    if dice1 == dice2:
        print('Дубль')
    elif sum == 7 or sum == 11:
        print('Джекпот')
    else:
        print('Обычный ход')

    answer = input('бросить еще раз? да/нет: ')
    if answer != 'да':
        print('пока')
        break