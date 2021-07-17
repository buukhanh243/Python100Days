my_dict = {'name': 'Khanh ong buu', 'sex': 'Male', 'age': '20'}
my_dict.update({'age':'27'})
print(my_dict)

my_dict['age'] = 25
print(my_dict)

my_dict.popitem()
print(my_dict)

for key in my_dict.keys():
    print(key, my_dict[key])

#loop over values:

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)