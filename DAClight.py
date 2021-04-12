import RPi.GPIO as GPIO
import time


D = [10, 9, 11, 5, 6, 13, 19, 26]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(D, GPIO.OUT)
bin_depth = 8
time_to_sleep = 0.05


def num2dac(val):
    binary_string = bin(val)[2:].zfill(bin_depth)
    for i in range(bin_depth):
        GPIO.output(D[i], int(binary_string[bin_depth - 1 - i]))


def all_out():
    for i in range(bin_depth):
        GPIO.output(D[i], 0)


if __name__ == '__main__':
    try:
        while True:
            value = int(input("Print value(-1 to exit)"))
            all_out()
            if value == -1:
                break
            if value < 0 or value > 255:
                raise Exception
            num2dac(value)
            time.sleep(0.3)
    except TypeError:
        print("You must print integers")
    except Exception:
        print("Something went wrong...")
    finally:
        all_out()
        print("Quit")
