colors = {'red', 'green', 'blue'}

print(colors)   # {'red', 'green', 'blue'}
colors.add('red') # Добавляя имеющийся элемент множества ничего не происходит
print(colors)   # {'red', 'green', 'blue'}
colors.add('gray') # LДобавить нвоый элемент множества
print(colors)   # {'red', 'green', 'blue', 'gray'}
colors.remove('red') # Убрать один из элементов множества
# colors.remove('red') - при попытке убрать отсутсвующий элемент выдает ошибку "KeyError: 'red'"
print(colors)   # {'green', 'blue', 'gray'}
colors.discard('red') # В данном случае даже если такое элемента множества нет, ничего не происходит, в том числе не выдает ошибку
print(colors)   # {'green', 'blue', 'gray'}
colors.clear()  # Очищаем множество от элементов - {}
print(colors)   # просит ввести элементы множества: set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()            # Создаем копию выбранного множества: c = {1, 2, 3, 5, 8}
u = a.union(b)          # Объединение множеств: u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)   # Пересечение множеств: i = {2, 5, 8}
dl = a.difference(b)    # Не пересекаемые значения в первом множестве: dl = {1, 3}
dr = b.different(a)     # Не пересекаемые значения во втором множестве: dr = {13, 21}

q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}

s = frozenset(a) # Не изменяемое множество. Никакие функци по добавлению, изменению и т.д. не будут работать