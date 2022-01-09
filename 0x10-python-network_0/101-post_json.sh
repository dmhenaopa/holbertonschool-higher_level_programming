#!/bin/bash
# A script that sends a POST request and displays the body of response
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
