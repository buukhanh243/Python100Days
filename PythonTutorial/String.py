import time

strA = "xin chao cac ban"
# strB = strA[len(strA)-1]
# strD = strA[-1]
# strE = strA[4:8]
# strC = strB in strA

strD = strA[None:None:-1]
strC = strD in strA
print(strD)
# print(strB)
print(strC)
# print(strD)
# print(strE)
# del strD
# print(strD)
print("Start :", time.ctime())
strE = "Nhi Nguyễn chó đẻ súc vật"
print("Đang bắt đầu tiến hóa thêm...")
strW = strE[None:10] + " con đĩ" + strE[10:None]
print(strW,end='\n')
time.sleep(3)
print("End :", time.ctime())

