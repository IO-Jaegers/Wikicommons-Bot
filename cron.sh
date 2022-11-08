#!/usr/bin/env bash

if [ ! -d  "./.enviroment" ]
  then
    echo "enviroment is not installed"
  else
    source ./.enviroment/bin/activate
    python bootstrap.py
fi




