#!/bin/bash
# bet cURL body size 
url=$1
curl -s $"url" | wc -c
