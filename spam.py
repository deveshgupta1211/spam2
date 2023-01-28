import pyautogui as pg
import time

# speed = input('0.25')
# time.sleep(3)
txt = open('animals2.txt', 'r')

a = "@wait7850 is a"

for i in txt:
    pg.write(a+ ' '+i)
    pg.press('Enter')
 