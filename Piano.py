from selenium import webdriver
from pyautogui import *


driver=webdriver.Chrome('chromedriver.exe')

driver.get('https://poki.com/en/g/piano-tiles-2')
# Tile Coordinates
a1, b1= 463, 507
a2, b2= 531, 507
a3, b3= 592, 507
a4, b4= 658, 507
while True:
    # Tile 1
    pixel1=screenshot(region=(a1,b1,1,1))
    color1=pixel1.getcolors()
    # Tile 2
    pixel2=screenshot(region=(a2,b2,1,1))
    color2=pixel2.getcolors()
    # Tile 3
    pixel3=screenshot(region=(a3,b3,1,1))
    color3=pixel3.getcolors()
    # Tile 4
    pixel4=screenshot(region=(a4,b4,1,1))
    color4=pixel4.getcolors()
    # Tile Test
    if color1[0][1]==(1,1,1) or color1[0][1][0:2]==(0, 2,):
        press('D')
    if color2[0][1]==(1,1,1) or color2[0][1][0:2]==(0, 2):
        press('F')
    if color3[0][1]==(1,1,1) or color3[0][1][0:2]==(0, 2):
        press('J')
    if color4[0][1]==(1,1,1) or color4[0][1][0:2]==(0, 2):
        press('K')