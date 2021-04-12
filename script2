import RPi.GPIO as GPIO
import time
import script1 as sc1


def guess(last_i):
    if not GPIO.input(sc1.comp):
        for i in range(last_i, -1, -1):
            sc1.num2dac(i)
            time.sleep(sc1.time_sleep)
            if GPIO.input(sc1.comp) == 1:
                print(f'Digital value: {i}, ', 'Analog value :{0:.{1}f} V'.format(i * sc1.voltage_step, sc1.rounded))
                return i
    for i in range(last_i, 2 ** sc1.bin_depth):
        sc1.num2dac(i)
        time.sleep(sc1.time_sleep)
        if GPIO.input(sc1.comp) == 0:
            print(f'Digital value: {i}, ', 'Analog value :{0:.{1}f} V'.format(i * sc1.voltage_step, sc1.rounded))
            return i


if __name__ == '__main__':
    try:
        GPIO.output(sc1.V_pin, 1)
        last = 0
        while True:
            sc1.all_out()
            last = guess(last)
    except Exception:
        pass
    finally:
        print('Quit')
        sc1.all_out()
