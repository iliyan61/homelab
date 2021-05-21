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


`sudo systemctl daemon-reload`
`sudo systemctl start grafana`
`sudo systemctl status grafana`
`sudo systemctl enable grafana`


At this point we have Grafana installed and configured to start on boot. Let’s start exploring!
Using a browser, connect to the Grafana server: http://10.1.1.110:3000.
Grafana login
Grafana login
The account and password are: admin/admin. Grafana will ask you to change this password.
The first configuration to be made will be to create a data source that Grafana will use to collect metrics. Of course, this will be our Prometheus instance
Go to the configuration menu (the little gear icon) and select ‘Data Sources’.
Data Sources Menu
Data Sources Menu
The select ‘Add Data Source’ and then select Prometheus as that data source.
Add Data Source
Add Data Source
Now we get to configure some of the settings for our connection to Prometheus.
In this case we can set the URL as ‘http://localhost:9090’ (since both Prometheus and Grafana are installed on the same server), the scrape interval as ’15s’, the Query timeout as 60s and the http method as ‘GET’.
Then click on the ‘Save & Test button’.
Save & Test
Save & Test
We should get some nice ticks to indicate that the data source is working.
Data Sources Tick
Data Sources Tick
Great!
Now things start to get just a little bit exciting. Remember the metrics that were being sent out by Prometheus? Those were the metrics that report back on how Prometheus is operating. In other words, it’s the monitoring system being monitored. We are going to use that to show our first dashboard.
Here lies another strength of Grafana. Dashboards can be built and shared by users so that everyone benefits. We will import one such dashboard to show us how Prometheus is operating.
At the top of our ‘Data Sources / Prometheus’ settings screen there is a ‘Dashboards tab. Click on that to show some available dashboards for our Prometheus instance;
Import Prometheus Dashboard
Import Prometheus Dashboard
Click on the ‘Import’ button for the ‘Prometheus 2.0 Stats’ dashboard. We should recieve a little green tick notification telling us that it has been successful. Now click on the ‘Prometheus 2.0 Stats’ label itself and the dashboard will open.
First Dashboard




























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