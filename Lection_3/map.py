li = [x for x in range(1, 20)]

li = list(map(lambda x:x+10, li))

print(li)

data = map(int, input().split())
print (data)

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)