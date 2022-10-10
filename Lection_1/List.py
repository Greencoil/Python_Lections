# Списки (массив для твоего понимания C#'ник)
# Задаем значение списка
numbers = [1, 2, 3, 4, 5]
print(numbers)
ran = range(1, 6)
print(type(ran))
numbers = list(ran)
print(type(numbers))

# Выводим данные списка
print(numbers)
numbers[0] = 10
print(f'{len(numbers)} len')
print(numbers)
for i in numbers:
    i*=2
    print(i)
print(numbers)

# Удаление, перемещение по списку элементов
colors = ['red', 'green', 'blue']

for e in colors:
    print(e)
for e in colors:
    print(e*2)

colors.append('gray')
print(colors == ['red', 'green', 'blue', 'gray'])
colors.remove('red') # del colors[0]
print(colors)