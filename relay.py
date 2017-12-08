#!/usr/bin/python
import time
from RPi import GPIO
import re


def init(a):
    pass

def setpins():
    pins = [4]
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

def main():
    pins = [4]

    GPIO.setmode(GPIO.BCM)

    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    try:
        # setup initial pin state
        a = []
        c = False
        d = []
        while True:
            init(pins)
            b = False
            a = time.ctime().split(' ')
            d = a[4].split(':')
            int_d = int(d[1])
	    if int_d % 5 == 0 :
            #if re.match(r'^19\:00', a[4]):
                b = True
                c = True
            while b:
                for i in range(2):
                    for pin in pins:
                        GPIO.output(pin, GPIO.LOW)
                        time.sleep(0.5)
                        GPIO.output(pin, GPIO.HIGH)
                        time.sleep(0.5)
                a = time.ctime().split(' ')
		d = a[4].split(':')
                int_d = int(d[1])
                if int_d % 5 <> 0:
                #if re.match(r'^19\:15', a[4]):
                    b = False 

            if c == True:
                GPIO.cleanup()
                c = False
                setpins()

    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
