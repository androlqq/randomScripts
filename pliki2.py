nazwaPliku = str(input("Podaj nazwę pliku, który chcesz wczytać: "))

def odczytPliku(sciezka):
    try:
        with open(sciezka, 'r', encoding='UTF-8') as file:
            print(file.readlines())
    except FileNotFoundError:
        print("Nie ma takiego pliku")

odczytPliku(nazwaPliku)