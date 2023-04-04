start = int(input("Your number:"))

num = (start * 3) + 1
if num >= 100:
    num = int(str(num)[1:])


count = 2
while num != start:
    num = (num * 3) + 1
    if num >= 100:
        num = int(str(num)[1:])
        
    count = count + 1
    
    if num == start:
        print(count)
