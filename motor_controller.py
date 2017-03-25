
import RPi.GPIO as GPIO
import time

DEBUG = 1

# TODO add proper testing and cleanup stuff that im too bored to do

# class must suport:
#  > seting up the I/O
class MotorController:

    # maximum frequency as required by the chip
    max_freq = 500e3
    

    def __init__(self, pwm_pin, dir_pin, frequency, name="Anon"):

        self.set_name(name)
        self.set_pwm_pin(pwm_pin)
        self.set_dir_pin(dir_pin)
        self.set_frequency(frequency)

        self.setup_GPIO()

        self.pwm = None
        self.direction = 0

        

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
        freq = min(freq, self.max_freq)

        self.frequency = freq

        if DEBUG == 1:
            print "Setting the motor {0} controller frequenccy to {1}".format(self.name, freq)

    def setup_GPIO(self):

        pins = (self.pwm_pin, self.dir_pin)
        GPIO.setup(pins, GPIO.OUT)

    def set_direction(self, dir):

        #TODO: add security stuuff

        self.direction = dir
        GPIO.output(self.dir_pin, self.direction)

    def init_pwm(self):       

        # if PWM was already initialised, stop it to avoid unexpected behaviour
        if self.pwm is not None:
            self.stop()

        self.pwm = GPIO.PWM(self.pwm_pin, self.frequency)

    def go(self, speed = 0):
        
        if speed != 0:
            self.set_frequency(abs(speed))

        self.set_direction( 1 if speed > 0 else 0 )
        self.init_pwm()

        self.pwm.start(50)

    def stop(self):
        self.pwm.stop()

