#!/usr/bin/python
from datetime import datetime
from time import sleep
from gpiozero import Button, LED #for the buttons connected to the GPIO-pins

# Set 4 doorbell-buttons connected to GPIO's 16, 18, 19 & 20, while 17 is connected to Ground
b26kaku = LED(26)
b12white = Button(12)

print('Started')
while True:
    if b12white.is_pressed:
        print('button connected to GPIO12 is pressed')
        b26kaku.on()
        print('Switched on at %s' % datetime.now().isoformat())
        sleep(1)
        b26kaku.off()
        print('Switched on at %s' % datetime.now().isoformat())
