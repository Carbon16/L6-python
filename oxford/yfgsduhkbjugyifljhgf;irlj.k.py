t1 = int(input())
t2 = int(input())
age = 0
while t1 != t2:
    if t1 > t2:
        t1 -= t2 + 1
    else:
        t2 -= t1 + 1
    age += 1
print(age)