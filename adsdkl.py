tablicaDanychImienia = []


with open('original.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        print(line.strip().split(' '))
        tablicaDanychImienia.append(line.strip().split(' '))

with open('imiona.txt', 'w+', encoding='UTF-8') as plikImion:
    for imiona in tablicaDanychImienia:
        print(imiona[0])
        plikImion.write(imiona[0] + '\n')

with open('nazwiska.txt', 'w+', encoding='UTF-8') as plikNazwisk:
    for nazwiska in tablicaDanychImienia:
        try:
            print(nazwiska[1])
            plikNazwisk.write(nazwiska[1] + '\n')
        except:
            print("NULL")
            plikNazwisk.write('NULL\n')
