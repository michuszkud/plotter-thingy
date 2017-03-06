#!/usr/bin/env python3
import sys,time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import svgpathtools
from math import sqrt

area_width = 800
area_height = 600
border = 20

# TODO: Add way to place location of motor shaft in relation to board
left_shaft = complex(0,0)
right_shaft = complex(area_width,0)

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, xlim=(-border,area_width+border), ylim=(-border,area_height+border))
# Mae origin top left corner
ax.invert_yaxis()
# Plot x axis on top of plot
ax.xaxis.tick_top()

# Draw Border
ax.plot([0,area_width,area_width,0,0],[0,0,area_height,area_height,0],'-',lw=0.5)

chains, = ax.plot([],[],'o-')
line, = ax.plot([],[],'-')
line_x = []
line_y = []

# List of arguments which will be passed to the animate function.
# Something like a list of (x,y) tuples would be good?
# frames = range(100)

input_file = 'drawing.svg'
paths, style = svgpathtools.svg2paths(input_file)

paths = paths[0].continuous_subpaths() # Created a list of continous paths

# print("path is continuous? ", paths.iscontinuous())
# print("path is closed? ", paths.isclosed())

points = []
# res sets the resolution
res = 0.25
for path in paths:
    for seg in path:
        for p in np.arange(0,1.001,res):
            points.append(seg.point(p))


arm_left_len = [abs(point - left_shaft) for point in points]
arm_right_len = [abs(point- right_shaft) for point in points]

frames = points

# print("Number of points in drawing: ",len(points))
# print(arm_left_len[:10])
# print(points[:10])

def calc_len(p1, p2):
	
	return

def animate(i):
    # print(i)
#     x = i[0].real
#     y = i[0].imag

    x = i.real
    y = i.imag

    line_x.append(x)
    line_y.append(y)


    chains.set_data([0,x,area_width],[0,y,0])
    line.set_data(line_x,line_y)
    return


def init():
    line_x = []
    line_y = []
    return

def DrawDickbutt():

	ani = FuncAnimation(fig, animate, frames, repeat=False, init_func=init, interval=25)

	plt.show()

def step(motor):
	print('Doing Step for motor:', str(motor))
	return

if __name__=='__main__':
	step_size = 50

	possible_length_l = np.arange(0,sqrt(area_height**2 + area_width**2),step_size)
	possible_length_r = np.arange(0,sqrt(area_height**2 + area_width**2),step_size)

	possible_xy = []
	for l in possible_length_l:
		for r in possible_length_r:
			if l+r > area_width:
				
				possible_xy.append(complex(l,r))

	


