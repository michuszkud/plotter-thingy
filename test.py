
import RPi.GPIO as GPIO
import time

DEBUG = 1

# TODO add proper testing and cleanup stuff that im too bored to do

# class must suport:
#  > seting up the I/O
class MotorControler:

    # maximum frequency as required by the chip
    max_freq = 500e3
    

    def __init__(self, pwm_pin, dir_pin, frequency, name="Anon"):

        self.pwm = None;
        self.set_name(name)
        self.set_pwm_pin(pwm_pin)
        self.set_dir_pin(dir_pin)
        self.set_frequency(frequency)

        

    def set_name(self, name):
        self.name = str(name)

    

    #TODO add proper testing
    def set_pwm_pin(self, pin):
        if pin >= 0 and pin <= 40:
            self.pwm_pin = pin
            if DEBUG == 1:
                print "Setting the motor {0} controller pin to {1}".format(self.name, pin)
        else:
            self.pwm_pin = -1
            if DEBUG == 1:
                print "Error assigning the motor {0} controller pin - wrong value ({1})!".format(self.name, pin)

    #TODO add proper testing
    def set_dir_pin(self, pin):
        if pin >= 0 and pin <= 40:
            self.dir_pin = pin
            if DEBUG == 1:
                print "Setting the motor {0} controller pin to {1}".format(self.name, pin)
        else:
            self.pwm_pin = -1
            if DEBUG == 1:
                print "Error assigning the motor {0} controller pin - wrong value ({1})!".format(self.name, pin)

    def set_frequency(self, freq):

        # limit the frequency to [0, max_freq] 

        freq = max(freq, 0)
        freq = min(freq, max_freq)

        self.frequency = freq

        if DEBUG == 1:
            print "Setting the motor {0} controller frequenccy to {1}".format(self.name, freq)

    def setup_GPIO(self):

        pins = (self.pwm_pin, self.dir_pin, self)
        GPIO.setup(pins, GPIO.OUT)

    def init_pwm(self):       

        # if PWM was already initialised, stop it to avoid unexpected behaviour
        if self.pwm is not None:
            self.pwm.stop()

        self.pwm = GPIO.PWM(self.pwm_pin, self.frequency)

        

    

# PWM frequency in Hz
freq = 1

t_min = 2e-6

freq = 1/t_min/1000

step_pin = 37
dir_pin = 3



GPIO.setmode(GPIO.BOARD)

# Pin numbering as on the breakout board
# Looking at the board from top with USB facing downwards
# PIN1 -> Top left corner
# PIN2 -> top right corner etc


GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)

# Create new PWM instance
pwm = GPIO.PWM(step_pin, freq)

# start PWM with 50% duty cycle
pwm.start(50)

time.sleep(60)

pwm.stop()

GPIO.cleanup()

