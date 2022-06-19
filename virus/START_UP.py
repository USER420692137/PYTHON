import keyboard
import time
from pyautogui import alert
import os
import shutil
import random
import turtle
from pobDOk import susy, nice

#############################
#          SKROTY           #
#############################
#             F4            #
F4Alert = "alt + f4"        #
#           HASLO           #
unRealPassWord = "1 + 4 + 7"#
#############################

###########################
# LICZNIK FUNKCJI         #
###########################
licznik = 0               #
###########################

#######################
# GEJE dla            #
# funkcji             #
#######################
gej1 = 0              #
gej2 = 2              #
#######################

##############################################################################################
#                                    SŁOWNICTWO DO ALERTÓW                                   #
##############################################################################################
gituwa = ['gej', 'hej' , 'lamus', 'lol', 'i jak?', 'pozdro', 'siuuu', 'letss goo', 'siuuur']##
##############################################################################################

def PobDok():
  susy()

while True:
############################################
# zabezpieczenia od alt + f4 ( wredna suka )
###########################################
# ZEBY NIE BYŁO ŁATWO                     #
###########################################
  alert(text=random.choice(gituwa), title='IMPOSTOR', button='OK')
  if keyboard.is_pressed(F4Alert):
    alert(text='BEZ F4 FRAJERZE', title='F4 => NULL', button='KU#$$#%')
#####################################################################
  
#######################################
# kod zabezpieczeń
# by mozna było wyjsc
# na wszelki
#########################################
  if keyboard.is_pressed(unRealPassWord):
    quit()
#########################################
  
###############
# Magia      ###
###############
  
#########################
# dzien swira ( siuuur)###
#########################
  if licznik == gej1:
##############################################
# WALIMY FULL SCREEENNN                      #
##############################################
    screen = turtle.Screen()                 #
    screen.setup(width = 1.0, height = 1.0)  #
##############################################
    
#########################################
# rysunek
# sprzetu
#########################################
    board = turtle.Turtle()
    board.color("black")
    board.pensize(10)
    board.penup()
    board.setpos(20,-66)
    board.pendown()
    board.circle(80)
    turtle.setup(100,100)
    board.penup()
    board.setpos(180,-66)
    board.pendown()
    board.circle(80)
    board.penup()
    board.setpos(150,85)
    board.pendown()
    board.left(90)
    board.forward (300)
    board.circle(50,180)
    board.forward(300)
    board.penup()
    board.pencolor("black")
    board.setpos(100,427)
    board.pendown()
    board.forward(30)
    board.left(90)
    board.pencolor("black")
    board.pensize(8)
    board.forward (50)
    board.left (180)
    board.forward (100)
###########################################
# letss goo                               #
###########################################
#                                        #
    gej1 += 100 # określenie kolejnego fiuta #
#                                        #
###########################################
# poleceniomat                           ##
#############################################
  licznik += 1                             ##
#############################################

#############################################################
# trzeba więciej razy sie upewniać bo kto to wie         ###
# długi czas działania pętli = więcej martwego czasu XD  ##
##########################################################
# na wszelki wypadek by nie zamknol         ######   ####
# programu                                ####   #####
##########################################################
  if keyboard.is_pressed(F4Alert):
    alert(text='BEZ F4 FRAJERZE', title='F4 => NULL', button='KU#$$#%')
    alert(text='BEZ F4 FRAJERZE', title='F4 => NULL', button='KU#$$#%')

################################################################
# sprawdzanie po koleji                                        ###
# informujemy o zaszłej sytuacji                                ###
#   XXDDDDDDDDDDDDDDDDDD                                       ###
#################################################################
  if licznik == 1:#                                              ############
    alert(text='KOMP ZOSTAŁ PRZEJĘTY', title='IMPOSTORvirus', button='SUS')#
    alert(text='POZDRO', title='IMPOSTORvirus', button='K%$^$%^#^')##########
##################################################################

##################################################################
##                      RICKKK ROOOLLLL                         ##
##################################################################
  if licznik == gej2:
    PobDok()
#####################################
    gej2 += 200                     #
#####################################
# POWYŻEJ ZMIANA NASTĘPNEGO         #
#####################################
##          RICK ROOOLLA           ##
#####################################
##        POBIERANIE DANYCH        ##
#####################################
  if licznik == 3:
    nice()