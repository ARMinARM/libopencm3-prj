#!/bin/bash

if [ -d libopencm3 ]; then
	echo "Directory libopencm3 exists: updating"
	cd libopencm3
	git pull
else
	echo "First time git clone: installing libopencm3"
	git clone https://github.com/libopencm3/libopencm3
	cd libopencm3
fi

make lib/stm32/f1

cd ..
