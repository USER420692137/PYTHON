import DataBaseLib.mainFunctions as DataM
import DataBaseLib.AdvencedFunctions as Adv

from DataBaseLib.mainFunctions import lisOfColumnsById , listOfRowsById , ListOfDataById

DataM.TableCreate(1)

DataM.ColumnAdd('A1',1,'PeopleNames')
DataM.ColumnAdd('A1',2,'PeopleSurnames')
DataM.ColumnAdd('A1',3,'PeopleAges')

DataM.RowAdd('A1',1,'WaltWhite')
DataM.RowAdd('A1',2,'JessiePigman')

DataM.AddData('A1' , '1' , '1' , 'PeopleName' , 'WaltWhite' , 'Walt')
DataM.AddData('A1' , '2' , '1' , 'PeopleSurnames' , 'WaltWhite' , 'White')
DataM.AddData('A1' , '3' , '1' , 'PeopleAges' , 'WaltWhite' , 51)

DataM.AddData('A1' , '1' , '2' , 'PeopleName' , 'JessiePigman' , 'Jessie')
DataM.AddData('A1' , '2' , '2' , 'PeopleSurnames' , 'JessiePigman' , 'Pigman')
DataM.AddData('A1' , '3' , '2' , 'PeopleAges' , 'JessiePigman' , 30)

DataM.TablePrint('A1' , 20)