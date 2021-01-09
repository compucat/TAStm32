#!/usr/bin/env python3
import serial, time
import serial_helper
import argparse_helper
import tastm32
import uinput

parser = argparse_helper.audio_parser()
args = parser.parse_args()

if args.serial == None:
    dev = tastm32.TAStm32(serial_helper.select_serial_port())
else:
    dev = tastm32.TAStm32(args.serial)

# connect to device
ser = dev

vjoy = uinput.Device((uinput.ABS_X, uinput.ABS_Y, uinput.BTN_SELECT, uinput.BTN_START, uinput.BTN_DPAD_UP, uinput.BTN_DPAD_DOWN, uinput.BTN_DPAD_LEFT, uinput.BTN_DPAD_RIGHT, uinput.BTN_TL, uinput.BTN_TR, uinput.BTN_NORTH, uinput.BTN_EAST, uinput.BTN_WEST, uinput.BTN_SOUTH))

ser.write(b'I')
time.sleep(0.1)
print(ser.read(2))

lastdata=0b1111111111111111
while True:
	ser.write(b'J') #J for proper read, K for "just read portb"
	data=ser.read(2)
	out=""
	if(data==b''): continue
	else:
		mappings = {
		0b10000000: uinput.BTN_DPAD_RIGHT,
		0b01000000: uinput.BTN_DPAD_LEFT,
		0b00100000: uinput.BTN_DPAD_DOWN,
		0b00010000: uinput.BTN_DPAD_UP,
		0b00001000: uinput.BTN_START,
		0b00000100: uinput.BTN_SELECT,
		0b00000010: uinput.BTN_WEST, #y
		0b00000001: uinput.BTN_SOUTH #bb
		}
		for key in mappings.keys():
			if (data[0] & key) == 0:
				#out += mappings[key]+" "
				vjoy.emit_click(mappings[key])

		mappings2 = {
		0b00001000: uinput.BTN_TR,
		0b00000100: uinput.BTN_TL,
		0b00000010: uinput.BTN_NORTH, #x
		0b00000001: uinput.BTN_EAST #a
		}
		for key in mappings2.keys():
			if (data[1] & key) == 0:
				#out += mappings[key]+" "
				vjoy.emit_click(mappings2[key])
		#	else:
		#		k.release(mappings[key])

		#if (data[1] & 0b00000001) == 0:	out+="A "
		#if (data[1] & 0b00000010) == 0:out+="X "
		#if (data[1] & 0b00000100) == 0:	out+="L "
		#if (data[1] & 0b00001000) == 0:out+="R "
		#print(''.join(format(ord(chr(byte)), '08b') for byte in data) + " aka " + str(bytes(data)))
		#print(out)
		time.sleep(0.01)
