'''
DIO - DIO_loopback_port.py with synchronous mode.

This example demonstrates how to write DIO loopback in port from EthanD.
Use DO pins to send signals and use DI pins to receive signals on single device also called "loopback".

First, it shows how to open DO and DI in port.
Second, write DO in port and read DI in port
Last, close DO and DI in port.

--------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## Python

import time

## WPC

from wpcsys import pywpc

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanD()

    ## Connect to device
    try:
        dev.connect("192.168.1.110") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0 ## Depend on your device
        DO_port = 0
        DI_port = 1
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        
        ## Get port mode
        port_mode = dev.Sys_getPortMode(port, timeout=timeout)
        print("Slot mode:", port_mode)

        ## If the port mode is not set to "DIO", set the port mode to "DIO"
        if port_mode != "DIO":
            err = dev.Sys_setPortDIOMode(port, timeout=timeout)
            print(f"Sys_setPortDIOMode in port {port}: {err}")

        ## Get port mode
        port_mode = dev.Sys_getPortMode(port, timeout=timeout)
        print("Slot mode:", port_mode)

        ## Get port DIO start up information
        info = dev.DIO_loadStartup(DO_port, timeout=timeout)
        print("Enable:   ", info[0])
        print("Direction:", info[1])
        print("State:    ", info[2])

        ## Write DO port to high or low
        err = dev.DO_writePort(DO_port, [1, 0, 1, 0], timeout=timeout)
        print(f"DO_writePort in port {DO_port}: {err}")

        ## Read DI port state
        state_list = dev.DI_readPort(DI_port, timeout=timeout)
        print(f"state_list in port {DI_port}: {state_list}")

        
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()