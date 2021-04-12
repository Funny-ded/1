import RPi.GPIO as GPIO
import time


D = [10, 9, 11, 5, 6, 13, 19, 26]
comp = 4
V_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(V_pin, GPIO.OUT)
voltage_step = 3.3 / 255
rounded = 2
bin_depth = 8
time_sleep = 0.001


def num2dac(val):
    binary_string = bin(val)[2:].zfill(bin_depth)
    binary_array = [int(binary_string[bin_depth - 1 - i]) for i in range(bin_depth)]
    GPIO.output(D, binary_array)    


def all_out():
    GPIO.output(D, 0)


def guess():
    for i in range(2 ** bin_depth):
        num2dac(i)
        time.sleep(time_sleep)
        if GPIO.input(comp) == 0:
            return f'{0.15 * i}V'


if __name__ == '__main__':
    try:
        GPIO.output(V_pin, 1)
        while True:
            value = int(input('Enter value (-1 to exit) > '))
            all_out()
            if value == -1:
                break
            if value < 0 or value > 255:
                raise Exception
            num2dac(value)
            print(f'{value} = ' + '{0:.{1}f}'.format(value * voltage_step, rounded))
    # except TypeError:
    #     pass
    # except Exception:
    #     pass
    finally:
        all_out()
        print('Quit')
