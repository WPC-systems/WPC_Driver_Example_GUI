'''
DIO - DO_blinky_pins.py with synchronous mode.

This example demonstrates how to write DO high or low in pins from USBDAQF1AOD.

First, it shows how to open DO in pins.
Second, each loop has different voltage output so it will look like blinking.
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
    dev = pywpc.USBDAQF1AOD()

    ## Connect to device
    try:
        dev.connect("default") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0 ## Depend on your device
        pinindex = [0,1]
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open pin0 and pin1 with digital output
        err = dev.DO_openPins(port, pinindex, timeout=timeout)
        print(f"DO_openPins in port {port}: {err}")

        ## Toggle digital state for 10 times. Each times delay for 0.5 second
        for i in range(10):
            if i%2 == 0:
                value = [0,1]
            else:
                value = [1,0]

            dev.DO_writePins(port, pinindex, value, timeout=timeout)
            print(f'Port: {port}, pinindex = {pinindex}, digital state = {value}')

            ## Wait for 0.5 second to see led status
            time.sleep(0.5) ## delay [s]

        ## Close pin0 and pin1 with digital output
        err = dev.DO_closePins(port, pinindex, timeout=timeout)
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