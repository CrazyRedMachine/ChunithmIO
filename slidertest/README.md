# ChunithmIO Slider test

This sample python script will allow you to check your chunithm slider is working correctly and is properly connected to your computer 

## Features

- This will test the slider init sequence

- A color test will check that your panel can display red, green and blue correctly

- An input test with reactive lights will check that your panel can read touch input correctly

## How to use

- Connect your slider via a rs232 to usb adapter (check pinout)
- Set port to COM1 using device manager
- Unplug/replug to check it is still on COM1
- (if applicable) Install python 3 on your system
- (if applicable) Run `pip install pyserial` to install the pyserial library
- Run `python3 slidertest.py`
- Press Ctrl+C to exit

## Slider pinout

### YLP-03V (connects into an YLR-03V)

This is the power input connector. Goes to a 12V wall PSU.

- Yellow is +12V
- Black is GND
- Green is EARTH

### SMR-04V (connects into an SMP-04V)

This is the serial input/output connector. Goes to your RS232 adapter.

- White is RX (db9 pin 2)
- Red is TX (db9 pin 3)
- Black is GND (db9 pin 5)
