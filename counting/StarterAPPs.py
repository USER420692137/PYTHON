from datetime import date, datetime
import random
from typing import List
from base import ListOfFunc, ListOfpyth, ListofRoot, square

#czass
hour = datetime.now()

# lista komend
fun = ListOfFunc
# lista komend do piTagoRasa
pyth = ListOfpyth
# pierwistki
root = ListofRoot
# pole kwadratu
square = square

listOFfunctions = ['count Pythagoras' , 'do square root']

def welcome():
    # sprawdzamy godzine i pszemy
    if hour.hour > 20:
        # wieczor
        print('Good eavning sir')
        Something()
    elif hour.hour > 12:
        # popolodnie
        print('Good afternoon sir')
        Something()
    elif hour.hour > 6:
        # ranek
        print('Good morning sir')
        Something()

def Pythagoras():
    # licznie

    # dane
    a = input('first side of the triangle')
    b = input('second side of the triangle')

    #potega
    output = int(a)**2 + int(b)**2

    # pierwiastek
    output = int(output)**0.5
    # odp
    print('c = ' + output)

def Root():
    # poziom pierwiastka 
    deg = input('square root level ')

    # liczba pierwiastkowana
    pier = input('give me a number under ')

    # pierwiastkowanie
    Root = int(pier) ** 1/int(deg)
    print(Root)

def Square():
    a = input('first side ')
    a = a ** 2
    print(a)

def Something():
    # co dziz robimy
    print("What are we doing todey?")

    #propozycja
    Random = random.choice(listOFfunctions)
    print('Shell we ' + Random + '?')
    print('To confirm write: ' + Random)

    # to co robimy?
    well = input('If you want to do somthing anorher just write it. You can also write List to see functions ')

    #możliwości
    if well in fun:
        # funkcja
        if well in pyth:
           Pythagoras()
        if well in root:
            Root()
        if well in square:
            Square()
        # there will be much more
    elif well == 'List':
        # poka liste
        print(listOFfunctions)
    else:
        # cos innego
        print('ajajaj')
    # there will be much more

Root()