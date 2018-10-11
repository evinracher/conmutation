#! /usr/bin/env python

import serial, serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())

for p in ports:
    if p[1] == 'Arduino Mega':
        print p
        arduino = serial.Serial(p[0], 9600)
        time.sleep(2)
        break

CRAZY_SIGNAL = '>'

file_names = ['coordenadas.txt', 'ruta.txt']

arduino.write(CRAZY_SIGNAL + '\n')

for file_name in file_names:
    print('file: ' + file_name)
    file = open(file_name, 'r')

    for line in file.readlines():
        print('line: ' + line)
        while arduino.read() != CRAZY_SIGNAL:
            pass
        arduino.write(line)

    arduino.write(CRAZY_SIGNAL + '\n')
    file.close()
