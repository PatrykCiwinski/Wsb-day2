import time

while True:
    liczba = int(input("Podaj liczbe, sprawdzimy parzystosc "))
    if liczba%2==0:
        time.sleep(3)
        print("serio, nie wiesz")
        time.sleep(2)
        print("dalej nic?")
        time.sleep(2)
        print("no, parzysta")
    else:
        time.sleep(3)
        print("nieparzysta, meh")
        time.sleep(2)
        if liczba>30:
            print("za wysokie progi panie")
        else:
            print("zszedłeś na niziny inteligencji")
    wybor=input("Jestem głąbem Tak/Nie: ").lower()
    if wybor=="tak":
            print("jesteś")
            time.sleep(3)
            print("glabem ale swiadomym s...")
            time.sleep(2)
            print("wojej ulomnosci")

    else:
            print("ty debilu skonczony")
    break