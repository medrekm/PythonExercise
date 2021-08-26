from random import randint


def dzielniki(x):
    for a in range(1, x):
        if (x % a == 0):
            print(a)


# end of function definition

x = int(input("podaj liczbę: "))
print("podana liczba: {}".format(x))

if (x % 2 == 0):
    print("Liczba {} jest parzysta".format(x))
else:
    print("Liczba {} jest nieparzysta".format(x))

a = 0
c = 2

for a in range(x):
    if (a % 2 == 0):
        print("{} --> parzyste".format(a))
    else:
        print("{} --> nieparzyste".format(a))

dzielniki(x)

a = 0
tablica = []
for a in range(x):
    u = randint(1, 100)
    tablica.append(u)

print("Liczby pseudolosowe: ")
print(tablica)

for i in range(x):
    for j in range(i+1,x):
        if (tablica[i] < tablica[j]):
            p = tablica[i]
            tablica[i] = tablica[j]
            tablica[j] = p

print("Tablica posortowana: ",tablica)


