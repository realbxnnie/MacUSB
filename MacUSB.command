#!/usr/bin/env sh

cd MacUSB;

python3 -m pip install -r ./requirements.txt;
clear;

sudo python3 ./__main__.py;