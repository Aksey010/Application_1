import os.path


def balance_game():
    balance = 0
    history = []

    if os.path.exists('balance.txt'):
        with open('balance.txt', 'r') as f:
            balance = int(f.read())


    if os.path.exists('bought_history.txt'):
        with open('bought_history.txt', 'r') as f:
            for item in f:
                history.append(item)


    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')



        if choice == '1':
            try:
                balance += int(input('Введите сумму для пополнения счёта'))
                with open('balance.txt', 'w') as f:
                    f.write(str(balance))
            except ValueError:
                print('Ошибка, введено неверное значение')



        elif choice == '2':
            try:
                bought_price = int(input('Введите сумму покупки'))
                if bought_price <= balance :
                    buy_item = input('Введите, что вы хотите купить')
                    balance -= bought_price
                    history.append(( buy_item, bought_price))
                    with open('bought_history.txt', 'w') as f:
                        for item in history:
                            f.write(str(item))
                else: print('У вас недостаточно средств')

            except ValueError:
                print('Ошибка, введено неверное значение')


        elif choice == '3':
            for item in history:
                print(item, end='\n')



        elif choice == '4':
            break



        else:
            print('Неверный пункт меню')
