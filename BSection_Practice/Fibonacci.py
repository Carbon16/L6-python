num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

count = 0
exitCon = False

def flip(num):
    snum = str(num)
    rstr = snum[::-1]
    return int(rstr)
    

while count < 25:
    rnum = flip(num2)
    if rnum == num1:
        print(rnum)
        count = 25
        break
    
    if count == 24:
        print(-1)
    
    sto = num2
    num2 = num1 + num2
    num1 = sto
    count = count + 1
