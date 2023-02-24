iput = 1000
iarr = []
while iput > 0:
    iput = int(input())
    iarr.append(iput)
    
for i in range(len(iarr)):
    line = ""
    gofor = int(iarr[i])
    for e in range (0, gofor):
        line += "-"
    print(line)
    