#!/usr/bin/python

# wykonanie programu: ./program.py lorem.txt

# import bibliotek
import os
import sys
import re

# sprawdzenie czy istnieje parametr
# proba domyslnego parametru
# sprawdzenie czy istnieje plik z parametru (np lorem.txt)
# jesli nie to komunikat i zamkniecie programu
if len(sys.argv) < 2:
    print("\nBrak parametru.")
    print("Sprawdzam 'lorem.txt'...")
    plik = "lorem.txt"
else:
    plik = sys.argv[1]

if not os.path.isfile(plik):
    print("\nPlik '%s' podany jako parametr nie istnieje." % plik)
    sys.exit()

# otwarcie pliku i wrzucenie do listy 'bufor'
# rozdzielenie tekstu na elementy - separator: znak nowej linii '\n'
p = open(plik, "r")
bufor = p.read().split("\n")
print("\nAnalizowany plik: %s" % plik)
p.close()

# wypisanie ilosci wierszy - ilosci elementow listy 'bufor'
print("\nIlosc wierszy: %s" % len(bufor))

# ilosc wierszy zaw. wyrazenie reg.
reg = '[0-9]+'
licznik = 0
linie_z_reg = []

for i, linia in enumerate(bufor):
    if re.search(reg, linia):
        linie_z_reg.append(i)
        licznik = licznik + 1

print("\nIlosc linii zawierajacych wyrazenie reg.'%s': %s" % (reg, licznik))

# pierwsze 'm' linii zawierajce wyraz. reg.
# '\t' - wciecie, tabulator
m = 5

print("Pierwsze <=%s linii, ktore zawieraja wyraz. reg.'%s':" % (m, reg))

if len(linie_z_reg) == 0:
    print("\tNie ma nic do wyswietlenia.")
else:
    for element in range(m):
        if element == len(linie_z_reg):
            break
        print("\tLinia %s: %s" % (
            linie_z_reg[element], bufor[linie_z_reg[element]]))

# dlugosc linii 'i'
i = 50

print("\nLinia %s: %s" % (i, bufor[i]))
print("Dlugosc linii %s: %s" % (i, len(bufor[i])))

# dlugosc pierwszych 'n' linii
# '\t' - wciecie, tabulator
n = 5

print("\nDlugosc pierwszych %s linii:" % n)

for linia in range(n):
    print("\tDlugosc linii %s wynosi %s" % (linia, len(bufor[linia])))

# linie o dlugosci 'l'
l = 5

print("\nLinie o dlugosci: %s" % l)

for i, linia in enumerate(bufor):
    if len(linia) == l:
        print("\tLinia %s: %s" % (i, linia))
