# -*- coding: utf-8 -*-
import serial
import serial.tools.list_ports

def search_com_port():
    coms = serial.tools.list_ports.comports()
    comlist = []

    if(len(coms) == 0): return ""

    for com in coms:
        comlist.append(com.device)
    print('Connected COM ports: ' + str(comlist))
    use_port = comlist[0]
    print('Use COM port: ' + use_port)

    return use_port

def read_microbit():
    use_port = search_com_port()

    if( use_port == ""): return -1

    sp = serial.Serial(use_port)
    sp.baudrate = 115200
    sp.timeout = 1
    print("start")
    signal = sp.readline()

    return int(signal)

if __name__ == '__main__':
    while True:
        signal = read_microbit()
        if(signal == -1): 
            print("No Serial Device.")
            break
        print(signal)
