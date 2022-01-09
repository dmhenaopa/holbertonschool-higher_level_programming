#!/bin/bash
# A script that displays only the status of the code
curl -s -o /dev/null -w "%{http_code}" "$1"
