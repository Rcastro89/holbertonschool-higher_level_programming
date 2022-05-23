#!/bin/bash
# Escriba un script Bash que tome una URL, envíe una solicitud POST a la URL pasada y muestre el cuerpo de la respuesta.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
