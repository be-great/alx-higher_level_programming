#!/bin/bash
# bet cURL body size
curl -s -o /dev/null -w "%{http_code}" "$1"
