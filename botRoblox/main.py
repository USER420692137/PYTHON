import time
from time import sleep
import pyautogui as pg
from sqlalchemy import true
import keyboard

a = 0

def start_move():
    pg.keyDown('w')

    time.sleep(1)
    pg.keyDown('d')
    time.sleep(1)
    pg.keyUp('d')

    pg.keyDown('s')
    time.sleep(1)
    pg.keyUp('s')

    pg.keyUp('w')

def checkLevel():
    pg.moveTo(212,820, duration=0.1)
    time.sleep(0.2)
    pg.click(button='left')
    pg.moveTo(412,820, duration=0.1)
    time.sleep(0.2)
    pg.click(button='left')
    print('checkLevel')

def mining():
    pg.keyDown('w')
    time.sleep(1)
    pg.keyUp('w')
    pg.click(button='left')
    pg.click(button='left')
    print('mining')

def mining_b():
    pg.keyDown('s')
    time.sleep(1)
    pg.keyUp('s')
    pg.click(button='left')
    pg.click(button='left')
    print('mining')

time.sleep(2)

start_move()
while true:
    a += 1

    if a == 120000:
        a = 0
        start_move()
    if a == 30000:
       mining_b

    checkLevel()
    mining()

