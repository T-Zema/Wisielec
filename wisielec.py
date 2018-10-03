import os
from random import randint


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def wisielec(n):
    try:
        wordlist = [line.strip() for line in open(n)]
    except:
        print('Could not open file')
        exit()
    wyraz = wordlist[randint(0, (len(wordlist) - 1))]
    wyraz = wyraz.lower()
    wisielce = ['', '''
|
|
|
|
|
| 
| 
''', '''_ _ _ _ 
|/
|
|
|
|
| 
| 
''', '''_ _ _ _ 
|/   | 
|   (_) 
|
|
|
| 
| 
''', '''_ _ _ _ 
|/   | 
|   (_) 
|    | 
|    | 
|
| 
| 
''', '''_ _ _ _ 
|/   | 
|   (_) 
|   \|/ 
|    | 
|
| 
| 
''', '''_ _ _ _ 
|/   | 
|   (_) 
|   \|/ 
|    | 
|   / \ 
| 
| 
''']

    odp = ["_"] * len(wyraz)
    for j in range(len(wyraz)):
        if wyraz[j] == " ":
            odp[j] = " "
    print(*odp)
    licznik = 0
    while licznik < 6 and "_" in odp:
        litera = (input("Podaj litere: \n"))
        litera = litera.lower()
        cls()
        if litera in odp:
            print(*odp)
            print(wisielce[licznik])
            print("Ta litera juz byla, podaj inna.")
        else:
            for k in range(len(wyraz)):
                if wyraz[k] == litera:
                    odp[k] = litera
            if litera not in wyraz:
                licznik += 1
            print(*odp)
            print(wisielce[licznik])
    print ("liczba bledow:", licznik)
    if licznik == 6:
        print("Przegranko :(")
        print("Zgadywane slowko:", wyraz)
    else:
        print("Wygranko :)")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Wisielec")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--izi", action='store_true', help="latwy poziom")
    group.add_argument("-H", "--hard", action='store_true', help="trudny poziom")
    group.add_argument("-p", "--path", action='store_true', required=False, help="podaj sciezke swoich pytan")
    args = parser.parse_args()
    if args.izi:
        n = "list.txt"
    elif args.hard:
        n = "list2.txt"
    elif args.path:
        n = input("Podaj sciezke: ")
    wisielec(n)


if __name__ == "__main__":
    main()
    exit()

