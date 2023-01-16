#!/bin/bash
# sends POST request for the body of response with various variables
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
