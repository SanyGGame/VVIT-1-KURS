while True:
    file = open('user_input.txt','a',encoding='UTF-8')
    text = input('Введите текст >> ')
    file.write(f'{text}\n')
    file.close()