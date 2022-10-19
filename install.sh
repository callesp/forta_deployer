#!/bin/sh

PASS_PHRASE=$1
OWNER_ADDRESS=$2
USER=forta

# Enable and start time sync service.
function time_sync(){
    systemctl enable systemd-timesyncd
    systemctl start systemd-timesyncd

    timedatectl status
}


# Install docker on centos7.
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

    yum install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

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


#Install forta on centos7.
function install_forta(){
    curl https://dist.forta.network/repositories/yum/Forta.repo -o /etc/yum.repos.d/Forta.repo -s

    yum install -y forta
}

# Create forta user and add it in docker group.
function create_user(){
    useradd -m forta
    usermod -aG docker $USER
}


# Initialize forta.
function forta_init(){
    su - $USER -c "forta init --passphrase=$PASS_PHRASE"
}


# Config forta.
function config_forta(){
    echo "forta config"
}

function start_forta(){
    echo "[Service]
Environment='FORTA_DIR=/home/forta/.forta'
Environment='FORTA_PASSPHRASE=$PASS_PHRASE'" > /etc/systemd/system/forta.service.d/env.conf

    systemctl daemon-reload
    systemctl enable forta
    systemctl start forta
}


function forta_register(){
    su - $USER -c "forta register --owner-address=$OWNER_ADDRESS --passphrase=$PASS_PHRASE"
}

install_docker

install_forta

create_user

forta_init

config_forta