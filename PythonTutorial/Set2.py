my_set = {1,2,3,4,5,6}
my_set_new = {4,5,6,7,8,9,10}
print(my_set.difference(my_set_new))
#hàm dif tìm điểm giao nhau của 2 cái set kia
my_set.discard(5)
#remove element from my_set if its a member
my_set.difference_update(my_set_new)
my_set.intersection(my_set_new)
#tập hợp giao #my_set & my_set_new --->> 12345678910
#.isdisjoin
#.issubset
#.issuperset
#.union
#my_set || my_set_new --->> 12345678910