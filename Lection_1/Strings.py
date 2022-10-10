# Строки (немножко)
text = 'съешь ещё этих мягких французких булок'
print(len(text))                    # 39 символы
print('ещё' in text)                # True
print(text.isdigit())               # False
print(text.islower())               # True
print(text.replace('ещё', 'ЕЩЁ'))   #

for c in text:
    print(c)

# Срезы для работы со строками
print(text[0])   # c print(text[1])   
print(text[1])   # ъ
print(text[len(text)-1])  # к
print(text[-5])  # б
print(text[:])   # print(text), так же это равно print(text[0:len(text)-1])
print(text[:2])  # съ
print(text[len(text)-2:])  # ок
print(text[2:9])  # ешь ещё
print(text[6:-18])  # ещё этих мягких
print(text[0:len(text):6])  # сеикакл
print(text[::6])  # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

