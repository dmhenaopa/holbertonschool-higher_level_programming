#!/bin/bash
# A script that sends a POST request and displays the body of response
curl -s -d "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" -X POST "$1"
