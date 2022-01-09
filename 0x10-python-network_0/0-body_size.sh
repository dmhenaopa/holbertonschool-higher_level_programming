#!/bin/bash
# A script that displays the size of the body of the response of a request
curl -s --head "$1" | grep "Content-Length:" | cut -d " " -f2
