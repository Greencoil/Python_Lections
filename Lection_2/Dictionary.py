dictionary = {}
# \ - Необходим что бы не писать все в одну строку
dictionary = \
    {
        'up': '↑',  # ALT + 2 и 4
        'left': '←', # ALT + 2 и 7
        'down': '↓', # ALT + 2 и 5
        'right': '→' # ALT + 2 и 6
    }

print(dictionary) # { 'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary['left'])  # ←


for k in dictionary.keys():
    print(k)

# .keys - только ключи (left, right etc.)
# .value - только значения (↓, ↑ etc.) 