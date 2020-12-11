# homelab
Project timeline and such for my PI server 

# SCP
scp pi@192.168.68.212:/home/pi/test.txt /Users/iliyanjivraj/


# SSH

	Check for existing keys: ls ~/.ssh
	
	Generate new keys: ssh-keygen

	Move key to remote machine: ssh-copy-id <USERNAME>@<IP-ADDRESS>

	Erase from known hosts: ssh-keygen -R <USERNAME>@<IP-ADDRESS>

# VNC FIX
	All on pi:
		sudo raspi-config

		sudo vncpasswd -service

		sudo nano /etc/vnc/config.d/common.custom
			Put this in that: Authentication=VncAuth

		sudo systemctl restart vncserver-x11-serviced


# Setting up headless PI's

	Config.txt
		Put this in that: dtoverlay=dwc2

	touch ssh

	cmdline.txt

		console=serial0,115200 console=tty1 root=PARTUUID=##PUTUUIDHERE##-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2,g_ether quiet init=/usr/lib/raspi-config/init_resize.sh

# RNDIS fix
	sudo nano /etc/modprobe.d/rndis.conf
		options g_ether host_addr=**RANDOM MAC HERE** dev_addr=**MAC OF HOST MACHINE**


# Give the Pi's WiFi back
sudo rfkill unblock wifi



# Sudo nano /etc/dhcpcd.conf
interface eth0
static ip_address=192.168.68
static routers=192.168.68.1
static domain_name_servers=192.168.68.1