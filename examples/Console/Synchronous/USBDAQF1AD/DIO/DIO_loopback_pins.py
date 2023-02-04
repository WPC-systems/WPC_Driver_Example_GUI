'''
DIO - DIO_loopback_pins.py with synchronous mode.

This example demonstrates how to write DIO loopback in pins from USBDAQF1AD.
Use DO pins to send signals and use DI pins to receive signals on single device also called "loopback".

First, it shows how to open DO and DI in pins.
Second, write DO pin and read DI pin
Last, close DO and DI in pins.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd.
All rights reserved.
'''

## Python

import time

## WPC

from wpcsys import pywpc

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1AD()

    ## Connect to device
    try:
        dev.connect("21JA1245")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Parameters setting
        port = 0
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])
 
        ## Open pin0, pin1, pin2, pin3 and pin4 with digital output
        err = dev.DO_openPins(port, [0,1,2,3,4], timeout)
        print("DO_openPins:", err)

        ## Set pin0 and pin1 to high, others to low
        all_pin_state = dev.DO_writePins(port, [0,1,2,3,4], [1,1,0,0,0], timeout)
        print("DO_writePins:", all_pin_state)

        ## Open pin5, pin6 and pin7 with digital output
        err = dev.DI_openPins(port, [5,6,7], timeout)
        print("DI_openPins:", err)

        ## Read pin5, pin6 and pin7 state
        state_list = dev.DI_readPins(port, [7,5,6], timeout)
        print(f"state_list {state_list}")

        ## Close pin0, pin1, pin2, pin3 and pin4 with digital output
        err = dev.DO_closePins(port, [0,1,2,3,4], timeout)
        print("DO_closePins:", err)

        ## Close pin5, pin6 and pin7 with digital input
        err = dev.DI_closePins(port, [5,6,7], timeout)
        print("DI_closePins:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return
    
if __name__ == '__main__':
    main()