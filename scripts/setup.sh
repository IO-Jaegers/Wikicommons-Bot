#!/usr/bin/env bash

cd ..

python3 -m venv .enviroment
source ./.enviroment/bin/activate

pip3 install -U setuptools

pip3 install requests
pip3 install wikitextparser
pip3 install pywikibot
