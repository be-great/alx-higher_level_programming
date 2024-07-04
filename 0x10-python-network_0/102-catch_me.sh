#!/bin/bash
# bet cURL body size
curl -s -L -X PUT "0.0.0.0:5000/catch_me" -d "user_id=98" >/dev/null 2>&1
