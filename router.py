
def toImpulses(dist):
	wheel_diameter
	pass

def translate(x, y):
	width = 100.0
	length = 100.0

	x_offset = 10.0
	y_offset = 10.0

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

	l_dir = l > 0
	r_dir = r > 0

	l_step = abs(l_step)
	r_step = abs(r_step)

	l_pulse = toImpulses(l_step)
	r_pulse = toImpulses(r_step)

	l_freq = l_pulse / time
	r_freq = r_pulse / time

	# move motors at frequencies

	sleep(time)

	#stop motors

	return (l_dest, r_dest)


l_cur = 0
r_cur = 0

