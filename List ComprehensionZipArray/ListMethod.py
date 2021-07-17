print(sum([1,2,4,5,6,7,8,8]))

wizards = ["ROn","Harry","doremon"]

pets = ["pig","Nhi cho de","suc vat"]

for index,(wiz,pet) in enumerate(zip(wizards,pets)):
    print(f'{index}. {wiz} has {pet}')

sorted_by_first = sorted(['hi','an com chua em','em 2 vach roi anh'],key= lambda el: el[1]) #sort theo ki tu thu 2
print(sorted_by_first)

sorted_by_key = sorted([
    {'name': 'khanh buu','age':15},{'name': 'ong khanh','age':14},{'name': 'thuy ngan','age':20}],key= lambda el: el['age'])
print(sorted_by_key)
