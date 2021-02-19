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
	0:["iliyans-cheese-grater-mac-pro.local","Mac Pro",1],
	1:["iliyan.pulseway.com","Pulseway",1],
	2:["iliyan.dev","Website",1],
	3:["pornhub.com","pornhub",1],
	4:["redtube.com","redtube",1],
	5:["onlyfans.com","onlyfans",1],
	6:["xhamster.com","xhamster",1],
	7:["8.8.8.8","Google DNS",1]
			}
 
while True:
	for x in range(8):
		# change the colour slightly whilst we are testing an IP address
		if pingdict[x][2]==0:
			set_pixel(x, 0, 0, 10)
		else:
			set_pixel(x, 0, 0, 10)
 		
		print("")
 		print("Ping?")

		show()
		# ping the IP address 
		response = os.system("ping -c 1 -W 2 " + pingdict[x][0]+ " >nul")
		if response == 0:
			set_pixel(x, 0, 10, 0)
			print 'pong', pingdict[x][1], ' is up'
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