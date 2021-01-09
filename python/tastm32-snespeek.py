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

input("Press any key to begin peeking")

while True:
	ser.write(b'K') #J for proper read, K for "just read portb"
	data=ser.read(2)
	print(''.join(format(ord(chr(byte)), '08b') for byte in data) + " aka " + str(bytes(data)))
	time.sleep(0.1)
