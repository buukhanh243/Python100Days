''' Lưu ý:
amazoncart = [a, b, c, d]
new_cart = amazoncart
new_cart[0] = 'gum'
--> new_Cart va amazon_cart = [gum,b,c,d]---> muon coppy ma ko thay doi list amazon
----> ta dung ----> new_cart = amazoncart[:]

amazon_cart.insert(1, 100) ---> a,100,b,c,d
amazon_cart.extend([1, 100]) ---> a,b,c,d,1,100
amazon_cart.pop() ---> xoa cuoi phan tu --> a,b,c ---->pop(0): xoa vi tri so 0---->b,c,d ---> pop la truyen vao index
amazon_cart.remove(truyền vào value: c) ----> a,b,d
new_list = amazon.remove()--->newlist =  non
new_list = amazon.pop()---> new = d
ngoài ra còn có hàm count('thuộc tính') -- đếm số thuộc tính trong mảng
hàm index[0:'thuộc tính']--- vị trí xuất hiện thuộc tính
'''

#a,b,c = 1,2,3
a,b,c = [1,2,3]

print(f'{a} & {b} & {c}') 
'''Get a=1, b=2, c=3'''

d,f,g, *anyIfYouLike,d = [1,2,3,4,5,6,7,8,9]
#[4, 5, 6, 7, 8]
print(anyIfYouLike)
print(d)

#user2 = dict(name='john son')-->{'name':'john son'}