from PIL import ImageGrab
import os
import time

import win32api, win32con

from PIL import ImageOps
from numpy import *

x_pad = 20
y_pad = 238

def screenGrab():
    box = (x_pad,y_pad,x_pad+640,y_pad+480)
    im = ImageGrab.grab(box)
    ##im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")          #completely optional. But nice for debugging purposes.

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('left Down')

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('left release')

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x-x_pad
    y = y-y_pad
    print(x,y)

def startGame():
    #location of first menu
    mousePos((329, 205))
    leftClick()
    time.sleep(.1)
     
    #location of second menu
    mousePos((319, 384))
    leftClick()
    time.sleep(.1)
     
    #location of third menu
    mousePos((588, 456))
    leftClick()
    time.sleep(.1)
     
    #location of fourth menu
    mousePos((317, 381))
    leftClick()
    time.sleep(.1)

class Cord:
     
    f_shrimp = (33,331)
    f_rice = (95,331)
    f_nori = (35,389)
    f_roe = (92, 387)
    f_salmon = (35, 443)
    f_unagi = (91, 443)

#-----------------------------------    

    phone = (580,350)
 
    menu_toppings = (540,270)
     
    t_shrimp = (500,220)
    t_nori = (500,275)
    t_roe = (575,275)
    t_salmon = (500,330)
    t_unagi = (575,220)
    t_exit = (584,335)
 
    menu_rice = (540,293)
    buy_rice = (545,280)
     
    delivery_norm = (493,294)

def clear_tables():
    mousePos((80,200))
    leftClick()
 
    mousePos((180,200))
    leftClick()
 
    mousePos((280,200))
    leftClick()
 
    mousePos((380,200))
    leftClick()
 
    mousePos((480,200))
    leftClick()
 
    mousePos((580,200))
    leftClick()
    time.sleep(1)

def foldMat():
    mousePos((Cord.f_rice[0]+40,Cord.f_rice[1])) 
    leftClick()
    time.sleep(.1)

def makeFood(food):
    if food == 'caliroll':
        print('Making a caliroll')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1)
     
    elif food == 'onigiri':
        print('Making a onigiri')
        foodOnHand['rice'] -= 2 
        foodOnHand['nori'] -= 1 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()         
        time.sleep(1)
 
    elif food == 'gunkan':
        print('Making a gunkan')
        foodOnHand['rice'] -= 1 
        foodOnHand['nori'] -= 1 
        foodOnHand['roe'] -= 2 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1)

def buyFood(food):
     
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(0.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(0.05)
        leftClick()
        time.sleep(0.1)
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (127, 127, 127):
            print('rice is available')
            mousePos(Cord.buy_rice)
            time.sleep(0.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(0.1)
            leftClick()
            time.sleep(1)
        else:
            print('rice is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        time.sleep(0.1)
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (53, 53, 39):
            print('nori is available')
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(1)
        else:
            print('nori is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
 
    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        time.sleep(0.1)
        s = screenGrab()
         
        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (101, 13, 13):
            print('roe is available')
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10 
            time.sleep(.1)
            leftClick()
            time.sleep(1)
        else:
            print('roe is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print('%s is low and needs to be replenished' % i)
                buyFood(i)

def get_seat_one():
    box = (46,299,46+61,299+14)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_two():
    box = (147,299,147+61,299+14)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    #im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_three():
    box = (248,299,248+61,299+14)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    #im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_four():
    box = (349,299,349+61,299+14)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    #im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_five():
    box = (450,299,450+61,299+14)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    #im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_six():
    box = (551,299,551+61,299+14)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    #im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

sushiTypes = {1817:'onigiri', 
              2461:'caliroll',
              1824:'gunkan',}

class Blank:
    seat_1 = 6434
    seat_2 = 5832
    seat_3 = 10536
    seat_4 = 10228
    seat_5 = 6290
    seat_6 = 8689

def check_bubs():
 
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if s1 in sushiTypes:
            print('table 1 is occupied and needs %s' % sushiTypes[s1])
            makeFood(sushiTypes[s1])
        else:
            print('sushi not found!\n sushiType = %i' % s1)
 
    else:
        print('Table 1 unoccupied')
 
    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if s2 in sushiTypes:
            print('table 2 is occupied and needs %s' % sushiTypes[s2])
            makeFood(sushiTypes[s2])
        else:
            print('sushi not found!\n sushiType = %i' % s2)
 
    else:
        print('Table 2 unoccupied')
 
    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if s3 in sushiTypes:
            print('table 3 is occupied and needs %s' % sushiTypes[s3])
            makeFood(sushiTypes[s3])
        else:
            print('sushi not found!\n sushiType = %i' % s3)
 
    else:
        print('Table 3 unoccupied')
 
    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if s4 in sushiTypes:
            print('table 4 is occupied and needs %s' % sushiTypes[s4])
            makeFood(sushiTypes[s4])
        else:
            print('sushi not found!\n sushiType = %i' % s4)
 
    else:
        print('Table 4 unoccupied')
 
    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if s5 in sushiTypes:
            print('table 5 is occupied and needs %s' % sushiTypes[s5])
            makeFood(sushiTypes[s5])
        else:
            print('sushi not found!\n sushiType = %i' % s5)
 
    else:
        print('Table 5 unoccupied')
 
    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if s6 in sushiTypes:
            print('table 1 is occupied and needs %s' % sushiTypes[s6])
            makeFood(sushiTypes[s6])
        else:
            print('sushi not found!\n sushiType = %i' % s6)
 
    else:
        print('Table 6 unoccupied')
 
    clear_tables()

def reset():

    foodOnHand['shrimp'] = 5
    foodOnHand['rice'] = 10
    foodOnHand['nori'] = 10
    foodOnHand['roe'] = 10
    foodOnHand['salmon'] = 5
    foodOnHand['unagi'] = 5

def main():
    reset()
    startGame()
    while True:
        check_bubs()