#!/bin/bash

echo 21 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio21/direction

while [ 1 ]
    do
        echo 1 > /sys/class/gpio/gpio21/value
        sleep 0.2s
        echo 0 > /sys/class/gpio/gpio21/value
        sleep 0.2s
    done