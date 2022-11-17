#!/bin/sh

PASS_PHRASE=$1
OWNER_ADDRESS=$2


function forta_register(){
    su - $USER -c "forta register --owner-address=$OWNER_ADDRESS --passphrase=$PASS_PHRASE"
}

function forta_start(){
    systemctl start forta
}


forta_register

forta_start