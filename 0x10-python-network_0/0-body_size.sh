#!/bin/bash
# displays size of the body of a URL (arg[1] in shell)
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
