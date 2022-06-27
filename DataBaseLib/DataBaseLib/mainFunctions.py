
listOfLists = []

lisOfColumnsByName = {}
lisOfColumnsById = {}

listOfRowsById = {}
ListOfRowsByName = {}

ListOfDataById = {}
listOfDataByName = {}

def TableCreate(tableId):
    # name and add to list 
    tableId = 'A' + str(tableId)
    listOfLists.append(tableId)

def ColumnAdd(TableId, ColumnId, ColumnName):
    # column
    if ColumnName in lisOfColumnsByName:
       print("'", ColumnName, "'" , 'already exists')
    else:
        lisOfColumnsByName[(ColumnName)] = str(TableId) + 'C' +str(ColumnId)
        
        lisOfColumnsById[(str(TableId) + 'C' + str(ColumnId))] = ColumnName
        
        return lisOfColumnsByName, lisOfColumnsById

def RowAdd(TableId, RowId, RowName):
    if TableId in listOfLists:
        if RowName in ListOfRowsByName:
            print("'", RowName, "'" , 'already exists')
        else:
            ListOfRowsByName[(RowName)] = str(TableId) + 'R' + str(RowId)
            
            listOfRowsById[str(TableId) + 'R' + str(RowId)] = (RowName)
            
            return listOfRowsById, ListOfRowsByName
    else:
        print(TableId , 'does not exist')

def AddData( TableId , ColumnId , RowId , ColumnName , RowName , Data):
    if TableId in listOfLists:
        if TableId + 'R' + RowId in listOfRowsById:
            if TableId + 'C' + ColumnId in lisOfColumnsById:
                if str(TableId) + 'C' + str(ColumnId) + 'R' + str(RowId) in ListOfDataById :
                    print(str(TableId) + 'C' + str(ColumnId) + 'R' + str(RowId) , 'already exists')
                else:
                    ListOfDataById[(str(TableId) + 'C' + str(ColumnId) + 'R' + str(RowId))] = Data
                    
                    listOfDataByName[str(ColumnName) + str(RowName)] = Data
                    
                    return ListOfDataById , listOfDataByName
            else:
               print(ColumnId , 'does not exist')
        else:
            print(RowId , 'does not exist')
    else:
        print(TableId , 'does not exist')

def DataTakeById(SquareId):
    if SquareId in ListOfDataById:
        ReceiveVariable = ListOfDataById[SquareId]
        
        return ReceiveVariable
    else:
        print(SquareId , 'does not exist')

def DataTakeByNameId(SquareNameId):
    if SquareNameId in listOfDataByName:
        ReceiveVariable = listOfDataByName[SquareNameId]

        return ReceiveVariable
    else:
        print(SquareNameId , 'does not exist')

def DataDelateById(SquareId):
    if SquareId in ListOfDataById:
        ListOfDataById[SquareId] = ''
    else:
        print(SquareId , 'does not exist')

def TablePrint(TableId , lenght):
    Collumns = ''
    Newspaces = str('')
    A = 1
    B = 1
    if TableId in listOfLists:
        for x in range(len(lisOfColumnsById)):
            long = len(lisOfColumnsById[f'{TableId}C{A}'])
            spaces = lenght - int(long)
            Newspaces = ''
            for n in range(spaces):
                Newspaces = str(Newspaces) + ' '
            Collumns = Collumns + '|' + str(lisOfColumnsById[f'{TableId}C{A}']) + Newspaces + '|'
            A += 1
        print(Collumns)
        for h in range(len(listOfRowsById)):
            Collumns = ''
            A = 1
            for x in range(len(lisOfColumnsById)):
                long = len(str(ListOfDataById[f'{TableId}C{A}R{B}']))
                spaces = lenght - int(long)
                Newspaces = ''
                for n in range(spaces):
                    Newspaces = str(Newspaces) + ' '
                Collumns = Collumns + '|' + str(ListOfDataById[f'{TableId}C{A}R{B}']) + Newspaces + '|'
                A += 1
            print(Collumns)
            B += 1
    else:
        print(TableId , 'does not exist')

def TablePrintInFile(TableId , File , lenght):
    Collumns = ''
    Newspaces = str('')
    sourceFile = open(File, 'w')
    A = 1
    B = 1
    if TableId in listOfLists:
        for x in range(len(lisOfColumnsById)):
            long = len(lisOfColumnsById[f'{TableId}C{A}'])
            spaces = lenght - int(long)
            Newspaces = ''
            for n in range(spaces):
                Newspaces = str(Newspaces) + ' '
            Collumns = Collumns + '|' + str(lisOfColumnsById[f'{TableId}C{A}']) + Newspaces + '|'
            A += 1
        print(Collumns , file = sourceFile)
        for h in range(len(listOfRowsById)):
            Collumns = ''
            A = 1
            for x in range(len(lisOfColumnsById)):
                long = len(ListOfDataById[f'{TableId}C{A}R{B}'])
                spaces = lenght - int(long)
                Newspaces = ''
                for n in range(spaces):
                    Newspaces = str(Newspaces) + ' '
                Collumns = Collumns + '|' + str(ListOfDataById[f'{TableId}C{A}R{B}']) + Newspaces + '|'
                A += 1
            print(Collumns , file = sourceFile)
            B += 1
    else:
        print(TableId , 'does not exist')