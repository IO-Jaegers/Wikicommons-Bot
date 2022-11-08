#!/usr/bin/env bash
# Setup of enviroment
python3 -m venv venv

source ./venv/bin/activate

pip install -U setuptools
pip install requests
pip install pywikibot
pip install wikitextparser

