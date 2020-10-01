#!/bin/bash

echo $HOSTNAME
uname -o
uname -r
uname -a

cat /etc/os-release | grep PRETTY_NAME
cat /etc/debian_version 
echo "this is a testing display !!!"