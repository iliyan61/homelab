# homelab
A repo of all the stuff I need for my HomeLab.

# SCP
```
scp pi@192.168.68.2XX:/home/pi/test.txt /Users/iliyanjivraj/
```


# SSH
```
Check for existing keys: ls ~/.ssh
	
Generate new keys: ssh-keygen

Move key to remote machine: ssh-copy-id <USERNAME>@<IP-ADDRESS>

Erase from known hosts: ssh-keygen -R <USERNAME>@<IP-ADDRESS>
```


# VNC FIX
```
sudo raspi-config

sudo vncpasswd -service

sudo nano /etc/vnc/config.d/common.custom
	Put this in that: Authentication=VncAuth

sudo systemctl restart vncserver-x11-serviced
```


# Setting up headless PI's
```
Config.txt
	Put this in that: dtoverlay=dwc2

touch ssh

cmdline.txt

	console=serial0,115200 console=tty1 root=PARTUUID=##PUTUUIDHERE##-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2,g_ether quiet init=/usr/lib/raspi-config/init_resize.sh
```


# RNDIS fix
```
sudo nano /etc/modprobe.d/rndis.conf
	options g_ether host_addr=**RANDOM MAC HERE** dev_addr=**MAC OF HOST MACHINE**
```


# Give the Pi's WiFi back
```
sudo rfkill unblock wifi
```


# Sudo nano /etc/dhcpcd.conf
```
interface eth0
static ip_address=192.168.68.
static routers=192.168.68.1
static domain_name_servers=192.168.68.1
```


# PSSH
```
pssh -h pssh_hosts -l pi -i -t 1 -v 
	sudo apt-get -y upgrade
	uptime
```


# Backups
```
sudo mkdir /media/backup

sudo mount.cifs //Iliyans-Cheese-Grater-Mac-Pro.local/BrambleX /media/backup -o user=pi

sudo nano /usr/local/bin/pibackup.sh

Use this to make it an executable sudo chmod +x /usr/local/bin/pibackup.sh 

```
[Backup Guide 1](https://polargeek.com/network-backup-your-raspberry-pi/)

[Backup Guide 2](https://www.linux-tips-and-tricks.de/en/quickstart-rbk/)


# Mount SMB 
[guide](https://www.raspberrypi.org/documentation/remote-access/samba.md)

```
sudo mount.cifs //<hostname or IP address>/share /home/pi/windowshare -o user=<name>
```


# Print CPU temp on prompt

```
get_cpu_temp() {
  cpuTemp=$( /opt/vc/bin/vcgencmd measure_temp | sed "s/[^0-9.]//g" )
  echo "[$cpuTemp]"
}
old_PS1=$PS1
PROMPT_COMMAND='PS1="$(get_cpu_temp) $old_PS1"'
```



get_cpu_temp() {
  cpuTemp=$( /usr/bin/vcgencmd measure_temp | sed "s/[^0-9.]//g" )
  echo "[$cpuTemp]"
}
old_PS1=$PS1
PROMPT_COMMAND='PS1="$(get_cpu_temp) $old_PS1"'




sudo apt update -y && sudo apt upgrade -y

ZFS Rebuild:
https://jordanelver.co.uk/blog/2018/11/26/how-to-replace-a-failed-disk-in-a-zfs-mirror/


http://www.d3noob.org/2020/02/installing-nodeexporter-for-monitoring.html


Grafana commmands:

sudo nano /home/pi/prometheus/prometheus.yml
sudo systemctl restart prometheus


Python Service shit


Blinkt 1

sudo nano /etc/systemd/system/blinkt.service
[Unit]                                                                                                                       
# Human readable name of the unit                                                                                    
Description=Blinkt Script

[Service]
# Command to execute when the service is started
ExecStart=/usr/bin/python /home/pi/RPI_ping_script.py



systemctl daemon-reload
sudo systemctl start blinkt.service
sudo systemctl status blinkt.service








Blinkt 2

sudo nano /etc/systemd/system/blinkt.service
[Unit]                                                                                                                       
# Human readable name of the unit                                                                                    
Description=Blinkt Script

[Service]
# Command to execute when the service is started
ExecStart=/usr/bin/python /home/pi/RPI_ping_script2.py



systemctl daemon-reload
sudo systemctl start blinkt.service
sudo systemctl status blinkt.service