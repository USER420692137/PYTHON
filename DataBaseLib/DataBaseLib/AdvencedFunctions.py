from DataBaseLib.mainFunctions import ListOfDataById , listOfLists , lisOfColumnsById

def changeA2B(AsquareId , BsquareId):
    if AsquareId in ListOfDataById:
        if BsquareId in ListOfDataById:
            change1 = ListOfDataById[AsquareId]
            change2 = ListOfDataById[BsquareId]
            change3 = change2

            change2 = change1
            change1 = change3

            ListOfDataById[AsquareId] = change1
            ListOfDataById[BsquareId] = change2
        else:
            print(BsquareId , 'does not exist')
    else:
        print(AsquareId , 'does not exist')

def PercentCount(SquareId1 , SquareId2):
    PercenT = (ListOfDataById[SquareId1]/ListOfDataById[SquareId2]) * 100
    print(PercenT)