#!/bin/bash
# bet cURL body size 
curl -s "$1" | wc -c
