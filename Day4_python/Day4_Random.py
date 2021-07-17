import random


random_integer = random.randint(0,1) #random 1 - 9
print(random_integer) 
random_float = random.random()*5 #random 0.0000-0.999999 *5: 0.0000-4.999999
print(random_float)

category_product = ['television', 'elephant', 'kong', 'godzila', 'luffy', 'ace', 'sabo' ]
category_product.append('beverages') 
category_product.extend(['ingredient', 'wallet', 'trophy', 'forces'])

print(category_product)

