import random

def collatz(n: int):
    if n <= 1:
        print("Liczba musi być większa od 1")
    wynik = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            print(n)
            wynik.append(n)
        else:
            n = n * 3 + 1
            print(n)
            wynik.append(n)
    return wynik

lista=[]
for i in range (1,500):
    x=len(wynik(i))
    lista.append(x)
print(lista.index(max(lista)))







