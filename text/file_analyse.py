from cgitb import text
import re
import json

fileName = str(input("Enter path to file: "))

f = open(fileName, 'r')
data = f.read()
f.close()
sample = []
chunky = {}


#get number of documents
match = re.findall(r'([0-9]{1,3}) of ([0-9]{1,3}) DOCUMENTS\s+(.+)\s+(.+)([\S\s]*?)LENGTH: \d{0,3} words([\n]*?)([\S\s]*?)LOAD-DATE', data)
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
     
for i in chunky:
    for i in chunky:
        if i != int(chunky[i]["id"]):
            sample.append(chunky[i]['text'])
    if chunky[i]['text'] in sample:
        chunky[i]['duplicate'] = True

for i in chunky:
    fNom = (chunky[i]['title']).replace(' ', '_') + '_' + chunky[i]['date'].replace(' ', '_') + '_' + chunky[i]['id'] + '.txt'
    fin = open(fNom, 'w', encoding='utf-8')
    fin.write(chunky[i]['text'])
    print(fNom)
    fin.close()

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(chunky, file, ensure_ascii=False, indent=4)
    