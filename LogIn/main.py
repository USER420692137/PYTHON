from atexit import register
from base import ListAc

# definiujemy liste naszą ukochaną 
Ac = ListAc

# trudna decyzja na sam początek
def decyzjaNaStart():
    #  fancy AsK
    Decyzja = input("LOGOWANIE CZY REJSTROWANIE (wpisz register lub login):? ")

    if Decyzja == 'login':
       # LOGin
       SomthingLikeAss()
    elif Decyzja == 'register':
         # Re(ligia)gister
         SomthinglikeYou()
    else:
       # cos inne wpisal goscu
       print('cos nie pyklo')


# czas na logowanie konta essa /login/

def SomthingLikeAss():
    # zapytanie o dane użytkownika 

    User = input('Ręce do góry dawaj użytkownika!: ')

    # chyba sprawdzanie bo działa

    if User in Ac:

        print('Użytkownik Git')
        # zapytanie o haslo i dalsza jazda
        passWord = input('Hasło albo śmierć!: ')

        if passWord in Ac[User]:
            # sławna dalsza akcja 
            print('Haslo Git witamy w systemie')
            dalszadroga()
        else:
            print('cos nie pyklo')
            decyzjaNaStart()
    else:
        print('Nie istnieje taki użytkownik *strzela*')
        decyzjaNaStart()

# czas na stworzenie konta /register/

def SomthinglikeYou():
    # akcja związana z regIsTracją
    NewUser = input('jegomościu jakże poważny jak się nazwiesz? ')
    
    # sprawdzanie neutralności
    if NewUser in Ac:
       # gosc scogal
       print('Sry ale nie jestes autentyczny')
       decyzjaNaStart()
    else:
        # gosc jest jak michal aniol orginal fresh
        print('i pykk dodajemy cie do systemu')
        # pytanko o tajne 4 znakowe haslo
        newPassWord = input('podawaj swoje haslo warjacie ')
        
        #gostek dodawany
        Ac[NewUser] = [newPassWord]
        decyzjaNaStart()
        
def dalszadroga():
    pass

decyzjaNaStart()