list1 = [1, 2, 3, 4, 5]
list2 = list1
list1[0] = 123 
list2[1] = 333
# Вне зависимости от того где поменяли символ, меняются оба листа в случае их копирования одног ов другой

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

print()

list3 = [1, 2, 3, 4, 5]

print('Изначальный список: ', list3)
print()
print('Убираем: ', list3.pop()) # Команда для удаления последнего эжлемента списка
print('Получаем: ', list3)
print()
print('Убираем: ', list3.pop()) # Команда для удаления последнего эжлемента списка
print('Получаем: ', list3)
print()
print('Убираем: ', list3.pop()) # Команда для удаления последнего эжлемента списка
print('Получаем: ', list3)
print()
print('Убираем: ', list3.pop()) # Команда для удаления последнего эжлемента списка
print('Получаем: ', list3)
print()
print('Убираем: ', list3.pop()) # Команда для удаления последнего эжлемента списка
print('Получаем: ', list3)

print()

list4 = [1, 2, 3, 4, 5]
print(list4)
list4.insert(2, 11) # Добавляем элемент списка на определенную позицию (позиция, элемент)
print(list4)

print()
list4.append(11) # Добавление элемента в конец списка
print(list4)
