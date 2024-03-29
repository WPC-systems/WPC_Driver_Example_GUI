'''
DIO - DO_blinky_port.py with synchronous mode.

This example illustrates the process of writing a high or low signal to a DO port from USBDAQF1D.

To begin with, it demonstrates the steps required to open the DO port.
Next, in each loop, a different voltage output is applied, resulting in a blinking effect.
Lastly, it concludes by closing the DO port.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
'''

## Python
import time

## WPC

from wpcsys import pywpc


def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1D()

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
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open port with digital output
        err = dev.DO_openPort(port, timeout)
        print(f"DO_openPort in port {port}, status: {err}")

        ## Toggle digital state for 10 times. Each times delay for 0.5 second
        for i in range(10):
            state = dev.DO_togglePort(port, timeout)
            print(state)

            ## Wait for 0.5 second to see led status
            time.sleep(0.5) ## delay [s]

        ## Close port with digital output
        err = dev.DO_closePort(port, timeout)
        print(f"DO_closePort in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()