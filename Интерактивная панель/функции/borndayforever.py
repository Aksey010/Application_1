def borndayforever(year=0,day=0):
    while year != '1799':
        year = input('Ввведите год рождения А.С.Пушкина:')
        if year == '1799': print("Верно")
        else: print('Неверно')

    while day != '6':
        day = input('В какой день июня родился Пушкин?')
        if day == '6' : print('Верно')
        else: print('Неверно')


