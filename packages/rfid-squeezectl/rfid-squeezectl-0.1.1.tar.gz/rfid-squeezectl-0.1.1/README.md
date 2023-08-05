# Control Logitech Squeezebox using RFID tags

This software is relying on https://github.com/ondryaso/pi-rc522.

## Setup

    sudo raspi-config nonint do_spi 0
    sudo reboot
    sudo apt install python3-venv
    python3 -m venv --system-site-packages ~/rfid-squeeze
    . ~/rfid-squeeze/bin/activate
    pip install rfid-squeezectl
    rfid-squeezectl host:port player_id

## Develop

    pip install bump2version
    bumpversion patch
    git push && git push --tags
