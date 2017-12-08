#!/usr/bin/python
import time
from RPi import GPIO

def init(a):
    pass

def main():
    pins = [4]

    GPIO.setmode(GPIO.BCM)

    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    try:
        # setup initial pin state
        init(pins)

        for i in range(2):
            for pin in pins:
                GPIO.output(pin, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(0.5)

        GPIO.cleanup()

    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
