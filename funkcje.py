# def dodaj_10_do_liczby(liczba:int):
#     wynik=liczba+10
#     print(wynik)
#
# dodaj_10_do_liczby(14)

def silnia(x:int):
    suma = 1
    for i in range (2, x+1):
        suma=i*suma
    return suma

print(silnia(889))

def fib(n):
    if n in [0, 1]:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(4))


