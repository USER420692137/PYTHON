import webbrowser
import keyboard
from pyautogui import alert
import shutil
from distutils.dir_util import copy_tree
import os

##############################
# pobieramy uzytkownika
user = os.path.expanduser('~')
##############################
# takie tam bzdury
F4Alert = "alt + f4"
##############################
# sciezki
# sciezka dla pliku pozdro

##################################
# SCIEZKA DO ZD                  #
#################################
zd = f'{user}\\Pictures'
#################################
# SCIEZKA DO DOCS                #
#################################
# docs = f'{user}\\Documents'                 TO DO
#################################

#####################################
# zmienna                           #
# opowiadająca za program           #
#####################################
# łatwe włącz i wyłącz              #
t = 0                               #
######################################

def susy():
####################################################
# zapraszam                                        #
####################################################
   
#######################################################
# odpalanie progrrrramu                              ##
#######################################################
   t = 0           # sławna zmienna                  ##
#######################################################
   while t == 0:
#######################
# rickkkkk           ##
#######################
    
###################################################################
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
###################################################################
#                       RICK ROOOLLLLLL                          #
################################################################## tu zaczyna sie tekst ricka {
# LECIUTKO GOSC SIE ZDENERWUJE
    alert(text='Never gonna give you up', title='SUSY', button='KU#$$#%')
    alert(text='Never gonna let you down', title='SUSY', button='KU#$$#%')
    alert(text='Never gonna run around and desert you', title='SUSY', button='KU#$$#%')
    alert(text='Never gonna make you cry', title='SUSY', button='KU#$$#%')
    alert(text='Never gonna tell a lie and hurt you', title='SUSY', button='KU#$$#%')
#################################################################### a tu koniec tesktu }
# stop programowi     #      _________________         ##
#######################      koniec rick rolla         ##
    t = 2             #                                ##
#########################################################

def nice():
####################################
# folder                           #
# na obrazy                        #
####################################
    directoryZD = "obrazy"         #
# na dokumenty                     #
#   DirectoryDocks = "dokumenty"   #              TO DO
#####################################
# Rodziiiiiiccccc                  #
    parent_dir = "C:\Susy"       #
#####################################
#                                  ##
#############################################b
# tworzenie sciezki dla zdjęć      ##
    pathZD = os.path.join(parent_dir, directoryZD)
# tworzenie sciezki dla dokumentów ##
#    pathDOC = os.path.join(parent_dir, DirectoryDocks)         TO DO
############################################
#                                      ##
#########################################
#                tworzenie             ##
#             folderu z plikami        ##
#########################################
    docelowyZD = 'C:\Susy\obrazy'
#   docelowyDocs = 'C:\Susy\dokumenty'                   TO DO
#########################################
# kopiowaniee {                   ##
####################################
# kopiowanie zdjec                ##
####################################
    copy_tree(zd, docelowyZD)     ##
####################################
# kopiowanie dokumentów
####################################
#   copy_tree(docs, docelowyDocs) ##                     TO DO
####################################
# koniec }                        ##
####################################

nice()