#!/bin/bash
# bet cURL body size
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
