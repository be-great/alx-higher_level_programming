#!/bin/bash
# bet cURL body size
curl -s -I -X OPTIONS "$1" | grep Allow
