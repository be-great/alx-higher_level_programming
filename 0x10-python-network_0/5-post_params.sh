#!/bin/bash
# bet cURL body size
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
