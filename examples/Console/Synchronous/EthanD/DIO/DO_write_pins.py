'''
DIO - DO_write_pins.py with synchronous mode.

This example demonstrates how to write DO in pins from EthanD.

First, it shows how to open DO in pins.
Second, write DO pin in two different types (hex or list) but it should be consistency.
Last, close DO in pins.

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
        pin_index = [0,1,2,3,4]
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open pin0, pin1, pin2, pin3 and pin4 with digital output.
        err = dev.DO_openPins(port, pin_index, timeout=timeout)
        print(f"DO_openPins in port {port}: {err}")

        ## Set pin0, pin1 to high, others to low.
        all_pin_state =  dev.DO_writePins(port, pin_index, [1,1,0,0,0], timeout=timeout)
        print(f"DO_writePins in port {port}: {all_pin_state}")

        ## Open pin5, pin6 and pin7 with digital output (1110 0000 in binary) (0xE0 in hex).
        err = dev.DO_openPins(port, 0xE0, timeout=timeout)
        print(f"DO_openPins in port {port}: {err}")

        ## Set pin7 and pin6 to high, others to low (1100 0000 in binary) (0xC0 in hex).
        err = dev.DO_writePins(port, 0xE0, 0xC0, timeout=timeout)
        print(f"DO_writePins in port {port}: {err}")

        ## Wait for 1 seconds to see led status
        time.sleep(1) ## delay [s]

        ## Close pin0, pin1, pin2, pin3 and pin4 with digital output.
        err = dev.DO_closePins(port, pin_index, timeout=timeout)
        print(f"DO_closePins in port {port}: {err}")

        ## Close pin5, pin6 and pin7 with digital output.
        err = dev.DO_closePins(port, 0xE0, timeout=timeout)
        print(f"DO_closePins in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()