#!/bin/bash
# A script that takes in a URL, with a header variable X-School-User-Id value 98
curl -s -H "X-School-User-Id: 98" "$1"
