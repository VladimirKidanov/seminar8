def search():
    print('Укажите по какому параметру будет осуществляться поиск:\n\
        1 - Фамилия\n\
        2 - Имя\n\
        3 - Номер телефона\n\
        4 - Описание')
    n = int(input('Ваш выбор: '))
    if n == 1:
        entry = input('Введите фамилию: ').title()
    if n == 2:
        entry = input('Введите имя: ').title()
    if n == 3:
        entry = input('Введите номер телефона: ').title()
    if n == 4:
        entry = input('Введите описание контакта (Личный, Рабочий, Домашний и т.д.): ').title()
    print(f'Поиск будет осуществляться по: {entry}')
    return entry