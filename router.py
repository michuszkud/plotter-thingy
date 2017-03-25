import motor_controller
import RPi.GPIO as GPIO
import time


def toImpulses(dist):
	# units in mm
	wheel_diameter = 28
	impulses_per_rotation = 16*200

	rotations = dist / (PI*wheel_diameter)

	impulses = impulses_per_rotation * rotations

	return impulses


def translate(x, y):

	#units in mm

	width = 600
	length = 1000

	x_offset = 200
	y_offset = 200

	xL_tot = x + x_offset
	yL_tot = y + y_offset

	xR_tot = 2*x_offset + width - x
	yR_tot = 2*y_offset + lenght - y

	left  = (xL_tot**2 + yL_tot)**0.5
	right = (xR_tot**2 + yR_tot)**0.5


	return (left, right)

def step(l_dest, r_dest, l_cur, r_cur, time):

	l_step = l_dest - l_cur
	r_step = r_dest - r_cur

	# l_dir = l > 0
	# r_dir = r > 0

	# l_step = abs(l_step)
	# r_step = abs(r_step)

	l_pulse = toImpulses(l_step)
	r_pulse = toImpulses(r_step)

	l_freq = l_pulse / time
	r_freq = r_pulse / time

	left.go(l_freq)
	right.go(r_freq)

	sleep(time)


	left.stop()
	right.stop()
	#stop motors

	return (l_dest, r_dest)

X = [0, 0, 100, 100]
Y = [0, 100, 100, 0]


freq = 5000

l_cur = 0
r_cur = 0

GPIO.setmode(GPIO.BOARD)

left = MotorControler(35, 33, freq/3, "Left")
right = MotorControler(37, 31, freq, "Right")

for i in range(len(X)):
	(l_cur, r_cur) = step(X[i], Y[i], l_cur, r_cur, 5)


