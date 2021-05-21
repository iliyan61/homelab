Grafana+Prometheus+Node_exporter HowTO

Pi Server:
http://www.d3noob.org/2020/02/installing-prometheus-and-grafana-on.html

`sudo apt-get update -y && sudo apt-get upgrade`

`wget: **NEWEST ONE FROM HERE: https://prometheus.io/download/**`
`tar xfz prometheus**WHATEVER VERSION**`
`rm prometheus**WHATEVER VERSION**`
`mv prometheus**WHATEVER VERSION** prometheus/`


`sudo nano /etc/systemd/system/prometheus.service`
    Put this in that:
        [Unit]
        Description=Prometheus Server
        Documentation=https://prometheus.io/docs/introduction/overview/
        After=network-online.target

        [Service]
        User=pi
        Restart=on-failure

        #Change this line if Prometheus is somewhere different
        ExecStart=/home/pi/prometheus/prometheus \
        --config.file=/home/pi/prometheus/prometheus.yml \
        --storage.tsdb.path=/home/pi/prometheus/data



        [Install]
        WantedBy=multi-user.target




`sudo systemctl daemon-reload`
`sudo systemctl start prometheus`
`sudo systemctl status prometheus`
`sudo systemctl enable prometheus`

`wget **NEWEST ONE FROM HERE: https://grafana.com/grafana/download?platform=arm**`

`tar xfz grafana **WHATEVER VERSION**`
`rm grafana **WHATEVER VERSION**`
`mv grafana **WHATEVER VERSION** grafana/`

`sudo nano /etc/systemd/system/grafana.service`
    Put this in that:

        [Unit]
        Description=Grafana Server
        After=network.target

        [Service]
        Type=simple
        User=pi
        ExecStart=/home/pi/grafana/bin/grafana-server
        WorkingDirectory=/home/pi/grafana/
        Restart=always
    RestartSec=10

        [Install]
        WantedBy=multi-user.target


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