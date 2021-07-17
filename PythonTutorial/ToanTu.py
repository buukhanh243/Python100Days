from decimal import *
from math import *
import math
from fractions import *
getcontext().prec = 30   # lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
d = Decimal(10) / Decimal(3)
print(d)

a = Decimal(100) / Decimal(3)
print(a)

b = 10**3
print(b)
print(type(b))

#f = 10//3 #ket qua luon nho hon hoac bang thuong nguyen
f = 10 // -3
print(f)

g = 10%3 #lay so du
print(g)


# Ham eval
s = "(5*6) - (7/2)+8+sin(0.5)+pow(2,3)"

print(eval(s))

frac = Fraction(1, 4)
print(frac)

#p = 2 + 1j5
p = complex(2, 1)
print(p)
print("phan thuc {0}, phan ao {1:>5}".format(p.real, p.imag))

#h = math.trunc(3.9) #lay phan nguyen
#h = math.fabs(-3) #lay tri tuyet doi
#h = math.sqrt(16) #can bac 2
#h = math.gcd(6, 4)#lay uoc chung lon nhat
#h = math.ceil(3.33) #lam tron lon hon : 4
h = math.floor(3.542) # lam tron nho hon : 3

print(h)
