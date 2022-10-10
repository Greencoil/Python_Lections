# # Логические ветвления (Управляющие конструкции) while, while else, for
# while condition:
    # operator 1
    # operator 2
    # operator ...
    # operator n

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

# while condition:
    # operator 1
    # operator 2
    # operator ...
    # operator n
# else:
    # operator n + 1
    # operator n + 2
    # operator ...
    # operator n + m

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит)')
print(inverted)

# for i in enumeration:
    # operator 1
    # operator 2
    # ...
    # operator n

for i in 'qwe - rty':
    print(i)