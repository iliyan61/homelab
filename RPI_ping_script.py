#!/usr/bin/env python
import os
import time
from blinkt import set_brightness, set_pixel, show, clear
 
# clear the LEDs
set_brightness(0.1)
clear()
show()
 
# dictionary data format is - "IP", "description", status where 0 = up and 1 = down
pingdict = {
	0:["8.8.8.8","Google DNS ",1],
	1:["192.168.68.210","TestPI",1],
	2:["192.168.68.212","BrambleN0de1",1],
	3:["192.168.68.214","BrambleN0de2",1],
	4:["192.168.68.216","BrambleN0de3",1],
	5:["192.168.68.218","BrambleN0de4",1],
	6:["pornhub.com","Pornhub",1],
	7:["iliyan.dev","Website",1]
			}
 
while True:
	for x in range(8):
		# change the colour slightly whilst we are testing an IP address
		if pingdict[x][2]==0:
			set_pixel(x, 100, 0, 255)
		else:
			set_pixel(x, 100, 0, 255)
 
		show()
		# ping the IP address 
		response = os.system("ping -c 1 -W 2 " + pingdict[x][0]+ " >nul")
		if response == 0:
			set_pixel(x, 0, 10, 0)
			print pingdict[x][1], ' is up'
			pingdict[x][2]=0
		else:
			set_pixel(x, 10, 0, 0)
			print pingdict[x][1], ' is down'
			pingdict[x][2]=1
		show()
 
	  # pause for a few seconds then loop again
	time.sleep(2)
	print("")
	print("")
	print("")