import re
import json

f = open('The_Guardian2013.txt', 'r')
data = f.read()
f.close()
sample = []
chunky = {}


#get number of documents
match = re.findall(r'([0-9]{1,3}) of ([0-9]{1,3}) DOCUMENTS\s+(.+)\s+(.+)([\S\s]*?)LENGTH: \d{0,3} words([\n]*?)([\S\s]*?)LOAD-DATE', data)
for i in match:
    id = str(i[0] + ' of ' + i[1])
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
    sample.append(chunky[i]['text'])
    
for i in chunky:
    if chunky[i]['text'] in sample:
        chunky[i]['duplicate'] = True
        print("Dupe")


with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(chunky, file, ensure_ascii=False, indent=4)

