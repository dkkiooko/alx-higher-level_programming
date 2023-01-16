#!/bin/bash
# takes URL and displays all HTTP methods allowed
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
