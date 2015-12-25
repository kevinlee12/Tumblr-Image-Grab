#!/bin/bash

if [ -z $1 ]; then
  USERNAME=huachenyufan
else
  USERNAME=$1
fi

rm -f canvas.py
echo "Things are going to happen"
python3 main.py $USERNAME
python3 canvas.py
