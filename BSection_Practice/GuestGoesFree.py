diners  = int(input("Number of diners: "))

total = 0
for i in range(diners):
    cost = float(input("Cost:"))
    total = cost + total

#tip
total = total * 1.05

#split
toPay = total / (diners - 1)
toPay = round(toPay, 2)
print(toPay)