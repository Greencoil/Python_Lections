# Основы запроса данных у пользователя:
# print('Ввежите a')
# a = input()
# print('Введите b')
# b = input()
# print(a, b)
# print('{1} {0}'.format(a, b))
# print(f'{a} {b}')
# !Важно - при таком запросе, вычисления произвести не получится, 
# так как мы запросили в формате строк. 
# Что бы производить операции с числами необходимо следующее:
print('Ввежите a')
a = int(input()) # Для вещественных чисел используем команду "Float"
print('Введите b')
b = int(input()) # Для вещественных чисел используем команду "Float"
print(a, ' + ', b, ' = ', a+b)