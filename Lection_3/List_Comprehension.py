list = []
for i in range(1, 101):
    if(i%2 == 0):
        list.append(i)
print(list)
print()

list2 = [i for i in range(1,21) if i%2 == 0] #Равносильно выше написанному
list3 = [(i, i) for i in range(1,21) if i%2 == 0] #Используем картежы
print (list2)
print()
print (list3)
print()

def f(x):
    return x**3

list4 = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(list4)