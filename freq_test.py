
import RPi.GPIO as GPIO
import time

# PWM frequency in Hz
freq = 1

t_min = 2e-6

freq = 1/t_min

step_pin = 37
dir_pin = 7



GPIO.setmode(GPIO.BOARD)

# Pin numbering as on the breakout board
# Looking at the board from top with USB facing downwards
# PIN1 -> Top left corner
# PIN2 -> top right corner etc


GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)

while freq > 0:
    
    # Create new PWM instance
    pwm = GPIO.PWM(step_pin, freq)


    # start PWM with 50% duty cycle
    pwm.start(50)

    inp = input("Set the frequency: ")

    if not inp.isdigit():
        inp = 0
    else:
        freq = int(inp)

    pwm.stop()



pwm.stop()

GPIO.cleanup()

