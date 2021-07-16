# homelab
A repo of all the stuff I need for my HomeLab.







# PSSH
```
pssh -h pssh_hosts -l pi -i -t 1 -v 
	sudo apt-get -y upgrade
	uptime
```




    Create the .ssh directory:

    mkdir ~/.ssh

    Set the right permissions:

    chmod 700 ~/.ssh

    Create the authorized_keys file:

    touch ~/.ssh/authorized_keys

    Set the right permissions:

    chmod 600 ~/.ssh/authorized_keys

