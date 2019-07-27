#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Zainab Adjiet
Student Number: ADJZAI001
Prac: Prac 1
Date: 27/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
import itertools as it

LEDs = (17, 27, 22)
btn_up = 18
btn_down = 23

values = list(it.product(range(2), repeat=3))
index = 0

# increment count on button push and change LEDs
def increment_count(channel):
    global index
    index = 0 if index == len(values)-1 else index+1

    on_LEDs = list(it.compress(LEDs, values[index]))
    off_LEDs = [a for a in LEDs if a not in on_LEDs]
    GPIO.output(on_LEDs, GPIO.HIGH)
    GPIO.output(off_LEDs, GPIO.LOW)

# decrement count on button push and change LEDs
def decrement_count(channel):
    global index
    index = len(values)-1 if index == 0 else index-1

    on_LEDs = list(it.compress(LEDs, values[index]))
    off_LEDs = [a for a in LEDs if a not in on_LEDs]
    GPIO.output(on_LEDs, GPIO.HIGH)
    GPIO.output(off_LEDs, GPIO.LOW)

# set up pins
def GPIO_setup():
    GPIO.setmode(GPIO.BCM)

    # setup LEDs
    GPIO.setup(LEDs, GPIO.OUT)
    GPIO.output(LEDs, GPIO.LOW)

    # setup increment button
    GPIO.setup(btn_up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(btn_up, GPIO.FALLING, callback=increment_count, bouncetime=200)

    # setup decrement button
    GPIO.setup(btn_down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(btn_down, GPIO.FALLING, callback=decrement_count, bouncetime=200)

# Logic that you write
def main():
    time.sleep(1)

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        GPIO_setup()
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
