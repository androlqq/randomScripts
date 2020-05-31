import json
import pprint

def zapisDoPliku(tekst):
    with open('aaa.txt', 'w') as file:
        json.dump(tekst, file, indent=4)

tekst = {'dupa': 'jasiu',
         'costam' : 'sdasdasd',
         'dasdsadsadasd' : 'sadsassdsad'
}

tekstPoFormacie = json.dumps(tekst, indent=4)
zapisDoPliku(tekst)

with open('aaa.txt', 'r') as file2:
    print(file2.read())

print(tekstPoFormacie)