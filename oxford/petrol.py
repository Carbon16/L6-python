#seperate chars by space
raw = input()
raw_array = raw.split(" ")
#total raw_array
fuel = 0
for i in range(len(raw_array)):
    fuel += int(raw_array[i])

ann = 0.0024 * fuel
#round down to nearest integer
final = int(ann)

print(final)