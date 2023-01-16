#!/bin/bash
# takes in a URL, sends a GET and displays body of only 200 status code response
curl -sL "$1"
