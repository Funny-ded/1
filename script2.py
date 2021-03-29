import script1 as scr1
import RPi.GPIO as GPIO
import time


try:
    repetitionsNumber = int(input("Print number of repetitions "))
    if repetitionsNumber <= 0:
        raise Exception
    for _ in range(repetitionsNumber):
        for i in range(2 ** scr1.bin_depth):
            scr1.all_out()
            scr1.num2dac(i)
            time.sleep(scr1.time_to_sleep)
        for i in range(2 ** scr1.bin_depth, -1, -1):
            scr1.all_out()
            scr1.num2dac(i)
            time.sleep(scr1.time_to_sleep)
except TypeError:
    print("Number of repetitions must be an integer")
except Exception:
    print("Something went wrong...")
finally:
    scr1.all_out()
    print("Quit")