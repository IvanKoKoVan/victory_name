again = 'да'
while again.lower() == 'да':
    right: int = 0
    wrong: int = 0

    query1 = input('Год рождения Ломоносова М.С.') #1711
    if query1 =='1711':
        print("Верно")
        right += 1
    else:
        print('Ошибка')
        wrong += 1

    query2 = input('Год рождения Иссака Ньютона')  # 1643
    if query2 == '1643':
        print("Верно")
        right += 1
    else:
        print('Ошибка')
        wrong += 1

    query3 = input('Год рождения Кулибина И.П.')  # 1735
    if query3 == '1735':
        print("Верно")
        right += 1
    else:
        print('Ошибка')
        wrong += 1

    query4 = input('Год рождения Стива Джобса')  # 1955
    if query4 == '1955':
        print("Верно")
        right += 1
    else:
        print('Ошибка')
        wrong += 1

    query5 = input('Год рождения Николы Теслы')  # 1856
    if query5 == '1856':
        print("Верно")
        right += 1
    else:
        print('Ошибка')
        wrong += 1

    print('Верно', right)
    print('Ошибок', wrong)
    print('Верно', right * 100 / 5, 'percent')
    print('Ошибок', wrong * 100 / 5, 'percent')

    again = input('Начнем игру сначала?')