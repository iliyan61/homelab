#!/bin/bash


# You Should Not Need To Edit Past This Line #
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

umount /media/backup
