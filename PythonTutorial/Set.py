my_set={1,2,3,4,5}
my_set.add(100)
my_set.add(2)
#2 không được add vào vì trong set đã có 2 r
#Kiểu set ko support cho index my_set[0] là báo lỗi
print(my_set)

my_set={1,2,3,4,5,5}
print(len(my_set))
# dòng trên sẽ ra là 5, vì năm ở cuối đc lặp lại nên ko tính là 6