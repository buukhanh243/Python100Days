import random


hoVaTen = input(f'Nhap vao ho va ten nhung nguoi duoc chon: ')
danhSach = hoVaTen.split(',')

numItems = len(danhSach)
random_choice = random.randint(0, numItems-1)

nguoiMayMan = danhSach[random_choice]
print(nguoiMayMan + " is going to by the meal today!")


