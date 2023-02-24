
ipit = str(input())
#slice and dice on spaces to array
iarr = ipit.split(" ")
oput = ""
oarr = []

for i in range(len(iarr)):
    if iarr[i][0] == "a" or ipit[i] == "e" or ipit[i] == "i" or ipit[i] == "o" or ipit[i] == "u":
        oarr[i].append(iarr[i] + "-yay")
    else:
        oarr[i].append(iarr[i][1:] + "-" + iarr[i][0] + "ay")

outpot = " ".join(oarr)
print(outpot)