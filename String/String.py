my_list = ['how', 'are', 'you', 'doing']
sentence = ' '.join(my_list)
print(sentence)

print(f" Ong    buu Khanh   ".strip())
print(f" On Island".strip(' O'))
print(f"but life is good".split(' '))
print(f"Help me huhu".replace("me huhu","con cac ne"))

my_string = "need to make a fire"
print(my_string.startswith("need"))
print(my_string.endswith("need"))

print(my_string.index('e'))
# index co bao loi
print(my_string.find('c')) #-1 la ko tim thay
print(my_string.upper())
print(my_string.title())
print(my_string.capitalize())
print(my_string.count('a'))