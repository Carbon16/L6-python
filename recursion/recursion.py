def addNums(numbers):
    if len(numbers) > 1:
        numbers[0] = numbers[0] + addNums(numbers[1:])
    print(numbers[0])
    return(numbers[0])

marks = [3,6,2,8]
total = addNums(marks)
print("Total = ", total)
