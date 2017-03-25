
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

        self.set_name(name)
        self.set_pwm_pin(pwm_pin)
        self.set_dir_pin(dir_pin)
        self.set_frequency(frequency)

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

        pins = (self.pwm_pin, self.dir_pin, self)
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

        self.pwm(start(50))

    def stop(self):
        self.pwm.stop()



# 31 33 35 37

# l pwm >> 35
# l dir -> 33

# r dir >> 37
# r pwm >> 31
    

# PWM frequency in Hz
freq = 1

t_min = 2e-6

freq = 1/t_min/100

step_pin = 35
dir_pin = 33

GPIO.setmode(GPIO.BOARD)

left = MotorControler(35, 33, freq, "Left")
right = MotorControler(31, 37, freq, "Right")



# Pin numbering as on the breakout board
# Looking at the board from top with USB facing downwards
# PIN1 -> Top left corner
# PIN2 -> top right corner etc


# GPIO.setup(dir_pin, GPIO.OUT)
# GPIO.setup(step_pin, GPIO.OUT)

# Create new PWM instance
# pwm = GPIO.PWM(step_pin, freq)

# start PWM with 50% duty cycle
# pwm.start(50)

left.go()
right.go()

time.sleep(3)

pwm.stop()

GPIO.cleanup()

