#!/bin/bash
# bet cURL body size
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
