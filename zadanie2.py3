import random
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

class dane_osobowe:
    def __init__(self, imie, nazwisko, stankonta):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stankonta = int(stankonta)

    def podaj_imie(self):
        print(f"Imie klienta to: {self.imie}.")
    def podaj_naziwsko(self):
        print(f"Nazwisko klienta to: {self.nazwisko}.")

klient1 = dane_osobowe("Andrzej", "Kowalski", random.randrange(0, 10000))
klient2 = dane_osobowe("Krzysztof", "Jaworski", random.randrange(0, 10000))
klient3 = dane_osobowe("Agata", "Witkiewicz", random.randrange(0, 10000))
klient4 = dane_osobowe("Janina", "Kowalska", random.randrange(0, 10000))
klient5 = dane_osobowe("Jerzy", "Wronka", random.randrange(0, 10000))    

suma1 = (klient1.stankonta+klient2.stankonta+klient3.stankonta+klient4.stankonta+klient5.stankonta)

class zarzadzanie(dane_osobowe):
    def stan(self):
        pass

    def podaj_wszystko(self):
        print(f"Dane uzytkownika: {self.imie} {self.nazwisko}. Stan konta: {self.stankonta} PLN.")
    def podaj_nowedane(self):
        print(f"Dziekujemy za dodanie uzytkownika: {self.imie} {self.nazwisko}. Stan konta wynosi: {self.stankonta} PLN.")
    def podaj_szczegoly(self):
        print(f"Imie: {self.imie}; Nazwisko: {self.nazwisko}; Stan konta: {self.stankonta} PLN.")
    def podaj_nowedane(self):
        print(f"Dziekujemy za dodanie uzytkownika: {self.imie} {self.nazwisko}. Stan jego konta wynosi: {self.stankonta} PLN.")
    @property
    def stan(self):
        print(f"")

    @stan.setter
    def stan(self):
        pass

@property
def podaj_stankonta(self): 
        print(f"Stan konta klienta wynosi: {self.stankonta} PLN.")

@podaj_stankonta.getter
def podaj_stankonta(self):
        return "Stan konta wynosi: " + str(self.stankonta)

from pprint import pprint

print("\n\nWitaj w sytemie bankowym. Wybierz jedna z ponizszych komend, aby kontynuowac.")
def menu1():
    print("\nCo dalej chcesz zrobic?\nDodaj nowego klienta: D\nWyswietl klientow: W\nOblicz sume depozytow: S\nZakoncz program: Z")

menu1()
option = input("Podaj komende: ")

while option != 0:
    if option == "W":
        print("\nWszyscy klienci:")
        pprint(vars(klient1))
        pprint(vars(klient2))
        pprint(vars(klient3))
        pprint(vars(klient4))
        pprint(vars(klient5))
        menu1()
        option = input("\nPodaj komende: ")
    elif option == "S":
        print("\nSuma depozytow w banku wynosi", suma1)
        menu1()
        option = input("\nPodaj komende: ")
    elif option == "D":
        break
    elif option == "Z":
        exit()
    else:
        print("\n\nPodana komenda nie istnieje!")
        menu1()
        option = input("\nPodaj komende: ")
    
def dodaj_klienta():
    nowe_konto = {}
    t_n = input("Czy chcesz stworzyc nowe konto? (T/N)")
    if "T" in t_n:
        print("Uzupelnij ponizsze dane by stworzyc konto:")
        nowe_konto["imie"] = input("Podaj imie klienta: ")
        while nowe_konto["imie"].isnumeric():
            print("Imie klienta nie moze zawierac cyfr.")
            nowe_konto["imie"] = input("Podaj imie ponownie: ")
        nowe_konto["nazwisko"] = input("Podaj nazwisko klienta: ")
        while nowe_konto["nazwisko"].isnumeric():
            print("Nazwisko klienta nie moze zawierac cyfr.")
            nowe_konto["nazwisko"] = input("Podaj nazwisko ponownie: ")
        nowe_konto["stankonta"] = input("Podaj stan konta: ")
        while not nowe_konto["stankonta"].isnumeric():
            print("Stan konta musi byc liczba.")
            nowe_konto["stankonta"] = input("Podaj stan konta ponownie: ")
        return nowe_konto
    else:
        print("Wroc ponownie, gdy bedziesz chcial stworzyc nowe konto.")
        exit()

nowyklient = zarzadzanie(**dodaj_klienta())
nowyklient.podaj_nowedane()

suma2 = (klient1.stankonta+klient2.stankonta+klient3.stankonta+klient4.stankonta+klient5.stankonta+nowyklient.stankonta)

class wykres:
    def wykres():
        pass
    
height = [klient1.stankonta, klient2.stankonta, klient3.stankonta, klient4.stankonta, klient5.stankonta, nowyklient.stankonta]
bars = (klient1.nazwisko, klient2.nazwisko, klient3.nazwisko, klient4.nazwisko, klient5.nazwisko, nowyklient.nazwisko)
x_pos = np.arange(len(bars))

plt.bar(x_pos, height, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(x_pos, bars)


def menu2():
    print("\n\nCo dalej chcesz zrobic?\nWyswietl klientow: W\nOblicz sume depozytow: S\nRysuj wykres: WK\nZakoncz program: Z")

menu2()
option = input("Podaj komende: ")

while option != 0:
    if option == "W":
        print("Wszyscy klienci:")
        pprint(vars(klient1))
        pprint(vars(klient2))
        pprint(vars(klient3))
        pprint(vars(klient4))
        pprint(vars(klient5))
        pprint(vars(nowyklient))
    elif option == "S":
        print("Suma depozytow w banku wynosi", suma2)
    elif option == "WK":
        plt.show()
    elif option == "Z":
        exit()
    else:
        print("\n\nPodana komenda nie istnieje!")

    menu2()
    option = input("Podaj komende: ")