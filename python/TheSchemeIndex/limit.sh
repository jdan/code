#!/bin/bash

racket -f $1 &
sleep $2
kill $! 2>/dev/null && echo "Out of time :("


