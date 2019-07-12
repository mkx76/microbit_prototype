# -*- coding: utf-8 -*-
import serial
import serial.tools.list_ports

def search_com_port():
    coms = serial.tools.list_ports.comports()
    comlist = []
    for com in coms:
        comlist.append(com.device)
    print('Connected COM ports: ' + str(comlist))
    use_port = comlist[0]
    print('Use COM port: ' + use_port)

    return use_port

if __name__ == '__main__':
    use_port = search_com_port()

    sp = serial.Serial(use_port)
    sp.baudrate = 115200
    sp.timeout = 1
    print("start")
    while True:
        # print("loop")
        signal = sp.readline()
        print(int(signal))

