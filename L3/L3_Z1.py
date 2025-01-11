def read(mode):
    file = open('example.txt', 'r', encoding='UTF-8')
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
read(mode)
