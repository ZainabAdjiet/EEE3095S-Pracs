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

LED = 17
btn = 18

# toggle LED on button push
def toggle_LED(channel):
    GPIO.output(LED, not GPIO.input(LED))

# set up pins
def GPIO_setup():
    GPIO.setmode(GPIO.BCM)

    # setup LEDs
    GPIO.setup(LED, GPIO.OUT)

    # setup button
    GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(btn, GPIO.FALLING, callback=toggle_LED, bouncetime=200)

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
