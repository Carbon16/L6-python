import json
import csv

data = {"hello": "world", "foo": "bar"}

def wCSV():
    #write to csv
    with open('data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in data.items():
            writer.writerow([key, value])
def rCSV():
    #read from csv
    with open('data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)

def wTXT():
    #write to txt
    with open('data.txt', 'w') as txt_file:
        for key, value in data.items():
            txt_file.write(f'{key} : {value}\n')
    
def rTXT():
    #read from txt
    with open('data.txt', 'r') as txt_file:
        for line in txt_file:
            print(line)
    
def wJSON():
    #write to json
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)
    
def rJSON():
    #read from json
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        print(data)
    
def wBIN():
    #write to binary
    with open('data.bin', 'wb') as bin_file:
        bin_file.write(data)
    
def rBIN():
    #read from binary
    with open('data.bin', 'rb') as bin_file:
        data = bin_file.read()
        print(data)
        
def menu():
    int(input("1. Write to CSV\n2. Read from CSV\n3. Write to TXT\n4. Read from TXT\n5. Write to JSON\n6. Read from JSON\n7. Write to BIN\n8. Read from BIN"))
    if input == 1:
        wCSV()
    elif input == 2:
        rCSV()
    elif input == 3:
        wTXT()
    elif input == 4:
        rTXT()
    elif input == 5:
        wJSON()
    elif input == 6:
        rJSON()
    elif input == 7:
        wBIN()
    elif input == 8:
        rBIN()
    # else:
    #     print("Invalid input")
    #     menu()
    
menu()