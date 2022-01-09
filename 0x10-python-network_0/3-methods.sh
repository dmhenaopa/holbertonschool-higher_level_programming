#!/bin/bash
# A script that takes in a URL and displays all HTTP accepted
curl -s --head "$1" | grep "Allow" | cut -d ":" -f2 | sed 's/^\s//g'
