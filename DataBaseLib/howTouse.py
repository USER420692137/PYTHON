
import DataBaseLib.mainFunctions as DataM
import DataBaseLib.AdvencedFunctions as Adv

##################################
#   How square Id is made ?      #
#   example A1C1R1 <--     row   #
#            \\--column          #
#            \----table          #
##################################
#  How name id is made?          #
# example RownameColumnname      #
#             /     \            #
# row name---/       \column name#
##################################

#  Table create                  #
##################################
# you can got this row by Id + A #
#    in this example print A1    #
#               id               #
DataM.TableCreate(1)
##################################

# column name                    #
##################################
# you can add a column to table  #
# you must to add id = {         #
#    table Id + colum id         #
#                  + column name #
DataM.ColumnAdd('A1',1,'Names')
##################################
#                                #
# row add                        #
##################################
# you can add row to table       #
# gou must to add id and name {  #
# table id + column id + name id #
DataM.RowAdd('A1',1,'PeopleName1')
#################################
#                                #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# names of rows and column can   #
# not repeats                    #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# Data Add                       #
##################################
# you can add data to a table    #
# you must to add {              #####################################
# table id + column id + row id + column name + row name + data }    #
DataM.AddData('A1' , '1' , '1' , 'PeopleName' , 'PeopleName1' , 'Walt')
######################################################################

# data take by id               #
#################################
# you can take data very simple #
# you must to make variable and #
# add ID                        #######
variable = DataM.DataTakeById('A1C1R1')
#######################################

# data take by name id          #
#################################
# its very simple like taking   #
#  by id                        #
#you must to make simple name id#
#  ColumnName + RowName         ################################
variable2 = DataM.DataTakeByNameId('PeopleSurnamePeopleSurname1')
################################################################

# table print                   #
#################################
# table printing is very simple #
# you must to add only table Id #
# and lenght                    #
# exemple                       #
DataM.TablePrint('A1' , 20)
#################################

# table print in file           #
#################################
# table print in file is very   #
# simle like normal print       #
# you must to add table id +    #
# file + lenght                 #
# exemple                       #####################
DataM.TablePrintInFile('A1' , 'ExempleFile.txt' , 50)
#####################################################

# data delate in square         #
#################################
# you can delate data in square #
# by DataDelateById() arguments=#
# = name id                     #
DataM.DataDelateById('A1C1R1')
#################################

# data change A2B               #
#################################
# you can move data from one    #
# square                        #
# you must to add a square id + #
#                   b square id #
Adv.changeA2B('A1C1R1' , 'A1C1R2')
#################################

# count percent                 #
#################################
#to count percent of two squers #
# you must to add id of squers  #
# data of squares must be int   #####
Adv.PercentCount('A1C3R1' , 'A1C3R2')
#####################################