#!/bin/sh

PASS_PHRASE=$1
OWNER_ADDRESS=$2

USER=forta

function forta_register(){
    su - $USER -c "forta register --owner-address=$OWNER_ADDRESS --passphrase=$PASS_PHRASE"
}

function start_forta(){
    mkdir /etc/systemd/system/forta.service.d

    echo "[Service]
Environment='FORTA_DIR=/home/$USER/.forta'
Environment='FORTA_PASSPHRASE=$PASS_PHRASE'" > /etc/systemd/system/forta.service.d/env.conf

    systemctl daemon-reload
    systemctl enable forta
    systemctl start forta
}


forta_register

start_forta


