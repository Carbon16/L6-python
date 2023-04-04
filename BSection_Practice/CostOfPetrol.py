nums = input("Enter the numer of miles: ")
litres = nums.split()
total = 0
for i in range(len(litres)):
    litres[i] = int(litres[i])
    total += litres[i]
emissions = total * 0.0024
emissions = round(emissions, 0)
print("Emissions ", emissions)