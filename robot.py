from gpiozero import Button,LED,OutputDevice
from time import sleep
import curses

led = LED(26)
button = Button(23)
speedR = OutputDevice(18)
speedL = OutputDevice(17)
in1 = OutputDevice(20)
in2 = OutputDevice(21)
in3 = OutputDevice(12)
in4 = OutputDevice(16)

def stop():
    speedL.value = 0
    speedR.value = 0
    in1.off()
    in2.off()
    in3.off()
    in4.off()

def speed():
    speedL.value = 1
    speedR.value = 1

def forward():
    speed()
    in1.on()
    in2.off()
    in3.on()
    in4.off()
    
def reverse():
    speed()
    in1.off()
    in2.on()
    in3.off()
    in4.on()

def left():
    speed()
    in1.off()
    in2.on()
    in3.on()
    in4.off()
    

def right():
    speed()
    in1.on()
    in2.off()
    in3.off()
    in4.on()

def main(window):
    next_key = None
    while True:
##        print("running curses control")
        curses.halfdelay(6)
        key = window.getch()
                    
        print("key:{}".format(key))
        if key == 259:
            led.on()
            curses.halfdelay(1)
            reverse()
        if key == 258:
            curses.halfdelay(1)
            forward()
        if key == 260:
            curses.halfdelay(1)
            left()
        if key == 261:
            curses.halfdelay(1)
            right()
        if key == -1:
            stop()
            led.off()
curses.wrapper(main)






##count = 0
##while True:
##    speedL.value = 0.5
##    speedR.value = 0.5
##    
##    if button.is_pressed:
##        led.on()
##        forward()
##        print("Button is pressed")
##    else:
##        reverse()
##        led.off() 
##        count+=1
##        print("Button is not pressed:{}".format(count))
##    sleep(0.1)
