import serial
import time

ser = serial.Serial("COM1", 115200)
ser.timeout = 3.0

# PANEL COMMUNICATION

## utility function for panel communication. 
## Computes a packet checksum.
def checksum(arr: bytearray):
    chksm = (~(sum(arr)))&255
    chksm += 1
    chksm = chksm & 255
    return chksm

## utility function for panel communication.
## Sends a command by appending the correct checksum and writing to serial port
def send_command(arr: bytearray):
    #print("Sending command")
    #print(arr)
    #print("length is " + hex(len(arr)))
    command = arr
    chksm = checksum(arr)
    #print("checksum is " + hex(chksm))
    command.append(chksm)
    ser.write(command)

# Slider init procedure
# Init the panel by sending the reset and hw info commands.
def slider_init() -> bool:
    print("Slider init")
    send_command(bytearray([0xff,0x10,0x00]))
    s = ser.read(4)
    #print(s)
    if s == b'\xff\x10\x00\xf1':
        print("    Reset ok")
    else:
        print("    Reset not ok")
        return False

    send_command(bytearray([0xff,0xf0,0x00]))
    s = ser.read(22)
    #print(s)
    if s == b'\xff\xf0\x1215330   \xa006712\xfd\xfe\x90\x00d':
        print("    HW info ok")
        return True
    else:
        print("    HW info not ok")
        return False

# COLOR TEST

## Panel color test, checks that red, green and blue leds are working for all keys and separators
def color_test():
    print("Color test")
    print("    Send red")
    send_led(127,0,0)
    time.sleep(1)
    print("    Send green")
    send_led(0,127,0)
    time.sleep(1)
    print("    Send blue")
    send_led(0,0,127)
    time.sleep(1)
    print("    Turn off")
    send_led(0,0,0)

## utility function for color_test. Lights the whole panel with the given rgb color
def send_led(red: int, green: int, blue: int):
    command = bytearray([0xff,0x02,0x5e,0x7f])
    for x in range(31):
        command.append(blue)
        command.append(red)
        command.append(green)
    send_command(command)

# IO TEST

## Panel IO test, checks that every zone is working by starting the auto scan loop and generating reactive lights
def input_test():
    print("I/O Test (press CTRL+C to exit)")
    send_command(bytearray([0xff,0x03,0x00]))
    touch_data = bytearray(32)
    while True:
        retrieve_input(touch_data)
        send_led_reactive(touch_data)

## utility function for input_test, fill a bytearray with data read from serial    
def retrieve_input(input_data: bytearray):
    # locate and skip sync byte (0xff)
    s = ser.read(1)
    if s != b'x\ff':
        while s != b'\xff':
            s = ser.read(1)
    while s == b'\xff':
        s = ser.read(1)
    
    # check command type (should be 0x01)
    if s != b'\x01':
        print("unexpected value")
        return
    s = ser.read(1)
    
    # check packet length (should be 0x20)
    if s != b' ':
        print("unexpected packet length")
        print(s)
        return
    
    # fill touch data bytearray
    for x in range(32):
        s = ser.read(1)
        input_data[x] = s[0]

    # consume checksum byte (no check)
    s = ser.read(1)
    
    return

## utility function for input_test, light the panel according to touch input data :
## - separators are always lit in purple
## - keys are lit in green (when top zone is touched) or orange (when bottom zone is touched)
def send_led_reactive(input_data: bytearray):
    command = bytearray([0xff,0x02,0x5e,0x7f])
    for x in range(31):
        # separators
        if x & 1:
            command.append(0x7f)
            command.append(0x23)
            command.append(0)           
        # top zone
        elif input_data[x]:
            command.append(0x23)
            command.append(0)
            command.append(0x7f)
        # bottom zone
        elif input_data[x+1]:
            command.append(0)
            command.append(0x7f)
            command.append(0x23)
        # untouched key
        else:
            command.append(0)
            command.append(0)
            command.append(0)
    send_command(command)

# main program
if slider_init() == False:
    print("Cannot communicate with panel. Exiting.")
    quit()

color_test()
input_test()
