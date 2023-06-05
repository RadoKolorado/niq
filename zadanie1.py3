a = 25001
b = 30012
c = 23005
d = 20007
e = 62015
f = 22022


print("")
#### DEFINIOWANIE WARTOSCI

g = int(input("Podaj ile razy wartosc 1.0 pojawila sie w probie: "))
if g > 0:
    print("Podana przez uzytkownika wartosc wynosi: ", g)
else:
    print("Podana wartosc nie moze byc liczba ujemna. Uruchom program ponownie.")

if g < 0:
    exit()

print("")
#### SREDNIA

lista = [25001, 30012, 23005, 20007, 62015, 22022, g]
srednia = int((a + b + c + d + e + f + g)/len(lista))
print("Srednia wartosc z proby wynosi:", srednia)

print("")
#### WARIANCJA 

def wariancja(lista):
    n = len(lista)
    mean = sum(lista)/n
    devi = [(x - mean)**2 for x in lista]
    
    wariancja = sum(devi)/(n-1)
    return wariancja

print("Wariancja wynosi:", wariancja(lista))

print("")
#### MODA

lista.sort()

if lista[-1] == a:
    print("Najczesciej wystepujaca wartoscia jest 1.5 i wystepuje", lista[-1], "razy.")
elif g == e:
    print("Moda nie moze zostac obliczona ze wzgledu na dwie takie same wartosci. Uruchom program ponownie")
elif lista[-1] == b:
    print("Najczesciej wystepujaca wartoscia jest 1.8 i wystepuje", lista[-1], "razy.")
elif lista[-1] == c:
    print("Najczesciej wystepujaca wartoscia jest 0.5 i wystepuje", lista[-1], "razy.")
elif lista[-1] == d:
    print("Najczesciej wystepujaca wartoscia jest 0.7 i wystepuje", lista[-1], "razy.")
elif lista[-1] == e:
    print("Najczesciej wystepujaca wartoscia jest 1.2 i wystepuje", lista[-1], "razy.")
elif lista[-1] == f:
    print("Najczesciej wystepujaca wartoscia jest 0.6 i wystepuje", lista[-1], "razy.")
elif lista[-1] == g:
    print("Najczesciej wystepujaca wartoscia jest 1.0 i wystepuje", lista[-1], "razy.")

if g == e:
    exit()

print("")
#### ZAPIS DO PLIKU

zapisz = open('wynik.txt', 'w')
zapisz.write("Uzytkownik podal wartosc: " + str(g) + "\n")
zapisz.write("Oznacza to, ze srednia wartosc z proby wynosi: " + str(srednia) + "\n")
zapisz.write("Wariancja wynosi: " + str(wariancja(lista)) + "\n")
zapisz.write("Moda: najczesciej wystepujaca wartosc pojawila sie " + str(lista[-1]) + " razy.")