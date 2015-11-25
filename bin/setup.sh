#!/bin/bash -e

LOG_FILE=/tmp/setup.log

echo "Updating the apt-get cache..."
apt-get update 1>>$LOG_FILE 2>>&1

echo "Installing apt-based libraries..."
sudo apt-get install -y build-essential python-dev git scons swig python-pip python-dev build-essential libffi-dev libssl-dev 1>>$LOG_FILE 2>>&1

echo "Installing Pi-NeoPixel libs..."
cd /home/pi
git clone https://github.com/jgarff/rpi_ws281x.git >>$LOG_FILE 2>>&1
cd rpi_ws281x
scons >>$LOG_FILE 2>>&1
cd python
python setup.py install >>$LOG_FILE 2>>&1

echo "Installing additional python libs..."
pip install requests[security] >>$LOG_FILE 2>>&1
