import numpy as np
import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import script1 as scr1
import sys

pi = 3.14

try:
    _time = float(input("Print period of time "))
    frequency = float(input("Print frequency "))
    samplingFrequency = float(input("Print sampling frequency "))
    time_ = np.arange(0, _time, 1 / samplingFrequency)
    amplitude = np.sin(2 * pi * frequency * time_)
    amplitude = (amplitude + 1) * (255 / 2)
    plt.plot(time_, amplitude)
    plt.title("SIN")
    plt.xlabel("Time")
    plt.ylabel("Amplitude sin(2 * pi * {} * time)".format(frequency))
    plt.show()
    c = int(input("Print 1 if you want to continue, else print -1 "))
    if c == -1:
        sys.exit()
    for i in range(len(amplitude)):
        scr1.all_out()
        scr1.num2dac(int(amplitude[i]))
        time.sleep(1 / samplingFrequency)
except TypeError:
    print("You must print numbers")
except Exception:
    print("Something went wrong...")
finally:
    scr1.all_out()
    print("Quit")
