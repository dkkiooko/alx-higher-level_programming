#!/bin/bash
# sends POST request for the body of response with various variables
curl -sd "email=test@gmail.com&subject=I%20wi
ll%20always%20be%20here%20for%20PLD" -X POST "$1"

