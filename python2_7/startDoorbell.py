#!/usr/bin/python
import tkinter as tk 
import urllib2
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from gpiozero import Button
from Ringer import FamilyOrFriend, Salesman, Deliverer, HansOrGrietje
from RingerSingleButton import SingleButton

EMAIL = 'timvans@gmail.com'

b7red = Button(7)
# Set 4 doorbell-buttons connected to GPIO's 16, 18, 19 & 20, while 17 is connected to Ground
b21blue = Button(21)
b20yellow = Button(20)
b16green = Button(16)
b12white = Button(12)

# Initialize the LCD plate.  
# try:
#     lcd = Adafruit_CharLCDPlate()
#     lcd.clear()
lcdIsOperational = True
# except:
#     lcdIsOperational = False

if lcdIsOperational:  # Clear display and show greeting, pause 1 sec
#     lcd.clear()
#     lcd.backlight(lcd.ON)
#     lcd.message("Welcome to your\nDOORBELL")
    print("Welcome to your\nDOORBELL")
else:
    print("LCD is not operational")

class FullScreenApp(object):
    padding=3
    dimensions="{0}x{1}+0+0"

    def __init__(self, master, **kwargs):
        self.master=master
        width=master.winfo_screenwidth()-self.padding
        height=master.winfo_screenheight()-self.padding
        master.geometry(self.dimensions.format(width, height))
# For variations of the button see:
# https://www.tutorialspoint.com/python/tk_button.htm
        img = tk.PhotoImage(file="/home/pi/doorbell/images/ancient.png")

#         b = tk.Button(self.master, command=lambda: self.pressed("b"))
#         b = tk.Label(self.master, image=img).pack()
#         b.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

        b = tk.Button(self.master, text="Duw dan, deliverer! ", command=lambda: self.pressed("b"))
        b.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

    def pressed(self, buttonname):
        if buttonname == "a":
            ringer = FamilyOrFriend()
            print("clicked button a!")
        if buttonname == "b":
            ringer = Deliverer()
            print("clicked button b!")
        

def internet_on():


    """This function tests if there is a connection to the internet.
    Will return a boolean, true when connected, false if there is no connection."""
    try:
        urllib2.urlopen('http://www.google.com', timeout=10)
        return True
    except urllib2.URLError:
        pass
    return False


# lcd.clear()
if internet_on():
    print('Internet is up')
    # lcd.message("Internet is set\nup :)")
else:
    print('Internet is down')
    # lcd.message("No internet use\nDoorbell wifi")

root=tk.Tk()
root.wm_attributes('-fullscreen','true')

app=FullScreenApp(root)

root.mainloop()


while True:
    doorbell_pressed = False
    while not doorbell_pressed:
        if b21blue.is_pressed:
            ringer = FamilyOrFriend()
            doorbell_pressed = True
        if b20yellow.is_pressed:
            ringer = Salesman()
            doorbell_pressed = True
        if b16green.is_pressed:
            ringer = Deliverer()
            doorbell_pressed = True
        if b12white.is_pressed:
            ringer = HansOrGrietje()
            doorbell_pressed = True
        if b7red.is_pressed:
            ringer = SingleButton()
            doorbell_pressed = True
    if doorbell_pressed:
        ringer.respond()
