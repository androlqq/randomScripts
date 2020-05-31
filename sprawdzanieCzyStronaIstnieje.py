import requests

dzialajaceStrony = open("dzialajacestrony.txt", 'w')

with open("listaStron.txt", 'r') as listaStron:
    for line in listaStron:
        print(line)
        zapytanieDoStrony = requests.get(line)
        if zapytanieDoStrony.status_code == 200:
            dzialajaceStrony.write(line)

print(dzialajaceStrony.read())
dzialajaceStrony.close()