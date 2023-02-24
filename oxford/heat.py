housea = int(input())
garda = int(input())
pipes = 0

if (housea * 2.5) <= garda:
    print("Horizontal")
else:
    print("Vertical")
    while housea > 0:
        housea -= 100
        pipes += 1
    print(pipes)