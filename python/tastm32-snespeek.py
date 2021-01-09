#!/usr/bin/env python3
import serial, time
import serial_helper
import argparse_helper
import tastm32

parser = argparse_helper.audio_parser()
args = parser.parse_args()

if args.serial == None:
    dev = tastm32.TAStm32(serial_helper.select_serial_port())
else:
    dev = tastm32.TAStm32(args.serial)

# connect to device
ser = dev

ser.write(b'I')
time.sleep(0.1)
print(ser.read(2))

while True:
	ser.write(b'J') #J for proper read, K for "just read portb"
	data=ser.read(2)
	out=""
	if(data==b''): continue
	else:
		if (data[0] & 0b10000000) == 0: out+="RIGHT "
		if (data[0] & 0b01000000) == 0: out+="LEFT "
		if (data[0] & 0b00100000) == 0: out+="DOWN "
		if (data[0] & 0b00010000) == 0: out+="UP "
		if (data[0] & 0b00001000) == 0: out+="START "
		if (data[0] & 0b00000100) == 0: out+="SELECT "
		if (data[0] & 0b00000010) == 0: out+="Y "
		if (data[0] & 0b00000001) == 0: out+="B "
		if (data[1] & 0b00000001) == 0: out+="A "
		if (data[1] & 0b00000010) == 0: out+="X "
		if (data[1] & 0b00000100) == 0: out+="L "
		if (data[1] & 0b00001000) == 0: out+="R "
		#print(''.join(format(ord(chr(byte)), '08b') for byte in data) + " aka " + str(bytes(data)))
		print(out)
		time.sleep(0.01)
