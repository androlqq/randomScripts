import requests

dzialajaceStrony = open("dzialajacestrony.txt", 'r+')

with open("listaStron.txt", 'r') as listaStron:
    for line in listaStron:
        #print(line)
        zapytanieDoStrony = requests.get(line.strip())
        if zapytanieDoStrony.status_code == 200:
            dzialajaceStrony.write(line)
    print(dzialajaceStrony.read())
    dzialajaceStrony.close()

