import os
import sys
import shutil
from функции.use_functions import balance_game as b_g
from функции.borndayforever import borndayforever as bdf


files = []
dirs = []


while True:
    print('1 создать папку')
    print('2 удалить(файл / папку)')
    print('3 копировать(файл / папку)')
    print('4 просмотр содержимого рабочей директории')
    print('5 посмотреть только папки')
    print('6 посмотреть только файлы')
    print('7 просмотр информации об операционной системе')
    print('8 создатель программы')
    print('9 играть в викторину')
    print('10 мой банковский счет')
    print('11 сохранить содержимое рабочей директории в файл')
    print('12 выход')

    choice = input('Выберите пункт меню')

    if choice == '1':
        a=input('Введите название папки')
        if not os.path.exists(a):
            os.mkdir(a)


    elif choice == '2':
        b=input('Введите название папки или файла')
        os.rmdir(b)


    elif choice == '3':
        c=input('Введите название папки')
        d=input('Введите новое название папки')
        shutil.copy(c,d)


    elif choice == '4':
        for path in os.scandir():
            print(str(path).replace('<DirEntry ','').replace('>',''))


    elif choice == '5':
        for path in os.scandir():
            if path.is_file():
                print(path.name)


    elif choice == '6':
        for path in os.scandir():
            if not path.is_file():
                print(path.name)


    elif choice == '7':
        print(sys.platform)


    elif choice == '8':
        print('Aksey010')


    elif choice == '9':
        bdf()


    elif choice == '10':
        b_g()


    elif choice == '11':
        with open('listdir.txt', 'w') as f:
            f.write('files: ')
            for path in os.scandir():
                if path.is_file() and files != path:
                    files.append(str(path).replace('<DirEntry ','').replace('>','').replace("'", ""))
            f.write(str(files))
            f.write('\n')
            f.write('dirs: ')
            for path in os.scandir():
                if not path.is_file():
                    dirs.append(str(path).replace('<DirEntry ','').replace('>','').replace("'", ""))
            f.write(str(dirs))


    elif choice == '12':
        break