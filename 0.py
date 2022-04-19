capitals = ["Berlin",
            "Warszawa",
            "Paryż",
            "Moskwa"
]
countries = [ "Niemców",
              "Polski",
              "Francji",
              "Rosji",
]

a = 0

for n in range(4):

    capital = input("Jaka jest stolica: " + countries[int(a)] + " ")

    if capital == capitals[int(a)]:
        print("Wyśmienicie")
        a = int(a) + int(1);
        int(a)
    else:
        print("Żle")

print("Brawo Ukończyłeś Test!!")

