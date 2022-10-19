#!/bin/sh

function time_sync(){
    systemctl enable systemd-timesyncd
    systemctl start systemd-timesyncd

    timedatectl status
}


function install_docker(){
    yum remove docker \
        docker-client \
        docker-client-latest \
        docker-common \
        docker-latest \
        docker-latest-logrotate \
        docker-logrotate \
        docker-engine

    yum install -y yum-utils

    yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

    yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin

    echo '{
   "default-address-pools": [
        {
            "base":"172.17.0.0/12",
            "size":16
        },
        {
            "base":"192.168.0.0/16",
            "size":20
        },
        {
            "base":"10.99.0.0/16",
            "size":24
        }
    ]
}' > /etc/docker/daemon.json

    systemctl start docker
}


function install_forta(){
    curl https://dist.forta.network/repositories/yum/Forta.repo -o /etc/yum.repos.d/Forta.repo -s

    yum install forta
}

install_docker()

install_forta()