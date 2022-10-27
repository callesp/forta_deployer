#!/bin/sh

systemctl stop forta

systemctl disable forta

yum remove -y docker-ce docker-ce-cli containerd.io docker-compose-plugin forta

rm -rf /etc/docker

userdel -r forta