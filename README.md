# Centos-Fastapi-loguru-promtail-loki-grafana
Centos-Fastapi-loguru-promtail-loki-grafana

## Install wget and tar
```
yum install wget
yum install tar
yum install zip unzip
```

## Download grafana
```
https://grafana.com/grafana/download
```

Standalone Linux Binaries
```
wget https://dl.grafana.com/enterprise/release/grafana-enterprise-9.3.6.linux-amd64.tar.gz
tar -zxvf grafana-enterprise-9.3.6.linux-amd64.tar.gz
```

## Start grafana
```
cd grafana-9.3.6
cd bin
grafana-server
```

```
sudo firewall-cmd --permanent --zone=public --add-port=3000/tcp
systemctl restart firewalld
go to chrome and check ip:3000 on the url
```

Login grafana
```
admin|admin
```
Change the password after login
```
admin|123456
```

## Download loki and promtail
Choose the zip file of loki and download
```
https://github.com/grafana/loki/releases/
```

```
curl -O -L "https://github.com/grafana/loki/releases/download/v2.7.3/loki-linux-amd64.zip"
# extract the binary
unzip "loki-linux-amd64.zip"
# make sure it is executable
chmod a+x "loki-linux-amd64"
```

```
curl -O -L https://github.com/grafana/loki/releases/download/v2.7.3/promtail-linux-amd64.zip
# extract the binary
unzip "promtail-linux-amd64.zip"
# make sure it is executable
chmod a+x "promtail-linux-amd64.zip"
```

## Download loki configuration
```
wget https://raw.githubusercontent.com/grafana/loki/master/cmd/loki/loki-local-config.yaml
```

start loki
```
./loki-linux-amd64 -config.file=loki-local-config.yaml
```

Open firewall
```
sudo firewall-cmd --permanent --zone=public --add-port=3100/tcp
systemctl restart firewalld
```

## Download promtail configuration
```
wget https://raw.githubusercontent.com/grafana/loki/main/clients/cmd/promtail/promtail-local-config.yaml
```

start promtail
```
./promtail-linux-amd64 -config.file=promtail-local-config.yaml
```

Open firewall
```
sudo firewall-cmd --permanent --zone=public --add-port=9080/tcp
systemctl restart firewalld
```

```
go to chrome and check ip:9080 on the url
```


## Go to grafana
```
Homepage -> data source -> loki -> ip:3100
```

```
Back to homepage -> /explore
```