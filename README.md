# ChunithmIO

Use a Chunithm control panel on PC

# Overview

The Chunithm panel is made of air towers and a touch slider.

## Air towers

The air towers are made of 6 photo interrupters and 2 led strips which can be interfaced with an arduino. See `ChunithmIO` for a firmware example which turns them into a keyboard device.

## Touch slider

The touch slider is an rs232 device and can be connected directly to the PC for native use. This repo contains a python script to help verify correct wiring. See `slidertest` folder readme for more info.

# Advanced usage

A better featured PCB is in the works allowing custom light effects, use of the touch slider as an HID compliant touchpad for use with android games, etc... more info coming soon.

# pinout

Diagrams coming soon.

## slider

### YLP-03V (connects into an YLR-03V)

This is the power input connector. Goes to a 12V wall PSU.

- Yellow is +12V. Goes to wall PSU +12V.
- Black is GND. Goes to wall PSU GND.
- Green is EARTH. Can be left disconnected.

### SMR-04V (connects into an SMP-04V)

This is the serial input/output connector. Goes to your RS232 adapter.

- White is RX (db9 pin 2)
- Red is TX (db9 pin 3)
- Black is GND (db9 pin 5)

## air tower

### YLP-15V (connects into an YLR-15V)

This is the air strings connector 

- 1 RED: to arduino +5V.
- 2~7 stripped grey: to the other tower pins 2~7.
- 8~10 stripped white: to the arduino gpio 8 9 10 (left tower) or 11 12 13 (right tower).
- 11~12 black: to arduino GND.
- 15 green: Can be left disconnected.

### YLP-06V (connects into an YLR-06V)

This is the ledstrip connector. Needs a 12V wall PSU.

- Yellow is +12V. Goes to wall PSU +12V.
- White with stripes is LED data. Goes to arduino gpio 5 (left tower) or 6 (right tower).
- Black is GND. Goes to wall PSU GND and arduino GND.

Leds are ws2811 in RGB order, with 9 leds per strip.
