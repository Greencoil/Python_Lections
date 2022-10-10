# Логические ветвления (Управляющие конструкции) if, else, elif
# if условие:
    # operator 1
    # operator 2
    # operator ...
    # operator n
# else:
    # operator n + 1
    # operator n + 2
    # operator ...
    # operator n + m
# !ВАЖНО отступы обязательны

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# if conditionl:
    # operator
# elif conditionl 2:
    # operator 2
# elif conditionl 3:
    # operator 3
# else:
    # operator

username = input('Введите имя: ')
if username == 'Лана':
    print('Ура, это же моя любовь Ланочка!')
elif username == 'Иван':
    print('С возвращением Иван!')
elif username == 'Ильнар':
    print('Ильнар - топ!)')
else:
    print('Привет, ', username)