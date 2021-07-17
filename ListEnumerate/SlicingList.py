list = [True,False,"ha ngoc ho",1,3.4]

print(list[0:3])
list.extend([100,67,"code dao"])
print(list)
list.pop(1)
print(list)

list.remove("ha ngoc ho")
print(list)

list.reverse()
#set(list)
print(list)
list.extend(('E', 'F'))
print(list)