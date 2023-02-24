#seperate chars by space
raw = input()
raw_array = raw.split(" ")
earnings = 0
days = 0 

while earnings < 1000:
    earnings += (int(raw_array.pop(0)) -20)
    days += 1
    
print(days)