#!/usr/bin/python
from datetime import datetime
from time import sleep
import urllib.request #to be able to test if internet is up. python2:urllib2
from gpiozero import Button, LED #for the buttons connected to the GPIO-pins

# Set 4 doorbell-buttons connected to GPIO's 16, 18, 19 & 20, while 17 is connected to Ground
b26kaku = LED(26)
b12white = Button(12)

print('Started')
while True:
    if b12white.is_pressed:
        print('White is connected')
        b26kaku.on()
        print('Switched on at %s' % datetime.now().isoformat())
        sleep(1)
        b26kaku.off()
        print('Switched on at %s' % datetime.now().isoformat())


#!/usr/bin/env python
# 
# import time
# import pigpio
# 
# LEDPin = 26
# buttonPin = 5
# 
# LEDOn = False
# minutesOn = 0
# 
# def callback(gpio, level, tick):
#    global minutesOn, LEDOn
#    if level == 0: # button press
#       if LEDOn:
#          print("LED off")
#          LEDOn = False
#          pi.write(LEDPin, 0)
#       else:
#          print("LED on")
#          LEDOn = True
#          pi.write(LEDPin, 1)
#          minutesOn = 0
#    elif level == pigpio.TIMEOUT:
#       if LEDOn:
#          minutesOn += 1
#          print("LED on for {} minutes".format(minutesOn))
#          if minutesOn >= 30:
#             print("LED off")
#             LEDOn = False
#             pi.write(LEDPin, 0)
# 
# pi = pigpio.pi()
# if not pi.connected:
#    exit()
# 
# # Setup the pin the LED is connected to
# pi.set_mode(LEDPin, pigpio.OUTPUT)
# 
# # Setup the button
# pi.set_mode(buttonPin, pigpio.INPUT)
# pi.set_pull_up_down(buttonPin, pigpio.PUD_UP)
# pi.set_glitch_filter(buttonPin, 5000) # 5000 micros debounce
# 
# pi.set_watchdog(buttonPin, 60000) # watchdog every minute
# 
# cb = pi.callback(buttonPin, pigpio.EITHER_EDGE, callback)
# 
# while True: # all the work is done in the callback
#    time.sleep(1)