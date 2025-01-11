def read(mode,name):
    try:
        file = open(name, 'r',encoding='UTF-8')
    except FileNotFoundError:
        print('Файла не существует!')
        return None
    if mode == 1:
        for line in file.readlines():
            print(line)
    if mode == 2:
        print(file.read())
    file.close()

mode = int(input('''Выберите режим чтения:
1 - Построчное
2 - Весь файл сразу
>> '''))
name = input('Введите имя файла >> ')
read(mode,name)
