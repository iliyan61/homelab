Grafana+Prometheus+Node_exporter HowTO

Pi Server:
http://www.d3noob.org/2020/02/installing-prometheus-and-grafana-on.html


EzPz DNS stuff:
    sudo apt install iptables-persistent
    sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 3000
    iptables-save > /etc/iptables/rules.v4
    sudo iptables-save > /etc/iptables/rules.v4
    sudo nano
    sudo nano /etc/iptables/rules.v4
    iptables-save > /etc/iptables/rules.v4
    sudo iptables-save > /etc/iptables/rules.v4
    sudo iptables-save
    iptables -t nat -L


Ubuntu:
https://rm-rf.id/install-node-exporter-for-prometheus-grafana-on-ubuntu-20-04/


Pi:
http://www.d3noob.org/2020/02/installing-nodeexporter-for-monitoring.html






Grafana commmands:

sudo nano /home/pi/prometheus/prometheus.yml
sudo systemctl restart prometheus


