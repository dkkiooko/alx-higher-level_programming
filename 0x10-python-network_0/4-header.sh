#!/bin/bash
# sends a GET request with a unique Header variable (id)
curl -sX GET H "X-School-User-Id:98" "$1"
