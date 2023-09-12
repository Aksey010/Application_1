def balance_game():
    a=[]
    score = 0
    dct_bought={}
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')



        if choice == '1':
            score+=int(input('Введите сумму для пополнения счёта'))



        elif choice == '2':
            bought_price = int(input('Введите сумму покупки'))
            if bought_price <= score :
                buy_item=input('Введите, что вы хотите купить')
                score -= bought_price
                a.append(( buy_item,bought_price))
            else: print('У вас недостаточно средств')



        elif choice == '3':
            print(a)



        elif choice == '4':
            break



        else:
            print('Неверный пункт меню')
