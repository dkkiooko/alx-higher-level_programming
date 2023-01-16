#!/bin/bash
# sends POST request for the body of response with various variables
curl "$1" -sX POST -d "email=test@gmail.com&subject=I wi
ll always be here for PLD" 
