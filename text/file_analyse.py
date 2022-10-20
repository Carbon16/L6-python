from cgitb import text
import re
import json

fileName = str(input("Enter path to file: "))

f = open(fileName, 'r')
data = f.read()
f.close()
chunky = {}


#get number of documents
#welcome to regex hell
#Explination of regex: https://regex101.com/r/nB0naG/1 (example will be broken, but it explains the syntax)
match = re.findall(r'([0-9]{1,3}) of ([0-9]{1,3}) DOCUMENTS\s+(.+)\s+(.+)([\S\s]*?)LENGTH: \d{0,3} words([\n]*?)([\S\s]*?)LOAD-DATE', data)
#this creates the json dictionary for debugging and ananlysis. I used json as it is a good visualisation of dictionaries
for i in match:
    id = str(i[0])
    total = int(i[1])
    # save all groups to a dictionary with id as key
    chunky[id] = {
        'id': id,
        'total': total,
        'title': i[2],
        'date': i[3],
        'text': i[6]
    }
    
#duplicate detecion
for i in chunky:
    #resets the array
    sample = []
    #adds the text of each document to the array bar the current document
    for i in chunky:
        if i != int(chunky[i]["id"]):
            sample.append(chunky[i]['text'])
    #checks if the current document is in the array, if it is it adds the duplicate attribue to the dictionary
    if chunky[i]['text'] in sample:
        chunky[i]['duplicate'] = True
    if chunky[i]['text'] not in sample:
        chunky[i]['duplicate'] = False

#saves each item in the dictionary to a sepereate text file
for i in chunky:
    if chunky[i]['duplicate'] == False:
        fNom = (chunky[i]['title']).replace(' ', '_') + '_' + chunky[i]['date'].replace(' ', '_') + '_' + chunky[i]['id'] + '.txt'
        fin = open(fNom, 'w', encoding='utf-8')
        fin.write(chunky[i]['text'])
        print(fNom)
        fin.close()

#saves json for debugging and anlaysis
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(chunky, file, ensure_ascii=False, indent=4)
    