import script1 as sc1 
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


def all_out():
    GPIO.output(D, 0)


def num2dac(val):
    binary_string = bin(val)[2:].zfill(bin_depth)
    binary_array = [int(binary_string[bin_depth - 1 - i]) for i in range(bin_depth)]
    GPIO.output(D, binary_array)  


def guess():
    k = 0
    for i in range(bin_depth):
        k += 2 ** (bin_depth - 1 - i)
        num2dac(k)
        time.sleep(time_sleep)
        if GPIO.input(comp) == 0:
            k -= 2 ** (bin_depth - 1 - i)
    print(f'Digital value: {k}, ', 'Analog value :{0:.{1}f} V'.format(k * voltage_step, rounded))


if __name__ == '__main__':
    try:
        GPIO.output(V_pin, 1)
        while True:
            all_out()
            guess()
    except Exception:
        print('Something went wrong...')
    finally:
        print('Quit')
        all_out()
