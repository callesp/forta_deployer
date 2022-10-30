#!/bin/sh

# kill -9 `ps axu | grep inst_stage* | grep -v grep | awk '{print $2}'`
# kill -9 `ps axu | grep clean.sh* | grep -v grep | awk '{print $2}'`

systemctl stop forta

systemctl disable forta

yum remove -y docker-ce docker-ce-cli containerd.io docker-compose-plugin forta

rm -rf /etc/docker

rm -rf /etc/systemd/system/forta.service.d

userdel -r forta