# napis= "nalesniczki"
#
# if napis.startswith('k'):
#     print('nalesniczki, a jak')
# else:
#     print('nie ma nalesniczkow')
uzytkownicy = ["macius98", "mandarynka_XD", "tytus19", "jej"]

while True:
    nazwa= input("Wpisz login: ")
    if nazwa in uzytkownicy:
        print ("booo, try again!!!")
    else:
        print("wchodzisz")
        uzytkownicy.append(nazwa)
        break
