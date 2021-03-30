#!/bin/bash


# You Should Not Need To Edit Past This Line #
sudo mount.cifs //Iliyans-Cheese-Grater-Mac-Pro.local/Bramble2 /media/backup -o user=pi,password=###
hname=`hostname`
BackupDir=/media/backup

 
# Check for backup directory, if not found create it #
directory_check () {
echo "Checking for "$BackupDir" and creating if missing"
[ ! -d "$BackupDir" ] && mkdir -p "$BackupDir"
}
 
 
# Do something else below #


directory_check

echo "Starting Backup"
dd if=/dev/mmcblk0 of=${BackupDir}/$(date +%Y-%m-%d).img bs=1M status=progress
echo "Backup Complete"

source /usr/local/bin/pishrink.sh ${BackupDir}/$(date +%Y-%m-%d).img

echo "PiShrink complete"

umount /media/backup