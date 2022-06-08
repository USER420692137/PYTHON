dzielnice = [
    "srodmiescie",
    "mokotow",
    "wola",
    "ursynow",
    "bemowo"
]

TabelkaNauczania = [
    0,
    0,
    0,
    0,
    0
]

rozwoj = [
    10,
    50,
    40,
    90,
    20,
]

WagaRozwoj = 3

def WybieranieRozwoj():
    a = 0
    b = 1
    for n in range (4):
        if rozwoj[a] > rozwoj[b]:
            a = a
        if rozwoj[a] < rozwoj[b]:
            a = b
        b = b + 1
    print(dzielnice[a])
    TabelkaNauczania[a] = TabelkaNauczania[a] + WagaRozwoj

iloscSklepow = [
    1000,
    2000,
    600,
    3000,
    4000
]

WagaSklepow = 1

def WybieranieIloscSklepow():
    c = 0
    d = 1
    for n in range(4):
        if iloscSklepow[c] > iloscSklepow[d]:
            c = c
        if iloscSklepow[c] < iloscSklepow[d]:
            c = d
        d = d + 1
    print(dzielnice[c])
    TabelkaNauczania[c] = TabelkaNauczania[c] + WagaSklepow

KosztMieszkanZaMetrK2 = [
    10000,
    15000,
    9000,
    13000,
    11000
]

WagaMieszkan = 2

def WybieranieKosztMieszkan():
    e = 0
    f = 1
    for n in range(4):
        if KosztMieszkanZaMetrK2[e] > KosztMieszkanZaMetrK2[f]:
            e = e
        if KosztMieszkanZaMetrK2[e] < KosztMieszkanZaMetrK2[f]:
            e = f
        f = f + 1
    print(dzielnice[e])
    TabelkaNauczania[e] = TabelkaNauczania[e] - WagaMieszkan

def KoncowaAkcja():
    v = 0
    g = 1
    for n in range(4):
        if TabelkaNauczania[v] > TabelkaNauczania[g]:
            v = v
        if TabelkaNauczania[v] < TabelkaNauczania[g]:
            v = g
        g = g + 1
    print("=================")
    print(dzielnice[v])
    print("=================")

i = 0

while i <= 10:

    TabelkaNauczania = [
        0,
        0,
        0,
        0,
        0
    ]
    print(TabelkaNauczania)
    WybieranieKosztMieszkan()
    WybieranieIloscSklepow()
    WybieranieRozwoj()
    print(TabelkaNauczania)

    KoncowaAkcja()
    Koniec = input("I JAK?")

    if Koniec == "Za drogo":
        print("Ok")
        WagaMieszkan = WagaMieszkan * 2
    if Koniec == "Za malo sklepow":
        print("Ok")
        WagaSklepow = WagaSklepow * 2
    if Koniec == "Za maly rozwoj":
        print("Ok")
        WagaRozwoj = WagaRozwoj * 2
